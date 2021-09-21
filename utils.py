import re

_headers = {
        "Connection": "keep-alive",
        "Expires": "-1",
        "Upgrade-Insecure-Requests": "-1",
        "User-Agent": (
            "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
        ),
    }

macrotrends_conversion = {
    # Income Statement
    "Revenue": "revenue",
    "Cost Of Goods Sold": "cost of goods sold",
    "Gross Profit": "gross profit",
    "Research And Development Expenses": "r&d expenses",
    "SG&A Expenses": "sg&a expenses",
    "Other Operating Income Or Expenses": "other operating income/expenses",
    "Operating Expenses": "total operating expenses",
    "Operating Income": "operating income",
    "Total Non-Operating Income/Expense": "non-operating income/expenses",
    "Pre-Tax Income": "pretax income",
    "Income Taxes": "income taxes",
    "Income After Taxes": "income after taxes",
    "Other Income": "other income",
    "Income From Continuous Operations": "income from continuous operations",
    "Income From Discontinued Operations": "income from discontinued operations",
    "Net Income": "net income",
    "EBITDA": "ebitda",
    "EBIT": "ebit",
    "Basic Shares Outstanding": "basic shares outstanding",
    "Shares Outstanding": "diluted shares outstanding",
    "Basic EPS": "basic eps",
    "EPS - Earnings Per Share": "diluted eps",

    # Balance Sheet
    "Cash On Hand": "cash and cash equivalents",
    "Receivables": "accounts receivable",
    "Inventory": "inventories",
    "Pre-Paid Expenses": "prepaid expenses",
    "Other Current Assets": "other current assets",
    "Total Current Assets": "total current assets",
    "Property, Plant, And Equipment": "property, plant and equipment",
    "Long-Term Investments": "long-term investments",
    "Goodwill And Intangible Assets": "intangible assets",
    "Other Long-Term Assets": "other non-current assets",
    "Total Long-Term Assets": "total non-current assets",
    "Total Assets": "total assets",
    "Total Current Liabilities": "total current liabilities",
    "Long Term Debt": "non-current debt",
    "Other Non-Current Liabilities": "other non-current liabilities",
    "Total Long Term Liabilities": "total non-current liabilities",
    "Total Liabilities": "total liabilities",
    "Common Stock Net": "common stock and additional paid-in capital",
    "Retained Earnings (Accumulated Deficit)": "retained earnings",
    "Comprehensive Income": "comprehensive income",
    "Other Share Holders Equity": "other shareholders equity",
    "Share Holder Equity": "total shareholders equity",
    "Total Liabilities And Share Holders Equity": "total liabilities and shareholders equity",

    # Cashflow Statement
    "Net Income/Loss": "net income cashflow statement",
    "Total Depreciation And Amortization - Cash Flow": "depreciation and amortization",
    "Other Non-Cash Items": "other non-cash items",
    "Total Non-Cash Items": "total non-cash items",
    "Change In Accounts Receivable": "change in accounts receivable",
    "Change In Inventories": "change in inventories",
    "Change In Accounts Payable": "change in accounts payable",
    "Change In Assets/Liabilities": "change in other assets/liabilities",
    "Total Change In Assets/Liabilities": "total change in assets/liabilities",
    "Cash Flow From Operating Activities": "cashflow from operating activities",
    "Net Change In Property, Plant, And Equipment": "capital expenditures",
    "Net Change In Intangible Assets": "change in intangible assets",
    "Net Acquisitions/Divestitures": "acquisitions/divestitures",
    "Net Change In Short-term Investments": "change in current investments",
    "Net Change In Long-Term Investments": "change in non-current investments",
    "Net Change In Investments - Total": "change in total investments",
    "Investing Activities - Other": "other investing activities",
    "Cash Flow From Investing Activities": "cashflow from investing activities",
    "Net Long-Term Debt": "non-current debt issued/retired",
    "Net Current Debt": "current debt issued/retired",
    "Debt Issuance/Retirement Net - Total": "total debt issued/retired",
    "Net Common Equity Issued/Repurchased": "common stock issued/repurchased",
    "Net Total Equity Issued/Repurchased": "total stock issued/repurchased",
    "Total Common And Preferred Stock Dividends Paid": "total dividends paid",
    "Financial Activities - Other": "other financing activities",
    "Cash Flow From Financial Activities": "cashflow from financing activities",
    "Net Cash Flow": "change in cash and cash equivalents",
    "Stock-Based Compensation": "stock-based compensation",
    "Common Stock Dividends Paid": "dividends paid"
}

camel_to_space = re.compile(r"(?<!^)(?=[A-Z])")

yahoo_conversion = {
    # Income Statement
    "totalRevenue": "revenue",
    "costOfRevenue": "cost of goods sold",
    "grossProfit": "gross profit",
    "researchDevelopment": "r&d expenses",
    "sellingGeneralAdministrative": "sg&a expenses",
    "nonRecurring": "non-recurring expenses",
    "otherOperatingExpenses": "other operating expenses",
    "totalOperatingExpenses": "total operating expenses",
    "operatingIncome": "operating income",
    "totalOtherIncomeExpenseNet": "other income/expenses",
    "ebit": "ebit",
    "interestExpense": "interest expenses",
    "incomeBeforeTax": "income before taxes",
    "incomeTaxExpense": "income taxes",
    "minorityInterest": "minority interest",
    "netIncomeFromContinuingOps": "income from continued operations",
    "discontinuedOperations": "income from discontinued operations",
    "extraordinaryItems": "extraordinary items",
    "effectOfAccountingCharges": "effect of accounting changes",
    "otherItems": "other items",
    "netIncome": "net income",
    "netIncomeApplicableToCommonShares": "net income attributable to common shares",

    # Balance Sheet
    "cash": "cash and cash equivalents",
    "shortTermInvestments": "short-term investments",
    "netReceivables": "acounts receivable",
    "inventory": "inventories",
    "otherCurrentAssets": "other current assets",
    "totalCurrentAssets": "total current assets",
    "longTermInvestments": "non-current investments",
    "propertyPlantEquipment": "property, plant and equipment",
    "goodWill": "goodwill",
    "intangibleAssets": "intagible assets",
    "otherAssets": "other non-current assets",
    "totalAssets": "total assets",
    "accountsPayable": "accounts payable",
    "shortLongTermDebt": "current debt",
    "otherCurrentLiab": "other current liabilities",
    "longTermDebt": "non-current debt",
    "deferredLongTermAssetCharges": "deferred long-term asset charges",
    "deferredLongTermLiab": "deferred long-term liabilities",
    "otherLiab": "other liabilities",
    "totalCurrentLiabilities": "total current liabilities",
    "totalLiab": "total liabities",
    "commonStock": "common stock",
    "retainedEarnings": "retained earnings",
    "treasuryStock": "treasury stock",
    "otherStockholderEquity": "other shareholders equity",
    "totalStockholderEquity": "total shareholders equity",
    "netTangibleAssets": "tangible assets",

    # Cashflow Statement
    "netIncome": "net income",
    "depreciation": "depreciation and amortization",
    "changeToNetincome": "other non-cash items",
    "changeToAccountReceivables": "change in accounts receivable",
    "changeToLiabilities": "change in liabilities",
    "changeToInventory": "change in inventories",
    "changeToOperatingActivities": "other operating activities",
    "effectOfExchangeRate": "gains/losses on currency changes",
    "totalCashFromOperatingActivities": "cashflow from operating activities",
    "capitalExpenditures": "capital expenditures",
    "investments": "change in total investments",
    "otherCashflowsFromInvestingActivities": "other investing activities",
    "totalCashflowsFromInvestingActivities": "cashflow from investing activities",
    "dividendsPaid": "total dividends paid",
    "netBorrowings": "total debt issued/retired",
    "otherCashflowsFromFinancingActivities": "other financing activities",
    "totalCashFromFinancingActivities": "cashflow from financing activities",
    "changeInCash": "change in cash and cash equivalents",
    "repurchaseOfStock": "total stock repurchased",
    "issuanceOfStock": "total stock issued"
}

class TickerError(ValueError):
    pass

class DatasetError(KeyError):
    pass