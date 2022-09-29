from typing import List
from pydantic import BaseSettings


class Config(BaseSettings):
    # 生效的QQ群号
    rookie_control_groups: List = ['群号A', '群号B']

    '''欢迎消息，用“/”给消息分段，每段消息前可以使用
        txt: 纯文本信息
        img: resource文件夹下的图片
        at @新人
        atall @全体成员
    作为前缀
    '''
    greets: str = '''
    at/txt:欢迎进入新鲜空气动漫社，入群请修改群名片哦(名片前面加上和其他群员一样的数字，新生改为⑱)/img:grps.png
    '''
    # 常见问题，格式为{'触发词': '回答'}，回答的文本格式也参考欢迎消息的格式
    faq: dict = {
        '龙图': 'txt:nmsl',
        '分群表': 'img:grps.png'
    }

    class Config:
        extra = "ignore"
