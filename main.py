# main.py
# 简单抽奖插件：/lucky_draw 返回 0-99 的随机整数
# 版本 1.0.0

from __future__ import annotations
import random

from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api import logger

@register("lucky_draw", "YourName", "简单抽奖：0-99 随机数", "1.0.0")
class LuckyDraw(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        logger.info("[lucky_draw] 插件已加载")

    async def terminate(self):
        logger.info("[lucky_draw] 插件已卸载")

    @filter.command("lucky_draw")
    async def lucky_draw(self, event: AstrMessageEvent):
        """
        用法：/lucky_draw
        生成一个 0-99 的随机整数并返回
        """
        n = random.randint(0, 99)
        # 统一使用 plain_result，适配群聊/私聊
        yield event.plain_result(f"抽奖结果：{n}")
