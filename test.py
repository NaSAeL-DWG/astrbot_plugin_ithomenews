import httpx
import atoma
from bs4 import BeautifulSoup

async def get_pure_text(html_str):
    if not html_str:
        return ""
    soup = BeautifulSoup(html_str, "html.parser")
    return soup.get_text(separator=" ", strip=True)

_url = "https://www.ithome.com/rss"

async def get_news():
    try:
        with httpx.Client() as client:
            _response = client.get(_url)
        feed = atoma.parse_rss_bytes(_response.content)
        _news= ""
        for item in feed.items[:30]: 
            _news += f"标题: {item.title}\n"
            raw_html = item.description
            pure_text = await get_pure_text(raw_html)
            _news += f"正文摘要: {pure_text}\n"

    except Exception as e:
        print(f"发生错误: {e}")
