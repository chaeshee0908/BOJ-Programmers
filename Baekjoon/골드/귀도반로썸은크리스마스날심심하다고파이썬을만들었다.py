# 골드5 6568번
# https://www.acmicpc.net/problem/6568

adder = 0
pc = 0
memory = []
for _ in range(32):
    memory.append(int(input(), 2))


while True:
    now = memory[pc]
    command = now // 32
    operand = now % 32
    pc = (pc + 1) % 32

    # 메모리 주소 x에 가산기의 값을 저장한다. 
    if command == 0:
        memory[operand] = adder
    # 메모리 주소 x의 값을 가산기로 불러온다. 
    elif command == 1:
        adder = memory[operand]
    # 가산기의 값이 0이면 PC값을 x로 바꾼다.
    elif command == 2:
        if adder == 0:
            pc = operand
    # 아무 연산도 하지 않는다. 
    elif command == 3:
        pass
    # 가산기 값을 1 감소시킨다. 
    elif command == 4:
        adder = (adder + 255) % 256
    # 가산기 값을 1 증가시킨다.
    elif command == 5:
        adder = (adder + 1) % 256
    # PC 값을 x로 바꾼다. 
    elif command == 6:
        pc = operand
    # 프로그램을 종료한다. 
    elif command == 7:
        break

print(bin(adder % 256)[2:])