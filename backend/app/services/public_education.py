"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class PublicEducationService(BaseModuleService):
    MODULE = "public_education"
    ENTITY = "宣教资料"
    OPERATION_TERM = "发布资料"
    LIST_FIELDS = ["资料名称", "宣教主题", "目标受众", "资料形式", "发布日期", "制作人", "使用次数", "备注说明"]
    REQUIRED_FIELDS = ["资料名称", "宣教主题", "目标受众"]
    STATUS_ORDER = ["制作中", "已发布", "已下架", "待更新"]
    ACTION_RULES = {"发布资料": "已发布", "下架资料": "已下架", "更新内容": "待更新"}
    NEGATIVE_ACTIONS = []
