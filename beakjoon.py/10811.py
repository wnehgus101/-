#목적: 바구니의 공을 역순으로 바꾸기

n, m = map(int, input().split())

my_list = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    count = 0
    for k in range(i, j):
        for l in range(i, j - count):
            temp = my_list[l - 1]
            my_list[l - 1] = my_list[l]
            my_list[l] = temp
        count += 1
        
for i in range(n):
    print(my_list[i], end = " ")