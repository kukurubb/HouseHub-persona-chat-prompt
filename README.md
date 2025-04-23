# 부동산 AI 대화 시스템

이 프로젝트는 부동산 거래를 위한 AI 기반 대화 시스템을 구현한 것입니다. 다양한 페르소나(고객 유형)에 맞춰 개인화된 부동산 추천과 대화를 제공합니다.

## 주요 기능

- persona_prompt_generator.py: 페르소나 기반 대화 생성 프롬프트
- slot_filling.py: 고객 키워드 추출 프롬프트

## 프로젝트 구조
"""
├── amenity.py           # 편의시설 관련 기능
├── budget.py           # 예산 계산 및 관리
├── persona_prompt_generator.py  # 페르소나 기반 대화 생성
├── property.py         # 부동산 특성 관리
├── role.py            # 페르소나 역할 정의
├── room_option.py     # 방 옵션 관리
├── security.py        # 보안 관련 기능
├── slot_filling.py    # 슬롯 필링 기능
├── tone.py           # 대화 톤 관리
├── transaction_type.py # 거래 유형 관리
└── utils.py          # 유틸리티 함수
"""