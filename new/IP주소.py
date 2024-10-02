import sys
input = sys.stdin.readline

N = int(input())
ip = []

def printIP(ip):
    a = int(ip[:8], 2)
    b = int(ip[8:16], 2)
    c = int(ip[16:24], 2)
    d = int(ip[24:32], 2)
    print(format(a) + '.' + format(b) + '.' + format(c) + '.' + format(d))

for _ in range(N):
    ip_address = input()
    first, second, third, host = tuple(map(int, ip_address.split('.')))
    now_ip = format(first,'08b') + format(second, '08b') + format(third, '08b') + format(host, '08b')
    ip.append(now_ip)

ip_address = list(map(int, ip_address.split('.')))

mask = ''
for j in range(32):
    first = int(ip[0][j])
    line = [ip[i][j] for i in range(N)]
    if all(int(x) ^ first == 0 for x in line):
        mask += '1'
    else:
        mask += '0' * (32-j)
        break

result_mask = int(mask, 2)
ip_total = (ip_address[0] << 24) + (ip_address[1] << 16) + (ip_address[2] << 8) + ip_address[3]
result_ip = result_mask & ip_total

printIP(bin(result_ip)[2:].zfill(32))
printIP(mask)
