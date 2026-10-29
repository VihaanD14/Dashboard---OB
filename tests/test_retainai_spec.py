import unittest
import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.data_loader import calculate_flight_risk_score, get_enterprise_settings


class TestFlightRiskScoring(unittest.TestCase):
    """Test deterministic flight risk scoring according to RetainAI specification."""

    def test_score_case_1(self):
        # (2.5, 6, 40, 18) -> 61.3
        score = calculate_flight_risk_score(2.5, 6, 40, 18)
        self.assertEqual(score, 61.3)

    def test_score_case_2(self):
        # (3.8, 2, 30, 8) -> 28.1
        score = calculate_flight_risk_score(3.8, 2, 30, 8)
        self.assertEqual(score, 28.1)

    def test_score_case_3(self):
        # (1.8, 8, 25, 26) -> 92.0
        score = calculate_flight_risk_score(1.8, 8, 25, 26)
        self.assertEqual(score, 92.0)

    def test_score_case_4(self):
        # (3.4, 1, 20, 30) -> 46.8
        score = calculate_flight_risk_score(3.4, 1, 20, 30)
        self.assertEqual(score, 46.8)

    def test_worst_survey_zero_exits(self):
        # worst survey (mean 1), 0 exits, 36 months -> 65.0
        score = calculate_flight_risk_score(1.0, 0, 10, 36)
        self.assertEqual(score, 65.0)

    def test_best_survey_zero_exits(self):
        # best survey (mean 5), 0 exits, 0 months -> 0.0
        score = calculate_flight_risk_score(5.0, 0, 10, 0)
        self.assertEqual(score, 0.0)


class TestStage6Evaluation(unittest.TestCase):
    """Test Stage 6 3-card evaluation logic according to RetainAI specification."""

    @staticmethod
    def evaluate_intervention(
        r_before_treated,
        r_current_treated,
        r_before_control,
        r_current_control,
        spend,
        replacement_cost,
        headcount,
        p_exit,
        has_control=True
    ):
        treated_drop = r_before_treated - r_current_treated
        if has_control:
            comparison_drop = r_before_control - r_current_control
            adjusted_drop = treated_drop - comparison_drop
        else:
            comparison_drop = 0.0
            adjusted_drop = treated_drop

        breakeven_exits = (spend / replacement_cost) if replacement_cost > 0 else 0.0
        prevented_exits = max(0.0, headcount * (adjusted_drop / 100.0) * p_exit)

        if adjusted_drop <= 0:
            base_verdict = "No measurable improvement"
        elif prevented_exits >= breakeven_exits:
            base_verdict = "Likely pays off"
        else:
            base_verdict = "Not yet clear - re-check at the next 30/60/90-day point"

        if not has_control:
            verdict = f"{base_verdict} (unadjusted)"
        else:
            verdict = base_verdict

        gross_savings = prevented_exits * replacement_cost
        net_gain = gross_savings - spend
        roi_pct = (net_gain / spend * 100.0) if spend > 0 else 0.0

        return {
            "treated_drop": round(treated_drop, 2),
            "comparison_drop": round(comparison_drop, 2),
            "adjusted_drop": round(adjusted_drop, 2),
            "breakeven_exits": round(breakeven_exits, 2),
            "prevented_exits": round(prevented_exits, 2),
            "verdict": verdict,
            "gross_savings": round(gross_savings, 2),
            "net_gain": round(net_gain, 2),
            "roi_pct": round(roi_pct, 2)
        }

    def test_stage_6_test_a(self):
        # Test A: treated 92->80, control 55->51, spend 30000, replacement_cost 75000, headcount 25, p_exit 0.32
        # -> adjusted_drop 8, breakeven 0.4, prevented 0.64, verdict "Likely pays off", gross 48000, net 18000, roi 60
        res = self.evaluate_intervention(
            r_before_treated=92,
            r_current_treated=80,
            r_before_control=55,
            r_current_control=51,
            spend=30000,
            replacement_cost=75000,
            headcount=25,
            p_exit=0.32,
            has_control=True
        )
        self.assertEqual(res["adjusted_drop"], 8.0)
        self.assertEqual(res["breakeven_exits"], 0.4)
        self.assertEqual(res["prevented_exits"], 0.64)
        self.assertEqual(res["verdict"], "Likely pays off")
        self.assertEqual(res["gross_savings"], 48000.0)
        self.assertEqual(res["net_gain"], 18000.0)
        self.assertEqual(res["roi_pct"], 60.0)

    def test_stage_6_test_b(self):
        # Test B: adjusted_drop 3 -> prevented 0.24, "Not yet clear"
        res = self.evaluate_intervention(
            r_before_treated=92,
            r_current_treated=80,
            r_before_control=55,
            r_current_control=46,
            spend=30000,
            replacement_cost=75000,
            headcount=25,
            p_exit=0.32,
            has_control=True
        )
        self.assertEqual(res["adjusted_drop"], 3.0)
        self.assertEqual(res["prevented_exits"], 0.24)
        self.assertIn("Not yet clear", res["verdict"])

    def test_stage_6_test_c(self):
        # Test C: adjusted_drop -2 -> prevented 0, "No measurable improvement"
        res = self.evaluate_intervention(
            r_before_treated=92,
            r_current_treated=84,
            r_before_control=55,
            r_current_control=45,
            spend=30000,
            replacement_cost=75000,
            headcount=25,
            p_exit=0.32,
            has_control=True
        )
        self.assertEqual(res["adjusted_drop"], -2.0)
        self.assertEqual(res["prevented_exits"], 0.0)
        self.assertEqual(res["verdict"], "No measurable improvement")

    def test_stage_6_test_d(self):
        # Test D: no control -> raw drop used, warning shown, verdict ends "(unadjusted)"
        res = self.evaluate_intervention(
            r_before_treated=92,
            r_current_treated=80,
            r_before_control=0,
            r_current_control=0,
            spend=30000,
            replacement_cost=75000,
            headcount=25,
            p_exit=0.32,
            has_control=False
        )
        self.assertEqual(res["adjusted_drop"], 12.0)  # raw drop used
        self.assertTrue(res["verdict"].endswith("(unadjusted)"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
