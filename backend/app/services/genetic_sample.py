"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class GeneticSampleService(BaseModuleService):
    MODULE = "genetic_sample"
    ENTITY = "样本档案"
    OPERATION_TERM = "登记样本"
    LIST_FIELDS = ["样本编号", "来源个体", "样本类型", "采集方法", "保存条件", "采集人", "采集日期", "备注说明"]
    REQUIRED_FIELDS = ["样本编号", "来源个体", "样本类型"]
    STATUS_ORDER = ["待采集", "已采集", "已入库", "已送检"]
    ACTION_RULES = {"登记样本": "已采集", "样本入库": "已入库", "送检分析": "已送检"}
    NEGATIVE_ACTIONS = []
