"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class PhotoArchiveService(BaseModuleService):
    MODULE = "photo_archive"
    ENTITY = "影像记录"
    OPERATION_TERM = "整理归档"
    LIST_FIELDS = ["拍摄对象", "拍摄地点", "影像类型", "存储路径", "拍摄时间", "拍摄人", "标签信息", "备注说明"]
    REQUIRED_FIELDS = ["拍摄对象", "拍摄地点", "影像类型"]
    STATUS_ORDER = ["待整理", "已整理", "已归档", "待标注"]
    ACTION_RULES = {"整理归档": "已整理", "添加标签": "已归档", "标注信息": "待标注"}
    NEGATIVE_ACTIONS = []
