# 목적: 각 바구니에 숫자가 적힌 공을 넣고, 빼기를 반복한다. 동작이 끝난 후에 바구니 안의 공의 숫자를 확인하기 위함이다.

n, m = map(int, input().split())
baskets = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        baskets[idx] = k

for i in range(n):
    print(baskets[i], end = " ")