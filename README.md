# astrbot_plugin_rss

这是一个为 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 开发的 RSS 订阅新闻获取插件。

可以让大模型（LLM）通过调用工具直接获取 RSS 订阅（默认配置为 IT之家）的新闻内容，并根据用户的提问进行总结和回答。

## 🌟 功能

- 提供 `@filter.llm_tool()` 给大语言模型，使其能够自主拉取并阅读 RSS 新闻。
- 支持在插件配置中自定义 RSS 订阅源地址。
- 支持配置每次发给大模型解析的新闻条数限制。

## 📦 安装

在 AstrBot 的元信息管理面板中，通过从 GitHub 链接安装：
https://github.com/NaSAeL-DWG/astrbot_plugin_ithomenews

或者将此代码仓库克隆到你的 AstrBot 的 `data/plugins/` 目录下。

## ⚙️ 配置项

安装完成后，在 AstrBot 管理面板或 `data/config.yaml` 中配置插件参数（参数 schema 定义在 `_conf_schema.json` 中）：

| 参数名  | 类型   | 说明                         | 默认值                       |
| :------ | :----- | :--------------------------- | :--------------------------- |
| `url`   | string | RSS 订阅地址                 | `https://www.ithome.com/rss` |
| `count` | int    | 每次拉取发送给模型的新闻数量 | `30`                         |

## 🛠️ 使用方法

直接向具有该插件权限的机器人发送消息，例如：
- “帮我看看今天 IT之家 有什么新闻？”
- “给我总结一下最新的 RSS 订阅内容”

大语言模型会自动调用 `get_news` 工具去拉取并返回摘要内容。

## 依赖

本插件使用了以下第三方库，需要确保已安装（通常 AstrBot 运行环境中已经自带）：
- `httpx`
- `atoma`
- `beautifulsoup4`
