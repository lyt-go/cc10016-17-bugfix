"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SpeciesRegisterService(BaseModuleService):
    MODULE = "species_register"
    ENTITY = "物种档案"
    OPERATION_TERM = "确认入库"
    LIST_FIELDS = ["物种名称", "保护等级", "分布区域", "种群数量", "栖息地类型", "登记人", "登记日期", "备注说明"]
    REQUIRED_FIELDS = ["物种名称", "保护等级", "分布区域"]
    STATUS_ORDER = ["待登记", "已入库", "已更新", "已存档"]
    ACTION_RULES = {"确认入库": "已入库", "更新信息": "已更新", "存档记录": "已存档"}
    NEGATIVE_ACTIONS = []
