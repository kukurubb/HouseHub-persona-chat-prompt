import numpy as np

class Role:
    def __init__(self):
        self.role_name = {
            "newlyweds": "신혼부부",
            "dinks": "딩크족",
            "college_student": "대학생",
            "solo_worker": "사회초년생",
            "investor": "투자자",
            "retiree": "은퇴자",
            "young_family": "젊은 부부",
            "high_earner": "전문직",
            "corporate_buyer": "법인 구매자",
            "foreigner": "외국인",
            "relocator": "이주민",
            "single_mom_or_dad": "싱글맘",
            "digital_nomad": "디지털 노마드",
            "military_family": "군인가족",
            "job_seeker": "취준생",
            "startup_founder": "스타트업 창업자",
            "creative_worker": "프리랜서",
            "weekend_commuter_dad": "기러기 아빠"
        }

    def get_role_name(self, role):
        return self.role_name[role]
    
    def get_role_key(self):
        return np.random.choice(list(self.role_name.keys()))