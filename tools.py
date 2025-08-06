from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
import json

@tool
def web_searchtool(query:str):
    """searches the web and return the results."""
    search_tool=DuckDuckGoSearchResults(num_results=10,verbose=True)
    return search_tool.run(query)
