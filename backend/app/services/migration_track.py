"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class MigrationTrackService(BaseModuleService):
    MODULE = "migration_track"
    ENTITY = "迁徙路径"
    OPERATION_TERM = "绘制路线"
    LIST_FIELDS = ["追踪个体", "起点区域", "途经区域", "终点区域", "迁徙距离", "记录人", "记录时段", "备注说明"]
    REQUIRED_FIELDS = ["追踪个体", "起点区域", "途经区域"]
    STATUS_ORDER = ["待绘制", "已绘制", "已验证", "待更新"]
    ACTION_RULES = {"绘制路线": "已绘制", "验证路线": "已验证", "更新路线": "待更新"}
    NEGATIVE_ACTIONS = []
