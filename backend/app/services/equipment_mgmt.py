"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class EquipmentMgmtService(BaseModuleService):
    MODULE = "equipment_mgmt"
    ENTITY = "装备档案"
    OPERATION_TERM = "确认领用"
    LIST_FIELDS = ["装备名称", "装备类型", "购入日期", "使用状态", "保管人", "存放位置", "上次维护", "备注说明"]
    REQUIRED_FIELDS = ["装备名称", "装备类型", "购入日期"]
    STATUS_ORDER = ["在库", "已领用", "使用中", "待维修"]
    ACTION_RULES = {"确认领用": "已领用", "归还登记": "使用中", "报修处理": "待维修"}
    NEGATIVE_ACTIONS = []
