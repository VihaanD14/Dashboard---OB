import pandas as pd
import json
import streamlit as st
import os

SETTINGS_FILE = "data/enterprise_settings.json"

def get_enterprise_settings():
    """Retrieve saved enterprise client settings with fallback defaults and session state overrides."""
    defaults = {
        "client_name": "Apex Global Technologies",
        "industry_vertical": "Enterprise Software & Cloud Services",
        "workforce_scale": "51-200",
        "exit_velocity_cap": 0.30,
        "weight_sentiment": 0.40,
        "weight_exit": 0.35,
        "weight_stagnation": 0.25,
        "risk_band_yellow": 40.0,
        "risk_band_red": 70.0,
        "stagnation_cap_months": 24.0,
        "salary_base": 25000.0,
        "salary_per_band": 25000.0,
        "replacement_multiplier_junior": 0.75,
        "replacement_multiplier_mid": 1.00,
        "replacement_multiplier_senior": 1.50,
        "calibration_note": "Defaults. Calibrate against the client's actual exits before relying on scores."
    }
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                saved = json.load(f)
                defaults.update(saved)
        except Exception:
            pass
            
    try:
        if hasattr(st, "session_state"):
            for k in defaults.keys():
                if k in st.session_state:
                    defaults[k] = st.session_state[k]
    except Exception:
        pass
    return defaults

def calculate_flight_risk_score(survey_mean, exits, headcount, months_since_promotion, settings=None):
    """
    Deterministic Composite Flight Risk Score (RetainAI Specification):
    - Sentiment Term: 1 - ((mean_score - 1) / 4.0) [survey scale 1-5; worst mean 1 gives full risk]
    - Exit Velocity: exits in trailing 12 months / active cohort headcount
    - Exit Term: min(1.0, exit_velocity / exit_velocity_cap) [default cap 0.30]
    - Stagnation Term: min(1.0, months_since_promotion / stagnation_cap_months) [default cap 24 mo]
    - R = 100 * (w_sentiment * sentiment_term + w_exit * exit_term + w_stagnation * stag_term)
    """
    if settings is None:
        try:
            settings = get_enterprise_settings()
        except Exception:
            settings = {}
            
    w_sent = float(settings.get("weight_sentiment", 0.40))
    w_exit = float(settings.get("weight_exit", 0.35))
    w_stag = float(settings.get("weight_stagnation", 0.25))
    vel_cap = float(settings.get("exit_velocity_cap", 0.30))
    stag_cap = float(settings.get("stagnation_cap_months", 24.0))
    
    sentiment_term = max(0.0, min(1.0, 1.0 - ((survey_mean - 1.0) / 4.0)))
    exit_velocity = (exits / headcount) if headcount > 0 else 0.0
    exit_term = min(1.0, max(0.0, exit_velocity / vel_cap if vel_cap > 0 else 0.0))
    stag_term = min(1.0, max(0.0, months_since_promotion / stag_cap if stag_cap > 0 else 0.0))
    
    raw_score = 100.0 * (w_sent * sentiment_term + w_exit * exit_term + w_stag * stag_term)
    return round(raw_score, 1)


def save_enterprise_settings(settings_dict):
    """Persist enterprise client settings to disk so they survive across sessions and tabs."""
    try:
        os.makedirs("data", exist_ok=True)
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings_dict, f, indent=2)
    except Exception:
        pass

@st.cache_data
def load_employees(scale=None):
    """Load employee dataset dynamically scaled according to workforce cohort setting."""
    if scale is None:
        scale = get_enterprise_settings().get("workforce_scale", "51-200")
    
    df_base = pd.read_csv("data/employees.csv")
    
    if scale == "1-50":
        # Small cohort (~45 total, 37 active, 8 exited)
        df = df_base.iloc[:45].copy().reset_index(drop=True)
        return df
    elif scale == "51-200":
        # Standard baseline (200 total, 163 active, 37 exited)
        return df_base.copy()
    elif scale == "201-500":
        # Mid-to-large cohort (~380 total, ~310 active, ~70 exited)
        extra_count = 180
        df_extra = df_base.sample(n=extra_count, replace=True, random_state=42).copy()
        df_extra['employee_id'] = [f"EMP{i:04d}" for i in range(201, 201 + extra_count)]
        df_extra['name'] = [f"Employee A{i:03d}" for i in range(201, 201 + extra_count)]
        df_combined = pd.concat([df_base, df_extra], ignore_index=True)
        return df_combined
    elif scale == "500+":
        # Enterprise scale (~850 total, ~692 active, ~158 exited)
        extra_count = 650
        df_extra = df_base.sample(n=extra_count, replace=True, random_state=42).copy()
        df_extra['employee_id'] = [f"EMP{i:04d}" for i in range(201, 201 + extra_count)]
        df_extra['name'] = [f"Employee A{i:03d}" for i in range(201, 201 + extra_count)]
        df_combined = pd.concat([df_base, df_extra], ignore_index=True)
        return df_combined
    return df_base.copy()

@st.cache_data
def load_exit_interviews(scale=None):
    """Load exit interview records filtered/scaled to match the active workforce cohort."""
    if scale is None:
        scale = get_enterprise_settings().get("workforce_scale", "51-200")
    
    df_emp = load_employees(scale=scale)
    exited_ids = set(df_emp[df_emp['status'] == 'Exited']['employee_id'])
    df_base_exits = pd.read_csv("data/exit_interviews.csv")
    
    if scale == "1-50":
        df = df_base_exits[df_base_exits['employee_id'].isin(exited_ids)].copy()
        if len(df) < 5:
            df = df_base_exits.iloc[:8].copy()
            df['employee_id'] = list(exited_ids)[:len(df)]
        return df.reset_index(drop=True)
    elif scale == "51-200":
        return df_base_exits.copy()
    else:
        needed_exits = len(exited_ids)
        if needed_exits > len(df_base_exits):
            extra_count = needed_exits - len(df_base_exits)
            df_extra = df_base_exits.sample(n=extra_count, replace=True, random_state=42).copy()
            new_ids = list(exited_ids - set(df_base_exits['employee_id']))[:extra_count]
            if len(new_ids) == extra_count:
                df_extra['employee_id'] = new_ids
            df_combined = pd.concat([df_base_exits, df_extra], ignore_index=True)
            return df_combined
        return df_base_exits.copy()

@st.cache_data
def load_survey_responses(scale=None):
    """Load pulse survey telemetry proportionally scaled to cohort size."""
    if scale is None:
        scale = get_enterprise_settings().get("workforce_scale", "51-200")
        
    df_surveys = pd.read_csv("data/survey_responses.csv")
    
    if scale == "1-50":
        df = df_surveys.copy()
        df['response_count'] = (df['response_count'] * 0.22).round().clip(lower=1).astype(int)
        df['total_eligible'] = (df['total_eligible'] * 0.22).round().clip(lower=2).astype(int)
        return df
    elif scale == "201-500":
        df = df_surveys.copy()
        df['response_count'] = (df['response_count'] * 1.9).round().astype(int)
        df['total_eligible'] = (df['total_eligible'] * 1.9).round().astype(int)
        return df
    elif scale == "500+":
        df = df_surveys.copy()
        df['response_count'] = (df['response_count'] * 4.25).round().astype(int)
        df['total_eligible'] = (df['total_eligible'] * 4.25).round().astype(int)
        return df
    return df_surveys.copy()

@st.cache_data
def load_policies():
    with open("data/company_policies.json", "r") as f:
        return json.load(f)

@st.cache_data
def get_department_stats():
    df = load_employees()
    total = len(df)
    active = len(df[df['status'] == 'Active'])
    exited = len(df[df['status'] == 'Exited'])
    attrition_rate = (exited / total) * 100 if total > 0 else 0
    return {
        "total": total,
        "active": active,
        "exited": exited,
        "attrition_rate": attrition_rate
    }

@st.cache_data
def get_exit_summary():
    df = load_exit_interviews()
    return df['stated_reason'].value_counts().to_dict()

@st.cache_data
def get_survey_trends():
    df = load_survey_responses()
    # Group by survey round and theme
    return df.groupby(['survey_round', 'question_theme'])['avg_score'].mean().reset_index()

@st.cache_data
def get_segment_metrics():
    df_emp = load_employees()
    df_exits = load_exit_interviews()
    df_survey = load_survey_responses()
    
    # We need DEPARTMENTS and ROLE_LEVELS, but to avoid circular import, we can get them from config or just unique values.
    # Let's get unique values directly from the employee dataframe
    departments = df_emp['department'].unique()
    role_levels = df_emp['role_level'].unique()
    
    segment_metrics = []
    dept_cohort_map = {}
    
    settings = get_enterprise_settings()
    w_sent = float(settings.get("weight_sentiment", 0.40))
    w_exit = float(settings.get("weight_exit", 0.35))
    w_stag = float(settings.get("weight_stagnation", 0.25))
    vel_cap = float(settings.get("exit_velocity_cap", 0.30))
    stag_cap = float(settings.get("stagnation_cap_months", 24.0))
    band_yellow = float(settings.get("risk_band_yellow", 40.0))
    band_red = float(settings.get("risk_band_red", 70.0))
    
    for d in departments:
        dept_cohort_map[d] = []
        survey_dept = df_survey[df_survey['department'] == d]
        dept_avg_survey = survey_dept['avg_score'].mean() if not survey_dept.empty else 3.0
        
        for rl in role_levels:
            active_emp = df_emp[(df_emp['department'] == d) & (df_emp['role_level'] == rl) & (df_emp['status'] == 'Active')]
            total_active = len(active_emp)
            
            # Trailing 12 months exits window: departures within trailing 12m for this cohort
            exits_emp = df_exits[(df_exits['department'] == d) & (df_exits['role_level'] == rl)]
            exits_count = len(exits_emp)
            exit_rate = exits_count / total_active if total_active > 0 else 0
            
            survey_seg = df_survey[(df_survey['department'] == d) & (df_survey['role_level'] == rl)]
            
            # k >= 5 rule strictly on survey RESPONSES (not nominal headcount)
            if not survey_seg.empty and 'response_count' in survey_seg.columns:
                responses_count = int(round(survey_seg['response_count'].mean()))
            else:
                responses_count = total_active
                
            # Privacy Protection: Automatic merge/rollup for cohorts under 5 responses
            if responses_count < 5:
                is_suppressed = True
                rolled_up_to_parent = True
                data_status = "Insufficient data (n < 5 responses)"
                avg_survey = dept_avg_survey
            else:
                is_suppressed = False
                rolled_up_to_parent = False
                avg_survey = survey_seg['avg_score'].mean() if not survey_seg.empty else dept_avg_survey
                data_status = "Sufficient (n >= 10)" if responses_count >= 10 else "Banded (5 <= n < 10)"
                
            # Prevent Leaver Inference: Borderline cohorts (5 <= n < 10) use qualitative banding
            is_banded = (5 <= responses_count < 10)
            
            mean_tenure = active_emp['tenure_years'].mean() if total_active > 0 else 0
            
            # Tenure Stagnation Index: min(1.0, Months Since Last Promotion / stagnation_cap_months)
            avg_promo_years = active_emp['last_promotion_years_ago'].mean() if total_active > 0 and 'last_promotion_years_ago' in active_emp.columns else 1.0
            months_since_promotion = avg_promo_years * 12.0
            tenure_stagnation = min(1.0, max(0.0, months_since_promotion / stag_cap if stag_cap > 0 else 0.0))
            
            # Survey Sentiment Inversion: 1 - ((Mean Score - 1) / 4.0)
            # Survey scale is 1-5, so worst mean (1) gives full risk (1.0)
            survey_inversion = max(0.0, min(1.0, 1.0 - ((avg_survey - 1.0) / 4.0)))
            
            # Exit Velocity: exits in trailing 12 months / active cohort headcount
            exit_velocity = exit_rate
            # Exit Term: min(1.0, exit_velocity / exit_velocity_cap)
            exit_term = min(1.0, max(0.0, exit_velocity / vel_cap if vel_cap > 0 else 0.0))
            
            # Deterministic Composite Flight Risk Score
            calc_score = round(100.0 * (w_sent * survey_inversion + w_exit * exit_term + w_stag * tenure_stagnation), 1)
            
            # Labels: Yellow = "Early warning (sentiment / stagnation)", Red = "Critical (adverse signals plus real departures)"
            # Note: With zero exits the maximum possible score is 65 (w_sent*1.0 + w_stag*1.0 = 65), so Red requires exits.
            if calc_score >= band_red:
                calc_level = "red"
            elif calc_score >= band_yellow:
                calc_level = "yellow"
            else:
                calc_level = "green"
                
            metric_entry = {
                "segment": f"{d} - {rl}",
                "department": d,
                "role_level": rl,
                "total_active": total_active,
                "response_count": responses_count,
                "is_suppressed": is_suppressed,
                "rolled_up_to_parent": rolled_up_to_parent,
                "is_banded": is_banded,
                "complementary_suppressed": False,
                "data_status": data_status,
                "exits_count": exits_count,
                "exit_rate": exit_rate,
                "exit_velocity": round(exit_velocity, 3),
                "exit_term": round(exit_term, 3),
                "exit_window": "trailing 12 months",
                "avg_survey_score": round(avg_survey, 2),
                "survey_inversion": round(survey_inversion, 3),
                "mean_tenure": round(mean_tenure, 2),
                "months_since_promotion": round(months_since_promotion, 1),
                "tenure_stagnation": round(tenure_stagnation, 3),
                "calculated_risk_score": calc_score,
                "risk_level": calc_level
            }
            segment_metrics.append(metric_entry)
            dept_cohort_map[d].append(metric_entry)
            
    # Complementary Suppression: Prevent algebraic subtraction leaks
    for d, cohorts in dept_cohort_map.items():
        suppressed_count = sum(1 for c in cohorts if c["is_suppressed"])
        if suppressed_count == 1:
            # Exactly one cohort is suppressed: an attacker could subtract visible cohorts from parent total.
            # Suppress the second-lowest cohort to break algebraic determinism.
            non_suppressed = [c for c in cohorts if not c["is_suppressed"]]
            if non_suppressed:
                second_lowest = min(non_suppressed, key=lambda x: x["response_count"])
                second_lowest["complementary_suppressed"] = True
                second_lowest["is_banded"] = True
                second_lowest["data_status"] = "Complementary Suppressed (Anti-Differencing)"
                
    return segment_metrics

@st.cache_data
def get_cached_risk_segments():
    from ai_engine.gemini_client import GeminiClient
    from ai_engine.risk_scorer import RiskScorer
    client = GeminiClient()
    scorer = RiskScorer(client)
    metrics = get_segment_metrics()
    return scorer.score_risk(metrics)

