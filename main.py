from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core.utils.astrbot_path import get_astrbot_data_path
import httpx

plugin_data_path = get_astrbot_data_path() / "plugin_data" / self.name 
@register("rssnews", "NaSAeL", "获取rss订阅新闻", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.context.add_llm_tools(get_news_from_rss())

    async def get_pure_text(html_str):
        if not html_str:
            return ""
        soup = BeautifulSoup(html_str, "html.parser")
        return soup.get_text(separator=" ", strip=True)

    @filter.llm_tool(name="get_news_from_rss")
    async def get_news_from_rss(self,_url:str="https://www.ithome.com/rss",_count:int=30):
        '''获取rss订阅新闻
        
        Args:
            _url (string): rss订阅地址
            _count (number): 发送给模型的新闻数量
        '''
        try:
            with httpx.Client() as client:
                _response = client.get(_url)
            feed = atoma.parse_rss_bytes(_response.content)
            _news= ""
            for item in feed.items[:_count]: 
                _news += f"标题: {item.title}\n"
                raw_html = item.description
                pure_text = await get_pure_text(raw_html)
                _news += f"正文摘要: {pure_text}\n"
           

        except Exception as e:
            print(f"发生错误: {e}")
        return _news