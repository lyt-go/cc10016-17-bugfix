"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class CooperationProjectService(BaseModuleService):
    MODULE = "cooperation_project"
    ENTITY = "项目档案"
    OPERATION_TERM = "确认立项"
    LIST_FIELDS = ["项目名称", "合作机构", "项目周期", "参与人员", "项目目标", "负责人", "项目状态", "备注说明"]
    REQUIRED_FIELDS = ["项目名称", "合作机构", "项目周期"]
    STATUS_ORDER = ["待立项", "已立项", "进行中", "已结题"]
    ACTION_RULES = {"确认立项": "已立项", "启动项目": "进行中", "结题归档": "已结题"}
    NEGATIVE_ACTIONS = []
