#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot

from nonebot.adapters.mirai2 import Adapter as MIRAI2Adapter  

nonebot.init(apscheduler_autostart=True)
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(MIRAI2Adapter) 

nonebot.load_from_toml("pyproject.toml")

nonebot.load_plugins('src/plugins')

if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!"
    )
    nonebot.run(app="__mp_main__:app")
