import calendar
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from finance_data.utils import HEADERS, DatasetError

class MarketscreenerReader:
    _base_url = "https://www.marketscreener.com"
    
    def __init__(self, identifier) -> None:
        params = {
            "q": identifier
        }
        html = requests.get(url=f"{self._base_url}/search/", params=params, headers=HEADERS).text
        soup = BeautifulSoup(html)
        
        try:
            company_tag = soup.find("table", {"class": "table table--small table--hover table--centered table--bordered"}).find("tbody").find_all("tr")[0].find("td").find("a")
        except AttributeError:
            raise DatasetError(f"no stock found for identifier '{identifier}'")
        
        self._company_url = f"{self._base_url}{company_tag.get('href')}"
        self._header_parsed = False

    def country_information(self) -> dict:
        if not hasattr(self, "_company_soup"):
            self._get_company_information()

        header = self._company_soup.find("b", text="Sales per region")
        if header is None:
            raise DatasetError(f"no country data found for stock '{self.name}'")
        else:
            rows = header.find_next("tr").find("td", recursive=False).find("table").find_all("tr")
        
        if rows[0].find_all("td")[-1].text == "Delta":
            years = {
                index+1: int(tag.find("b").text)
                for index, tag in enumerate(rows[0].find_all("td")[1:-1])
            }
        else:
            years = {
                index+1: int(tag.find("b").text)
                for index, tag in enumerate(rows[0].find_all("td")[1:])
            }
        data = {}
        for year in sorted(years.values(), reverse=True):
            data[year] = {}

        for row in rows[1:-1]:
            cells = row.find_all("td")
            name = cells[0].text.title()
            for index, cell in enumerate(cells[1:-1:2]):
                data[years[index+1]][name] = float(cell.text.replace(" ", "")) * 1e6 if cell.text != "-" else None
        
        return data

    def segment_information(self) -> dict:
        if not hasattr(self, "_company_soup"):
            self._get_company_information()
        
        header = self._company_soup.find("b", text="Sales per Business")
        if header is None:
            raise DatasetError(f"no segment data found for stock '{self.name}'")
        else:
            rows = header.find_next("tr").find("td", recursive=False).find("table").find_all("tr")
        
        if rows[0].find_all("td")[-1].text == "Delta":
            years = {
                index+1: int(tag.find("b").text)
                for index, tag in enumerate(rows[0].find_all("td")[1:-1])
            }
        else:
            years = {
                index+1: int(tag.find("b").text)
                for index, tag in enumerate(rows[0].find_all("td")[1:])
            }
        data = {}
        for year in sorted(years.values(), reverse=True):
            data[year] = {}

        for row in rows[1:-1]:
            cells = row.find_all("td")
            name = cells[0].text
            for index, cell in enumerate(cells[1:-1:2]):
                data[years[index+1]][name] = float(cell.text.replace(" ", "")) * 1e6 if cell.text != "-" else None
        
        return data

    def _get_company_information(self) -> None:
        url = f"{self._company_url}/company/"
        html = requests.get(url=url, headers=HEADERS).text
        self._company_soup = BeautifulSoup(html)

    def _get_financial_information(self) -> None:
        url = f"{self._company_url}/financials/"
        html = requests.get(url=url, headers=HEADERS).text
        self._financial_soup = BeautifulSoup(html)
    
    def _parse_header(self) -> None:
        if self._header_parsed:
            return
        if hasattr(self, "_financial_soup"):
            soup = self._financial_soup
        elif hasattr(self, "_company_soup"):
            soup = self._company_soup
        else:
            self._get_financial_information()
            soup = self._financial_soup
        
        ticker, isin = soup.find("div", {"class": "bc_pos"}).find("span", {"class": "bc_add"}).find_all("span")
        self._ticker = ticker.text.strip()
        self._isin = isin.text.strip()
        
        self._name = re.findall("(.+)\(.+\)", soup.find("h1").parent.text.strip())[0].strip()
        
        price_tag = soup.find("span", {"class": "last variation--no-bg txt-bold"})
        self._price = float(price_tag.text)
        self._currency = price_tag.find_next("td").text.strip()
        
        self._header_parsed = True