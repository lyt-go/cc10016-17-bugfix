"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class HabitatSurveyService(BaseModuleService):
    MODULE = "habitat_survey"
    ENTITY = "调查数据"
    OPERATION_TERM = "开始调查"
    LIST_FIELDS = ["调查区域", "植被类型", "水源距离", "人为干扰", "食物丰富度", "调查人", "调查日期", "备注说明"]
    REQUIRED_FIELDS = ["调查区域", "植被类型", "水源距离"]
    STATUS_ORDER = ["待调查", "调查中", "已报告", "需复查"]
    ACTION_RULES = {"开始调查": "调查中", "提交报告": "已报告", "申请复查": "需复查"}
    NEGATIVE_ACTIONS = []
