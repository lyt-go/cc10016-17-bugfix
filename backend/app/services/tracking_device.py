"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TrackingDeviceService(BaseModuleService):
    MODULE = "tracking_device"
    ENTITY = "设备档案"
    OPERATION_TERM = "确认部署"
    LIST_FIELDS = ["设备编号", "设备类型", "佩戴对象", "信号频率", "电池续航", "部署日期", "负责人", "备注说明"]
    REQUIRED_FIELDS = ["设备编号", "设备类型", "佩戴对象"]
    STATUS_ORDER = ["待部署", "已部署", "信号正常", "已回收"]
    ACTION_RULES = {"确认部署": "已部署", "标记正常": "信号正常", "回收设备": "已回收"}
    NEGATIVE_ACTIONS = []
