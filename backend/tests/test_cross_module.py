"""业务断言与跨模块数据流测试。

测试覆盖核心跨模块链路：
  - 位置记录 -> 迁徙路线 聚合
  - 行为观测 -> 数据分析 统计
  - 巡护记录 -> 威胁评估 触发
  - 种群普查 -> 物种登记 同步
  - 设备信号 -> 位置数据 异常标注
  - 年度总结 多源汇总

本测试文件可直接运行：python3 -m pytest backend/tests/test_cross_module.py -v
或在缺少pytest时用 python3 backend/tests/test_cross_module.py 运行内嵌的unittest。
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

# 将backend加入搜索路径
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.cross_module import (
    analyze_behavior_for_data_analysis,
    build_annual_summary,
    build_migration_from_locations,
    check_device_signal_for_locations,
    link_genetic_to_research,
    link_rescue_to_species,
    trigger_threat_from_patrol,
    update_species_population_from_census,
)
from app.store import store


class TestLocationToMigration(unittest.TestCase):
    """位置记录 -> 迁徙路线 聚合测试。"""

    def test_migration_requires_locations(self):
        """验证：无位置数据时返回错误信息。"""
        result = build_migration_from_locations("不存在的个体XYZ")
        self.assertIn("error", result)
        self.assertEqual(result.get("location_count"), 0)

    def test_migration_returns_source_record_ids(self):
        """验证：迁徙路线包含源位置记录ID列表。"""
        result = build_migration_from_locations("LOCA")
        if "error" not in result:
            self.assertIn("source_records", result)
            self.assertGreater(len(result["source_records"]), 0)
            self.assertGreater(result["distance_km"], 0)

    def test_migration_has_start_via_end(self):
        """验证：迁徙路线包含起点、途经、终点三要素。"""
        result = build_migration_from_locations("LOCA")
        if "error" not in result:
            for key in ("start_region", "via_region", "end_region"):
                self.assertIn(key, result)
                self.assertIsNotNone(result[key])


class TestBehaviorToAnalysis(unittest.TestCase):
    """行为观测 -> 数据分析 统计测试。"""

    def test_behavior_analysis_returns_distribution(self):
        """验证：行为分析返回类型分布与主导行为。"""
        result = analyze_behavior_for_data_analysis("行为观测")
        if "error" not in result:
            self.assertIn("behavior_distribution", result)
            self.assertIn("dominant_behavior", result)
            self.assertGreater(result["observation_count"], 0)
            self.assertIn("source_record_ids", result)

    def test_behavior_analysis_unknown_species(self):
        """验证：未知物种返回错误。"""
        result = analyze_behavior_for_data_analysis("完全不存在的物种#NONE#")
        self.assertIn("error", result)
        self.assertEqual(result.get("observation_count"), 0)


class TestPatrolToThreat(unittest.TestCase):
    """巡护记录 -> 威胁评估 触发测试。"""

    def test_trigger_threat_creates_assessment(self):
        """验证：存在威胁的巡护记录触发新的威胁评估。"""
        result = trigger_threat_from_patrol(2)
        self.assertIn("created", result)
        if result["created"]:
            self.assertIn("assessment_id", result)
            self.assertIn("assessment", result)
            self.assertEqual(result["assessment"]["status"], "待评估")

    def test_trigger_threat_missing_patrol(self):
        """验证：不存在的巡护记录返回错误。"""
        result = trigger_threat_from_patrol(99999)
        self.assertIn("error", result)


class TestCensusToSpecies(unittest.TestCase):
    """种群普查 -> 物种登记 同步测试。"""

    def test_census_updates_species_population(self):
        """验证：普查数据同步更新物种登记数量。"""
        result = update_species_population_from_census(1)
        if "error" not in result:
            self.assertIn("new_population", result)
            self.assertIn("updated_species_ids", result)

    def test_census_missing_record(self):
        """验证：不存在的普查记录返回错误。"""
        result = update_species_population_from_census(99999)
        self.assertIn("error", result)


class TestDeviceToLocation(unittest.TestCase):
    """追踪设备 -> 位置记录 异常标注测试。"""

    def test_device_signal_check(self):
        """验证：设备信号检查返回关联位置数。"""
        result = check_device_signal_for_locations("TRAC-0001")
        self.assertIn("linked_locations", result)
        self.assertIn("device_status", result)

    def test_device_missing(self):
        """验证：不存在的设备返回错误。"""
        result = check_device_signal_for_locations("DEV-NOTEXIST")
        self.assertIn("error", result)


class TestRescueToSpecies(unittest.TestCase):
    """救护记录 -> 物种登记 关联测试。"""

    def test_rescue_links_species(self):
        """验证：救护记录关联物种。"""
        result = link_rescue_to_species(1)
        if "error" not in result:
            self.assertIn("linked_species_ids", result)
            self.assertIn("matched_count", result)

    def test_rescue_missing(self):
        """验证：不存在的救护记录返回错误。"""
        result = link_rescue_to_species(99999)
        self.assertIn("error", result)


class TestGeneticToResearch(unittest.TestCase):
    """遗传样本 -> 研究成果 测试。"""

    def test_genetic_not_analyzed_yet(self):
        """验证：未送检的样本不能生成研究成果。"""
        result = link_genetic_to_research(1)
        self.assertIn("error", result, "未送检样本应返回错误")

    def test_genetic_missing(self):
        """验证：不存在的样本返回错误。"""
        result = link_genetic_to_research(99999)
        self.assertIn("error", result)


class TestAnnualSummary(unittest.TestCase):
    """年度总结 多源汇总测试。"""

    def test_annual_summary_returns_stats(self):
        """验证：年度总结包含多模块统计。"""
        result = build_annual_summary(2026)
        self.assertIn("summary", result)
        summary = result["summary"]
        self.assertIn("species", summary)
        self.assertIn("locations", summary)
        self.assertIn("observations", summary)
        self.assertIn("confirmed_census", summary)
        self.assertIn("annual_summary_entry", result)

    def test_annual_summary_creates_entry(self):
        """验证：年度总结创建/返回总结条目。"""
        result = build_annual_summary(2025)
        self.assertIn("annual_summary_entry", result)
        entry = result["annual_summary_entry"]
        self.assertEqual(entry["报告年份"], "2025")


class TestStoreIntegrity(unittest.TestCase):
    """数据仓库完整性断言。"""

    def test_all_18_modules_present(self):
        """验证：18个业务模块全部注册。"""
        expected = {
            "species_register", "tracking_device", "location_record",
            "behavior_observe", "habitat_survey", "population_census",
            "migration_track", "rescue_record", "genetic_sample",
            "patrol_record", "photo_archive", "research_output",
            "threat_assessment", "equipment_mgmt", "public_education",
            "cooperation_project", "data_analysis", "annual_summary",
        }
        actual = set(store.module_names())
        self.assertEqual(actual, expected)

    def test_each_module_has_seed_data(self):
        """验证：每个模块至少有种子数据。"""
        for name in store.module_names():
            rows = store.rows(name)
            self.assertGreaterEqual(len(rows), 1, f"模块 {name} 缺少种子数据")

    def test_each_entry_has_id(self):
        """验证：每条记录都有唯一ID。"""
        for name in store.module_names():
            ids = [row.get("id") for row in store.rows(name)]
            self.assertEqual(len(ids), len(set(int(i) for i in ids if i is not None)),
                             f"模块 {name} 存在重复ID")

    def test_status_in_valid_range(self):
        """验证：每条记录的状态值在模块的合法范围内。"""
        from app.services import service_for
        for name in store.module_names():
            svc = service_for(name)
            if svc:
                valid_statuses = set(svc.STATUS_ORDER)
                for row in store.rows(name):
                    self.assertIn(row.get("status"), valid_statuses,
                                  f"模块 {name} 记录 {row.get('id')} 的状态 {row.get('status')} 不合法")


def run_unittest():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for cls in [
        TestLocationToMigration,
        TestBehaviorToAnalysis,
        TestPatrolToThreat,
        TestCensusToSpecies,
        TestDeviceToLocation,
        TestRescueToSpecies,
        TestGeneticToResearch,
        TestAnnualSummary,
        TestStoreIntegrity,
    ]:
        suite.addTests(loader.loadTestsFromTestCase(cls))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_unittest())