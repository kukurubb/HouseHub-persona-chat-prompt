import numpy as np

class Budget:
    def __init__(self):
        # 매물 등급 정의 (A, B, C)
        self.property_grades = ['A', 'B', 'C']
        
        # 매물 유형별 기본 가격 범위 (단위: 만원)
        self.property_price_ranges = {
            "아파트": {
                "A": {"매매": (150000, 300000), "전세": (70000, 120000), "월세": (5000, 10000, 150, 300)},   # 프리미엄/신축
                "B": {"매매": (80000, 150000), "전세": (40000, 70000), "월세": (3000, 5000, 100, 150)},     # 중급
                "C": {"매매": (40000, 80000), "전세": (20000, 40000), "월세": (1000, 3000, 50, 100)}        # 일반
            },
            "오피스텔": {
                "A": {"매매": (70000, 120000), "전세": (40000, 60000), "월세": (3000, 5000, 100, 200)},
                "B": {"매매": (40000, 70000), "전세": (25000, 40000), "월세": (2000, 3000, 70, 100)},
                "C": {"매매": (20000, 40000), "전세": (15000, 25000), "월세": (1000, 2000, 50, 70)}
            },
            "빌라": {
                "A": {"매매": (40000, 70000), "전세": (25000, 40000), "월세": (2000, 3000, 80, 150)},
                "B": {"매매": (25000, 40000), "전세": (15000, 25000), "월세": (1000, 2000, 50, 80)},
                "C": {"매매": (15000, 25000), "전세": (8000, 15000), "월세": (500, 1000, 30, 50)}
            },
            "원룸": {
                "A": {"매매": (25000, 35000), "전세": (15000, 25000), "월세": (1000, 2000, 70, 100)},
                "B": {"매매": (15000, 25000), "전세": (8000, 15000), "월세": (500, 1000, 50, 70)},
                "C": {"매매": (8000, 15000), "전세": (5000, 8000), "월세": (300, 500, 30, 50)}
            },
            "단독/다가구주택": {
                "A": {"매매": (80000, 150000), "전세": (50000, 80000), "월세": (3000, 5000, 150, 250)},
                "B": {"매매": (50000, 80000), "전세": (30000, 50000), "월세": (2000, 3000, 100, 150)},
                "C": {"매매": (30000, 50000), "전세": (15000, 30000), "월세": (1000, 2000, 70, 100)}
            },
            "상가주택": {
                "A": {"매매": (70000, 120000), "전세": (40000, 70000), "월세": (3000, 5000, 200, 300)},
                "B": {"매매": (40000, 70000), "전세": (25000, 40000), "월세": (2000, 3000, 150, 200)},
                "C": {"매매": (25000, 40000), "전세": (15000, 25000), "월세": (1000, 2000, 100, 150)}
            },
            "다세대주택": {
                "A": {"매매": (50000, 80000), "전세": (30000, 50000), "월세": (2000, 3000, 100, 150)},
                "B": {"매매": (30000, 50000), "전세": (20000, 30000), "월세": (1000, 2000, 70, 100)},
                "C": {"매매": (20000, 30000), "전세": (10000, 20000), "월세": (500, 1000, 50, 70)}
            },
            "연립주택": {
                "A": {"매매": (45000, 75000), "전세": (25000, 45000), "월세": (2000, 3000, 100, 150)},
                "B": {"매매": (30000, 45000), "전세": (15000, 25000), "월세": (1000, 2000, 70, 100)},
                "C": {"매매": (20000, 30000), "전세": (10000, 15000), "월세": (500, 1000, 50, 70)}
            },
            "전원주택": {
                "A": {"매매": (100000, 200000), "전세": (50000, 80000), "월세": (3000, 5000, 200, 300)},
                "B": {"매매": (60000, 100000), "전세": (30000, 50000), "월세": (2000, 3000, 150, 200)},
                "C": {"매매": (40000, 60000), "전세": (20000, 30000), "월세": (1000, 2000, 100, 150)}
            }
        }

    def get_budget(self, transaction_type, property_type):
        grade = np.random.choice(self.property_grades)
        price_range = self.property_price_ranges[property_type][grade][transaction_type]

        if transaction_type == "매매":
            trigger = True
            while trigger:
                price1 = self.get_random_price(price_range, 2)
                price2 = self.get_random_price(price_range, 2)

                if price1 != price2:
                    trigger = False

            min_price = min(price1, price2)
            max_price = max(price1, price2)

            return f"매매가 {min_price}만원 이상 {max_price}만원 이하"
        
        elif transaction_type == "전세":
            trigger = True
            while trigger:
                price1 = self.get_random_price(price_range, 2)
                price2 = self.get_random_price(price_range, 2)

                if price1 != price2:
                    trigger = False

            min_price = min(price1, price2)
            max_price = max(price1, price2)

            return f"전세가 {min_price}만원 이상 {max_price}만원 이하"
        
        elif transaction_type == "월세":
            trigger = True
            while trigger:
                deposit1 = self.get_random_price(price_range[:2], 1)
                deposit2 = self.get_random_price(price_range[:2], 1)

                rent_fee1 = self.get_random_price(price_range[2:], 0)
                rent_fee2 = self.get_random_price(price_range[2:], 0)

                if (deposit1 != deposit2) and (rent_fee1 != rent_fee2):
                    trigger = False

            min_deposit = min(deposit1, deposit2)
            max_deposit = max(deposit1, deposit2)

            min_rent_fee = min(rent_fee1, rent_fee2)
            max_rent_fee = max(rent_fee1, rent_fee2)

            return f"보증금 {min_deposit}만원 이상 {max_deposit}만원 이하, 월세 {min_rent_fee}만원 이상 {max_rent_fee}만원 이하"

    def get_random_price(self, price_range, round_digit):
        """
        주어진 가격 범위 내에서 랜덤 가격을 생성하는 함수
        
        Args:
            price_range: tuple (최소가격, 최대가격)
            round_digit: int 
                반올림할 자릿수
                2: 100단위 반올림 (예: 45300)
                1: 10단위 반올림 (예: 45340)
                0: 1단위 반올림 (예: 45342)
        
        Returns:
            int: 지정된 자릿수로 반올림된 랜덤 가격
        """
        min_price, max_price = price_range
        # 랜덤 값 생성
        random_price = np.random.uniform(min_price, max_price)
        
        # 반올림 자릿수에 따른 나누는 수 계산
        # round_digit=2 이면 100으로 나눔
        # round_digit=1 이면 10으로 나눔
        # round_digit=0 이면 1로 나눔
        divisor = 10 ** round_digit
        
        # 지정된 자릿수로 반올림
        rounded_price = round(random_price / divisor) * divisor
        return int(rounded_price)
    
