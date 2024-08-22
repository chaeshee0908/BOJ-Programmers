def solution(x, y, z):
    diff = abs(x - y)
    # z번의 이동을 모두 수행해도 y번째 상자에 도착 못할 경우
    if z < diff:
        return -1
    max_value = max(x, y)
    # 우측으로 다녀올 수 있는 거리
    plus_value = (z - diff) // 2
    return max_value + plus_value