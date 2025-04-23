"""
1. 생성 프롬프트 종류
    - single turn conversation(문의글, 문의 폼)
    - multi turn conversation(채팅, 전화)
2. 기능 상세
    - 1차 필터와 태그 검색 두가지로 나누어 검색이 가능한 형태로 작성할 것
    - 1차 필터에 들어갈 내용에 태그도 일부 포함할 것
3. 모델 입력 시 배치로 묶는 기능 추가
"""
class SlotFiller:
    def __init__(self):
        pass

    def generate_single_turn_slot_filling_prompt(self, input_sentence):
        prompt = f"""
            [task]
            single turn slot filling
            
            [situation]
            고객의 문의에서 부동산 관련 키워드를 추출

            [rule]
            1. 출력은 dictionary 형태로 할 것
            2. 출력 변수명은 [options]의 요소들로 작성할 것
            3. options의 budget 출력 형태는 # 주석 표시에 맞게 변경할 것

            [options]
            role : []
            tone : []
            property_type : []
            transaction_type : []
            budget : [
                # property_type이 매매인 경우
                min_sale_price : min_value
                max_sale_price : max_value
                unit : unit

                # property_type이 전세인 경우
                min_deposit : min_value
                max_deposit : max_value
                unit : unit

                # property_type이 월세인 경우
                min_deposit : min_value
                max_deposit : max_value
                min_rent_fee : min_value
                max_rent_fee : max_value
                unit : unit
            ]
            amenity : []
            room_option : []
            security : []

            [input_example1]
            안녕하세요. 업무 특성상 조용하고 품격 있는 공간을 찾고 있어 전원주택 월세 매물을 알아보고 있습니다.
            브랜드 신뢰도와 입지가 중요하며, 보증금은 4,120만 원에서 4,800만 원, 월세는 240만 원에서 255만 원 사이로 고려 중입니다.
            마당이 잘 갖춰져 있고, 샤워부스, 책상, 소파, 가스레인지, 건조기 등 생활 옵션이 충실하며, 현관보안과 카드키, 인터폰 같은 기본 보안도 철저한 곳이면 좋겠습니다.

            [output_example1]
            {{
                "role": "전문직",
                "tone": "위치와 브랜드를 중요시하는 말투",
                "property_type": "전원주택",
                "transaction_type": "월세",
                "budget": {{
                    "min_deposit": 4120,
                    "max_deposit": 4800,
                    "min_rent_fee": 240,
                    "max_rent_fee": 255,
                    "unit": "만원"
                }},
                "amenity": [
                    "마당"
                ],
                "room_option": [
                    "샤워부스",
                    "책상",
                    "소파",
                    "가스레인지",
                    "건조기"
                ],
                "security": [
                    "현관보안",
                    "카드키",
                    "인터폰"
                ]
            }}

            [input_sentence]
            {input_sentence}
        """

        return prompt

    def generate_multi_turn_slot_filling_prompt(self, input_conversation):
        prompt = f"""
            [task]
            multi turn slot filling
            
            [situation]
            고객과 공인중개사의 대화에서 부동산 관련 키워드를 추출

            [rule]
            1. 출력은 dictionary 형태로 할 것
            2. 출력 변수명은 [options]의 요소들로 작성할 것
            3. options의 budget 출력 형태는 # 주석 표시에 맞게 변경할 것

            [options]
            role : []
            tone : []
            property_type : []
            transaction_type : []
            budget : [
                # property_type이 매매인 경우
                min_sale_price : min_value
                max_sale_price : max_value
                unit : unit

                # property_type이 전세인 경우
                min_deposit : min_value
                max_deposit : max_value
                unit : unit

                # property_type이 월세인 경우
                min_deposit : min_value
                max_deposit : max_value
                min_rent_fee : min_value
                max_rent_fee : max_value
                unit : unit
            ]
            amenity : []
            room_option : []
            security : []

            [input_conversation]
            {input_conversation}
        """

        return prompt
    
if __name__ == "__main__":
    slot_filler = SlotFiller()

    input_sentence = """
            안녕하세요. 아이와 함께 지낼 안전하고 실용적인 연립주택을 전세로 찾고 있어요.
            예산은 2억 9,100만 원에서 4억 3,700만 원 사이로 생각 중이고, 테라스나 베란다처럼 환기 잘 되는 공간이 있으면 좋겠어요.
            싱크대, 책상, 인덕션레인지, 세탁기 같은 기본 옵션이 잘 갖춰져 있고, 비디오폰처럼 아이 혼자 있을 때도 안심할 수 있는 보안 시설이 있었으면 해요.
    """
    prompt = slot_filler.generate_single_turn_slot_filling_prompt(input_sentence)
    print(prompt)

    input_conversation = """
            1. 고객:
            안녕하세요. 저희 부부가 아이 키우기 좋은 아파트를 월세로 알아보려 해요.

            2. 공인중개사:
            반갑습니다. 혹시 보증금과 월세는 어느 정도로 생각하고 계실까요?

            3. 고객:
            보증금은 2,460만 원에서 2,720만 원, 월세는 51~60만 원 정도요.

            4. 공인중개사:
            감사합니다. 학군이나 육아 환경도 중요하게 보고 계신가요?

            5. 고객:
            네, 유치원 근처면 좋겠고, 가까이에 공원이 있으면 더 좋아요.

            6. 공인중개사:
            생활 편의시설로는 어떤 것들이 있으면 좋으실까요?

            7. 고객:
            무인택배함이나 베란다, 테라스 같은 공간이 있으면 정말 좋을 것 같아요.

            8. 공인중개사:
            화재경보기 같은 기본 안전 설비도 포함되면 괜찮으신가요?

            9. 고객:
            네, 그런 건 기본이었으면 좋겠어요. 안전은 항상 중요하니까요.

            10. 공인중개사:
            내부 옵션은 어떤 부분을 중점적으로 보고 계세요?

            11. 고객:
            샤워부스, 욕조, 비데는 꼭 있었으면 하고, 냉장고도 포함됐으면 해요.

            12. 공인중개사:
            주방 옵션으로 인덕션레인지, 가스오븐, 가스레인지는 어떠세요?

            13. 고객:
            좋아요. 식탁이랑 소파, 건조기도 포함되면 너무 좋겠네요.

            14. 공인중개사:
            보안은 어떤 수준을 원하시나요? 예: 현관보안, 카드키, CCTV 등

            15. 고객:
            CCTV랑 카드키, 인터폰 같은 건 꼭 있었으면 좋겠어요. 현관보안도요.

            16. 공인중개사:
            좋습니다. 조건에 맞는 아파트 매물 확인해서 곧 연락드릴게요!
    """
    prompt = slot_filler.generate_multi_turn_slot_filling_prompt(input_conversation)
    print(prompt)