"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class DataAnalysisService(BaseModuleService):
    MODULE = "data_analysis"
    ENTITY = "分析记录"
    OPERATION_TERM = "开始分析"
    LIST_FIELDS = ["分析主题", "数据来源", "分析方法", "分析结论", "可视化产出", "分析人", "分析日期", "备注说明"]
    REQUIRED_FIELDS = ["分析主题", "数据来源", "分析方法"]
    STATUS_ORDER = ["待分析", "分析中", "已报告", "待复核"]
    ACTION_RULES = {"开始分析": "分析中", "提交报告": "已报告", "申请复核": "待复核"}
    NEGATIVE_ACTIONS = []
