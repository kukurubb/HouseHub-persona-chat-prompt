class Tone:
    def __init__(self):
        self.tone = {
            "newlyweds": "첫 집을 신중하게 알아보는 듯한 말투",
            "dinks": "프라이버시 좋고 세련된 구조에 관심",
            "college_student": "월세 예산 안에서 가성비 좋은 곳을 찾는 느낌",
            "solo_worker": "출퇴근 거리, 주변 편의시설에 민감",
            "investor": "수익률, 입지, 시세 상승 여력이 중요한 요소",
            "retiree": "안정적이고 조용한 주거 환경을 찾는 느낌",
            "young_family": "학군, 공원, 육아 환경 고려",
            "high_earner": "위치와 브랜드를 중요시하는 고급 수요",
            "corporate_buyer": "수익 구조와 절세 전략 중심",
            "foreigner": "계약 조건과 생활환경에 대한 세부 정보 요청",
            "relocator": "입지 적응과 초기 생활 안정성 고려",
            "single_mom_or_dad": "안전한 동네와 실용적인 구조 중시",
            "digital_nomad": "가볍게 머물 수 있고 교통 좋은 매물",
            "military_family": "이사 편의성과 전세 기간이 유리한 조건 선호",
            "job_seeker": "가격 민감하고 교통 좋은 원룸 선호",
            "startup_founder": "사무/주거 겸용이 가능한 구조, 유연한 조건 선호",
            "creative_worker": "조용하고 창의적인 작업이 가능한 공간 선호",
            "weekend_commuter_dad": "교통 접근성, 특히 기차역이나 터미널 접근성을 중시하는 말투"
        }

    def get_tone(self, role):
        return self.tone[role]