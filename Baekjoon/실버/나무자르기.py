# 2805번 (실버3)
# 이분 탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(trees)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in trees:
        # 잘랐을 때의 나무 길이 계산
        if x > mid:
            total += x - mid
    # 나무 길이가 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 나무 길이가 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid    # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록
        start = mid + 1

print(result)