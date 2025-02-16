from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile", 
                 api_key= "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"),
                tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
                show_tool_calls= True,
                markdown=True,
                instructions=["Use tavbles to display data",
                              "If you are unable to find the company, the symbol for a company is not know, use the get_company_symbol tool to find the synbol."],
                debug_mode= True
                 )


agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
