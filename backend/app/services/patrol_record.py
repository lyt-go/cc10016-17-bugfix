"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class PatrolRecordService(BaseModuleService):
    MODULE = "patrol_record"
    ENTITY = "巡护日志"
    OPERATION_TERM = "提交日志"
    LIST_FIELDS = ["巡护路线", "巡护人员", "发现情况", "威胁类型", "处置措施", "巡护日期", "环境条件", "备注说明"]
    REQUIRED_FIELDS = ["巡护路线", "巡护人员", "发现情况"]
    STATUS_ORDER = ["待填写", "已填写", "已审阅", "需跟进"]
    ACTION_RULES = {"提交日志": "已填写", "审阅通过": "已审阅", "标记跟进": "需跟进"}
    NEGATIVE_ACTIONS = []
