"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class RescueRecordService(BaseModuleService):
    MODULE = "rescue_record"
    ENTITY = "救护档案"
    OPERATION_TERM = "开始救护"
    LIST_FIELDS = ["救护对象", "发现地点", "伤病情況", "救护措施", "康复状态", "救护人", "救护日期", "备注说明"]
    REQUIRED_FIELDS = ["救护对象", "发现地点", "伤病情況"]
    STATUS_ORDER = ["待救护", "救护中", "已康复", "已放归"]
    ACTION_RULES = {"开始救护": "救护中", "记录康复": "已康复", "确认放归": "已放归"}
    NEGATIVE_ACTIONS = []
