"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class LocationRecordService(BaseModuleService):
    MODULE = "location_record"
    ENTITY = "位置数据"
    OPERATION_TERM = "清洗数据"
    LIST_FIELDS = ["设备编号", "经纬度", "海拔高度", "移动速度", "温度读数", "记录时间", "数据来源", "备注说明"]
    REQUIRED_FIELDS = ["设备编号", "经纬度", "海拔高度"]
    STATUS_ORDER = ["已接收", "已清洗", "已标注", "异常数据"]
    ACTION_RULES = {"清洗数据": "已清洗", "标注异常": "已标注", "重采样数据": "异常数据"}
    NEGATIVE_ACTIONS = []
