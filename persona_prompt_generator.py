from role import Role
from tone import Tone
from property import Property
from transaction_type import TransactionType
from budget import Budget
from security import Security
from amenity import Amenity
from room_option import RoomOption

"""
1. 생성 프롬프트 종류
    - single turn conversation(문의글, 문의 폼)
    - multi turn conversation(채팅, 전화)
2. 기능 상세
    - 1차 필터와 태그 검색 두가지로 나누어 검색이 가능한 형태로 작성할 것
    - 1차 필터에 들어갈 내용에 태그도 일부 포함할 것
3. 모델 입력 시 배치로 묶는 기능 추가
"""
class PersonaPromptGenerator:
    def __init__(self):
        self.role = Role()
        self.tone = Tone()
        self.property = Property()
        self.transaction_type = TransactionType()
        self.budget = Budget()
        self.security = Security()
        self.amenity = Amenity()
        self.room_option = RoomOption()

    def generate_single_turn_conversation_prompt(self, role):
        role_name = self.role.get_role_name(role)
        tone = self.tone.get_tone(role)
        property_type = self.property.get_property_type(role)
        transaction_type = self.transaction_type.get_transaction_type()
        budget = self.budget.get_budget(transaction_type, property_type)
        security_tags = self.security.get_security_tags(role)
        amenity_tags = self.amenity.get_amenity_tags(role)
        room_option_tags = self.room_option.get_room_option_tags(role)

        prompt = f"""
            [task]
            single turn conversation generation

            [situation]
            공인중개사에게 부동산 문의를 하는 고객의 질문

            [rule]
            1. 문장은 한국어로 작성하며, 문장 길이는 100자에서 200자 사이로 제한할 것
            2. [options]에 해당하는 요소들을 전부 포함하여 문장을 생성할 것
            3. 사용자 역할에 맞는 말투와 표현 방식을 사용할 것
            4. 고객의 요청은 실제로 문의하는 듯한 자연스러운 표현으로 구성할 것
            5. 반복되는 표현은 피하고, 다양한 어휘를 사용할 것
            6. 명시적으로 언급되지 않더라도 직업 기반으로 일반적으로 요구될 수 있는 요소는 자연스럽게 포함 가능

            [options]
            role : {role_name}

            tone : {tone}

            property_type : {property_type}

            transaction_type : {transaction_type}

            budget : {budget}

            amenity : {amenity_tags}

            room_option : {room_option_tags}

            security : {security_tags}

            [example1]
            안녕하세요. 결혼을 앞두고 함께 살 첫 신혼집을 찾고 있는 예비부부입니다.
            신축 아파트 위주로 보고 있고, 앞으로 자녀도 계획하고 있어서 최소 2.5룸 이상의 공간이면 좋겠습니다.
            조용하고 깨끗한 동네였으면 좋겠고, 단지 내에 CCTV가 설치되어 있거나 상주 경비원이 있는 등 보안 시설이 잘 갖춰진 곳을 우선적으로 고려하고 있어요.
            예산은 전세 기준으로 3억 2천만원에서 4억 1천만원 정도 생각하고 있고, 교통이나 생활 인프라도 어느 정도 갖춰져 있으면 더할 나위 없이 좋을 것 같아요.

            [example2]
            안녕하세요. 현재 취업 준비 중이라 교통 편리한 지역의 저렴한 월세 빌라 원룸을 찾고 있습니다.
            보증금은 550만원에서 770만원, 월세는 36만원에서 43만원 정도로 생각 중입니다.
            싱크대, 침대, 책상, 냉장고, 전자레인지 등 기본 옵션은 꼭 있었으면 해요.
            현관보안, CCTV, 카드키 같은 보안도 중요하고, 엘리베이터나 무인택배함, 베란다, 마당 같은 생활 편의 시설도 잘 갖춰진 곳이면 좋겠습니다.
        """

        return prompt

    def generate_multi_turn_conversation_prompt(self, role):
        role_name = self.role.get_role_name(role)
        tone = self.tone.get_tone(role)
        property_type = self.property.get_property_type(role)
        transaction_type = self.transaction_type.get_transaction_type()
        budget = self.budget.get_budget(transaction_type, property_type)
        security_tags = self.security.get_security_tags(role)
        amenity_tags = self.amenity.get_amenity_tags(role)
        room_option_tags = self.room_option.get_room_option_tags(role)

        prompt = f"""
            [task]
            multi turn conversation generation

            [situation]
            부동산 문의를 위한 공인중개사와 고객의 대화

            [rule]
            1. 문장은 한국어로 작성하며, 대화의 턴 수는 10회에서 20회 사이로 제한할 것
            2. 한 턴의 문장의 길이는 80자 이하로 제한할 것
            3. [options]에 해당하는 요소들이 추출해야하는 정보이며 [options]에 해당하는 요소들을 전부 포함하여 문장을 생성할 것
            4. 고객은 역할에 따라 부동산 관련 지식이 적을 수도 있고, 많을 수도 있음. 부동산 지식이 적은 고객은 원하는 바를 명쾌하게 설명할 수 없음
            5. 공인중개사는 추출해야하는 정보를 고객으로부터 얻을 수 있도록 시도할 것. 필요에 따라서 고객에게 추가적인 질문을 할 것
            6. 사용자 역할에 맞는 말투와 표현 방식을 사용할 것
            7. 고객의 요청은 실제로 문의하는 듯한 자연스러운 표현으로 구성할 것
            8. 공인중개사는 고객의 요청을 정확하게 이해하고, 고객의 요청을 충족시키기 위한 정보를 제공할 것
            9. 반복되는 표현은 피하고, 다양한 어휘를 사용할 것
            10. 명시적으로 언급되지 않더라도 직업 기반으로 일반적으로 요구될 수 있는 요소는 자연스럽게 포함 가능

            [options]
            role : {role_name}

            tone : {tone}

            property_type : {property_type}

            transaction_type : {transaction_type}

            budget : {budget}

            amenity : {amenity_tags}

            room_option : {room_option_tags}

            security : {security_tags}
        """

        return prompt

    
if __name__ == "__main__":
    role = Role()
    random_role = role.get_role_key()
    persona = PersonaPromptGenerator()
    prompt = persona.generate_single_turn_conversation_prompt(random_role)
    print(prompt)

    # prompt = persona.generate_multi_turn_conversation_prompt(random_role)
    # print(prompt)