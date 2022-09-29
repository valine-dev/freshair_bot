<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="./logo.jpg" style="width:100px; height:100px; border-radius:100%; overflow:hidden;" alt="nonebot"></a>
</p>

<div align="center">

# 新空 BOT

</div>

> 您现在正在阅读：正经版 README

一个基于 Nonebot2 / Mirai 的 QQ 群聊机器人，为长安大学新鲜空气动漫社群提供新人服务（分群表、常见）及丰富日常群聊趣味的功能。

## 部署


### 参考资料

本项目是标准的 Nonebot2 项目，由使用 nb-cli 搭建的框架与自制插件构成，因此部署方法与 [Nonebot2 文档](https://v2.nonebot.dev/)中叙述的叙述的方式一致，但请注意每个插件自有的配置文件，即便它们也会读取环境变量中确定的配置。

并且，由于本 BOT 默认使用了 Mirai 协议（并在插件中使用了大量 Mirai 特有 API）请参考 [mirai2 Adapter 的配置说明](https://github.com/ieew/nonebot_adapter_mirai2/wiki)

## 插件

除去部分基础的、管理用插件外，新空 BOT 由以下自制插件组成

> **请注意**，一切 `config.py` 内的配置都是 **默认配置** 如非必要（如多行文字等情况），请勿直接修改 `config.py` ，而是在 `.env.*` 下修改相应的键值

### good_fortune

一个将当前日期及用户 prompt hash 之后计算出的随机运势，并附加来自 Hitokoto 的签语。

链接Hitokoto或许需要您使用代理，请在`good_fortune/config.py`下查阅相关配置

您需要在`results`文件中编辑签语，用 *** 隔开普通签和特殊签并用 /// 隔开每个签语

### rookie_kit

迎新、回答常见问题用插件。可以在配置文件中编辑起作用的 QQ 群号、迎新消息和常见问题的关键字及回答，具体配置请查阅`rookie_kit/config.py`

### repeater_killer

新空传统艺能插件，可以在`repeater_killer/config.py`下查阅特定配置
