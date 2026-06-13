from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# 🔍 SEARCH TOOL
@tool
def web_search(query: str) -> str:
    """Return structured search results."""

    results = tavily.search(query=query, max_results=5)

    cleaned = []

    for r in results.get("results", []):
        cleaned.append({
            "title": r.get("title"),
            "url": r.get("url"),
            "snippet": (r.get("content") or "")[:200]
        })

    return str(cleaned)


# 🌐 SCRAPER TOOL
@tool
def scrape_url(url: str) -> str:
    """Scrape clean text safely."""

    try:
        resp = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:3000]

    except Exception as e:
        return f"SCRAPE_FAILED: {str(e)}"