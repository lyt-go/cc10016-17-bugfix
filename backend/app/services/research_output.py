"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ResearchOutputService(BaseModuleService):
    MODULE = "research_output"
    ENTITY = "研究产出"
    OPERATION_TERM = "确认登记"
    LIST_FIELDS = ["成果标题", "研究主题", "作者团队", "发表渠道", "发表年份", "引用次数", "登记人", "备注说明"]
    REQUIRED_FIELDS = ["成果标题", "研究主题", "作者团队"]
    STATUS_ORDER = ["待登记", "已登记", "已发表", "已引用"]
    ACTION_RULES = {"确认登记": "已登记", "标记发表": "已发表", "记录引用": "已引用"}
    NEGATIVE_ACTIONS = []
