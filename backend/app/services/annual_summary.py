"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class AnnualSummaryService(BaseModuleService):
    MODULE = "annual_summary"
    ENTITY = "总结报告"
    OPERATION_TERM = "提交报告"
    LIST_FIELDS = ["报告年份", "覆盖物种", "主要发现", "数据总量", "保护建议", "编制人", "报告状态", "备注说明"]
    REQUIRED_FIELDS = ["报告年份", "覆盖物种", "主要发现"]
    STATUS_ORDER = ["编制中", "已提交", "已审核", "已发布"]
    ACTION_RULES = {"提交报告": "已提交", "审核通过": "已审核", "发布报告": "已发布"}
    NEGATIVE_ACTIONS = []
