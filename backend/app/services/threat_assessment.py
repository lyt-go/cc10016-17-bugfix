"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ThreatAssessmentService(BaseModuleService):
    MODULE = "threat_assessment"
    ENTITY = "评估报告"
    OPERATION_TERM = "开始评估"
    LIST_FIELDS = ["评估对象", "威胁类别", "威胁程度", "影响范围", "缓解建议", "评估人", "评估日期", "备注说明"]
    REQUIRED_FIELDS = ["评估对象", "威胁类别", "威胁程度"]
    STATUS_ORDER = ["待评估", "评估中", "已签发", "需更新"]
    ACTION_RULES = {"开始评估": "评估中", "签发报告": "已签发", "申请更新": "需更新"}
    NEGATIVE_ACTIONS = []
