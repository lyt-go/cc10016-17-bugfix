"""领域服务注册表：通用资源路由按模块 key 分派到独立业务服务。"""
from __future__ import annotations

from app.services.base import BaseModuleService
from app.services.species_register import SpeciesRegisterService
from app.services.tracking_device import TrackingDeviceService
from app.services.location_record import LocationRecordService
from app.services.behavior_observe import BehaviorObserveService
from app.services.habitat_survey import HabitatSurveyService
from app.services.population_census import PopulationCensusService
from app.services.migration_track import MigrationTrackService
from app.services.rescue_record import RescueRecordService
from app.services.genetic_sample import GeneticSampleService
from app.services.patrol_record import PatrolRecordService
from app.services.photo_archive import PhotoArchiveService
from app.services.research_output import ResearchOutputService
from app.services.threat_assessment import ThreatAssessmentService
from app.services.equipment_mgmt import EquipmentMgmtService
from app.services.public_education import PublicEducationService
from app.services.cooperation_project import CooperationProjectService
from app.services.data_analysis import DataAnalysisService
from app.services.annual_summary import AnnualSummaryService

SERVICES: dict[str, BaseModuleService] = {
    "species_register": SpeciesRegisterService(),
    "tracking_device": TrackingDeviceService(),
    "location_record": LocationRecordService(),
    "behavior_observe": BehaviorObserveService(),
    "habitat_survey": HabitatSurveyService(),
    "population_census": PopulationCensusService(),
    "migration_track": MigrationTrackService(),
    "rescue_record": RescueRecordService(),
    "genetic_sample": GeneticSampleService(),
    "patrol_record": PatrolRecordService(),
    "photo_archive": PhotoArchiveService(),
    "research_output": ResearchOutputService(),
    "threat_assessment": ThreatAssessmentService(),
    "equipment_mgmt": EquipmentMgmtService(),
    "public_education": PublicEducationService(),
    "cooperation_project": CooperationProjectService(),
    "data_analysis": DataAnalysisService(),
    "annual_summary": AnnualSummaryService(),
}


def service_for(module: str) -> BaseModuleService | None:
    return SERVICES.get(module)
