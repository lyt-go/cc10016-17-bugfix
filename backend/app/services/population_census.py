"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class PopulationCensusService(BaseModuleService):
    MODULE = "population_census"
    ENTITY = "普查记录"
    OPERATION_TERM = "执行普查"
    LIST_FIELDS = ["普查区域", "目标物种", "调查方法", "目击数量", "置信区间", "普查人", "普查日期", "备注说明"]
    REQUIRED_FIELDS = ["普查区域", "目标物种", "调查方法"]
    STATUS_ORDER = ["待普查", "已普查", "已确认", "需重查"]
    ACTION_RULES = {"执行普查": "已普查", "确认结果": "已确认", "申请重查": "需重查"}
    NEGATIVE_ACTIONS = []
