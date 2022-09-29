'''迎新系统:
    迎新系统是新空BOT建立最初的目的，该插件承担了以下功能
    - 分群表的随时调用
    - 回答新人的常见疑惑
    Usage:
    (当新人加入群时) -> 发送迎新消息
    用户：[带关键词的问题] -> 发送相应回答
'''
from os.path import abspath

import nonebot
from nonebot import on_message, on_notice
from nonebot.adapters import Bot, Event, Message
from nonebot.adapters.mirai2 import MessageSegment
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State

from .config import Config

# 从全局配置读取配置
plugin_config = Config.parse_obj(nonebot.get_driver().config)

# 创建 Matcher
greeting = on_notice()
faq = on_message(rule=to_me())


def read_message(raw: str, target: int) -> Message[MessageSegment]:
    """说明:
        读入定义的欢迎信息为 Message 对象

    参数:
        raw (str): 原文本
        target (int): 对话的目标 QQ 号，用以At

    Returns:
        Message[MessageSegment]: _description_
    """    
    raw_segments = raw.split('/')
    segments = []
    for seg in raw_segments:
        fine = seg.split(':')
        match fine[0]:
            case 'txt':
                segments.append(
                    MessageSegment.plain(fine[1])
                )
            case 'img':
                segments.append(
                    MessageSegment.image(
                        abspath(f'./resource/{fine[1]}')
                    )
                )
            case 'at':
                segments.append(
                    MessageSegment.at(target)
                )
    return Message(segments)  # type: ignore


# 处理新人入群啊嗯
@greeting.handle()
async def greets(bot: Bot, event: Event, state: T_State):
    if not event.get_type() == "MemberJoinEvent":
        # 只处理加群请求
        await greeting.finish()
    