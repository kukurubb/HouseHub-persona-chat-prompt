import numpy as np
from utils import get_probabilities, get_tags

class Amenity:
    def __init__(self):
        self.amenity_options = ['엘리베이터', '테라스', '무인택배함', '화재경보기', '베란다', '마당']
        self.amenity_importance = {
            "newlyweds": 0.4,           # 신혼부부는 편의시설 관심
            "dinks": 0.6,               # 맞벌이 부부는 편의시설 중시
            "college_student": 0.2,     # 비용 대비 기본적인 것만
            "solo_worker": 0.4,         # 실용적인 편의시설 선호
            "investor": 0.3,            # 임대가치 기준
            "retiree": 0.5,             # 편안한 생활 중시
            "young_family": 0.6,        # 가족 편의 매우 중시
            "high_earner": 0.6,         # 고급 편의시설 선호
            "corporate_buyer": 0.3,     # 실용성 위주
            "foreigner": 0.5,           # 편의시설 중시
            "relocator": 0.4,           # 새로운 환경 적응 고려
            "single_mom_or_dad": 0.5,   # 자녀 편의 중시
            "digital_nomad": 0.3,       # 기본적인 편의시설 중시
            "military_family": 0.4,     # 기본 편의사항 고려
            "job_seeker": 0.2,          # 비용 대비 기본적인 것만
            "startup_founder": 0.5,     # 업무환경 고려
            "creative_worker": 0.4,     # 작업 환경 고려
            "weekend_commuter_dad": 0.4 # 기본적인 편의사항 중시
        }

    def get_tag_indices(self, role):
        threshold = self.amenity_importance[role]
        num_tags = len(self.amenity_options)

        probabilities = get_probabilities(num_tags)
        true_indices = np.where(probabilities > threshold)[0]

        return true_indices

    def get_amenity_tags(self, role):
        indices = self.get_tag_indices(role)
        tags = get_tags(self.amenity_options, indices)

        return tags