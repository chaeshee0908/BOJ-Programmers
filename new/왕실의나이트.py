now = input()
y, x = ord(now[0]) - ord('a'), int(now[1]) - 1
count = 0

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, 1), (2, -1)]
for dx, dy in move:
    nx = x + dx
    ny = y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        count += 1
print(count)