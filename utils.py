import numpy as np

def get_probabilities(num_tags, decimal_places=2):
    """
    n개의 0~1 사이 랜덤 확률값을 numpy 배열로 반환하는 함수
    
    Args:
        num_tags (int): 생성할 확률값의 개수
        decimal_places (int): 소수점 자릿수 (기본값: 2)
    
    Returns:
        numpy.ndarray: num_tags개의 확률값이 담긴 배열
    """
    return np.round(np.random.random(num_tags), decimal_places)

def get_tags(tag_list, indices):
    """
    주어진 인덱스에 해당하는 태그 리스트를 반환하는 함수
    
    Args:
        tag_list (list): 전체 태그 리스트 (security, amenity, room_option 등)
        indices (list): 선택할 태그들의 인덱스 리스트
    
    Returns:
        list: 선택된 인덱스에 해당하는 태그들의 리스트
    
    Example:
        >>> tags = ['현관보안', '방범창', '카드키']
        >>> indices = [0, 2]
        >>> get_tags(tags, indices)
        ['현관보안', '카드키']
    """
    return [tag_list[i] for i in indices]





