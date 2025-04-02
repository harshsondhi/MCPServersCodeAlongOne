from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
from bs4 import BeautifulSoup
import json


load_dotenv()

mcp = FastMCP("tech_news")

USER_AGENT = "news-app/1.0"

NEWS_SITES = {
    "arstechnica": "https://arstechnica.com"
}

async def fetch_news(url: str):
    """ It pulls and summarizes the latest news from the specified news site"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url,  timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            text = "".join([p.get_text() for p in paragraphs[:5]])
            return text
            
        except httpx.TimeoutException:
            print("Timeout occurred while fetching news.")
            return "Timeout error"
        
        
        
@mcp.tool()
async def get_tech_news(source: str):
    """
    Fetches the latest news from a specified source and summarizes it.
    Args:
        source (str): The news source to fetch from.(for example: arstechnica or techcrunch)
    Returns:
        str: The summarized news content.
    """
    if source not in NEWS_SITES:
        return ValueError(f"Invalid source {source}. Available sources are: arstechnica, techcrunch.")
    
    url = NEWS_SITES[source]
    news_content = await fetch_news(url)
    
    if news_content == "Timeout error":
        return "Failed to fetch news due to timeout."
    
    return news_content[:300]



# def main():
#     print("Hello from mcp-server-project!")


if __name__ == "__main__":
    mcp.run(transport="stdio")
