"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class BehaviorObserveService(BaseModuleService):
    MODULE = "behavior_observe"
    ENTITY = "观测记录"
    OPERATION_TERM = "提交记录"
    LIST_FIELDS = ["观测对象", "行为类型", "起止时间", "参与个体数", "环境条件", "观测人", "观测日期", "备注说明"]
    REQUIRED_FIELDS = ["观测对象", "行为类型", "起止时间"]
    STATUS_ORDER = ["待提交", "已提交", "已审核", "待补充"]
    ACTION_RULES = {"提交记录": "已提交", "审核通过": "已审核", "退回补充": "待补充"}
    NEGATIVE_ACTIONS = []
