from utils import get_probabilities, get_tags
import numpy as np


class Security:
    def __init__(self):
        self.security_options = ['현관보안', '방범창', '카드키', '인터폰', '경비원', '사설경비', '비디오폰', 'CCTV']
        self.security_importance = {
            "newlyweds": 0.4,           # 신혼부부는 보안에 민감
            "dinks": 0.5,               # 맞벌이 부부는 보안 중시
            "college_student": 0.1,     # 비용 대비 낮은 중요도
            "solo_worker": 0.3,         # 보통 수준의 보안 선호
            "investor": 0.2,            # 투자용이라 평균적 수준
            "retiree": 0.4,             # 안전 중시
            "young_family": 0.6,        # 자녀가 있어 매우 중시
            "high_earner": 0.6,         # 프리미엄 보안 선호
            "corporate_buyer": 0.3,     # 기본 수준 이상
            "foreigner": 0.4,           # 낯선 환경이라 보안 중시
            "relocator": 0.4,           # 새로운 환경이라 보안 중시
            "single_mom_or_dad": 0.6,   # 자녀 안전 매우 중시
            "digital_nomad": 0.2,       # 평균적 수준
            "military_family": 0.3,     # 기본 수준 이상
            "job_seeker": 0.1,          # 비용 대비 낮은 중요도
            "startup_founder": 0.4,     # 사무공간 겸용이라 중요
            "creative_worker": 0.3,     # 작업물 보안도 고려
            "weekend_commuter_dad": 0.4 # 집을 비우는 시간이 많아 중요
        }
    
    def get_tag_indices(self, role):
        threshold = self.security_importance[role]
        num_tags = len(self.security_options)

        probabilities = get_probabilities(num_tags)
        true_indices = np.where(probabilities > threshold)[0]

        return true_indices

    def get_security_tags(self, role):
        indices = self.get_tag_indices(role)
        tags = get_tags(self.security_options, indices)

        return tags