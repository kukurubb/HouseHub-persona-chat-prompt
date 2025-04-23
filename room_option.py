from utils import get_probabilities, get_tags
import numpy as np

class RoomOption:
    def __init__(self):
        self.room_options = ['싱크대', '샤워부스', '욕조', '비데', '냉장고', 'TV', '책상', '인덕션레인지', 
                            '옷장', '침대', '소파', '식탁', '식기세척기', '붙박이장', '전자레인지', 
                            '가스오븐', '세탁기', '가스레인지', '신발장', '건조기']
        self.room_importance = {
            "newlyweds": 0.5,           # 신혼집 살림 중시
            "dinks": 0.6,               # 편리한 살림 중시
            "college_student": 0.2,     # 기본적인 옵션만
            "solo_worker": 0.4,         # 실용적인 옵션 선호
            "investor": 0.3,            # 임대가치 기준
            "retiree": 0.4,             # 편한 생활 중시
            "young_family": 0.6,        # 가족 생활 중시
            "high_earner": 0.7,         # 풀옵션 선호
            "corporate_buyer": 0.4,     # 기본 옵션 위주
            "foreigner": 0.5,           # 풀옵션 선호
            "relocator": 0.5,           # 기본 살림 중시
            "single_mom_or_dad": 0.6,   # 편리한 살림 중시
            "digital_nomad": 0.3,       # 기본적인 것만
            "military_family": 0.5,     # 이사 고려한 옵션
            "job_seeker": 0.2,          # 최소한의 옵션
            "startup_founder": 0.4,     # 재택근무 고려
            "creative_worker": 0.5,     # 작업 환경 고려
            "weekend_commuter_dad": 0.4 # 기본 옵션 위주
        }

    def get_tag_indices(self, role):
        threshold = self.room_importance[role]
        num_tags = len(self.room_options)

        probabilities = get_probabilities(num_tags)
        true_indices = np.where(probabilities > threshold)[0]

        return true_indices
    
    def get_room_option_tags(self, role):
        indices = self.get_tag_indices(role)
        tags = get_tags(self.room_options, indices)
        return tags