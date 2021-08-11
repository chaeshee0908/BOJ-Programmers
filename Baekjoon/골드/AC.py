# 5430번 (골드5)
# 구현, 자료구조, 문자열, 파싱, 덱
# 시간초과 유의(reverse는 홀수 개 있을 때만 실행)

from collections import deque
import sys

def execution(queue, orders, n):
    global result
    rev = 0
    for order in orders:
        if order == 'R':
            rev += 1
        elif order == 'D':
            # 큐가 비었으면(입력받을 때부터) 삭제 불가 => 에러
            if n == 0:
                print('error')
                return 
            if len(queue) > 0:
                # 짝수번 뒤집으면 원본과 같음
                if rev % 2 == 0:
                    queue.popleft()
                # 홀수번 뒤집으면 뒤에서 삭제되는 걸로 생각
                else:
                    queue.pop()
            # 큐가 비었으면(삭제로 인해서) 삭제 불가 => 에러        
            else:
                print('error')
                return
    if rev % 2 != 0:
        queue.reverse()
    print('['+','.join(queue)+']')
    

t = int(input())
for _ in range(t):
    orders = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    string = sys.stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(string)
    execution(queue,orders,n)