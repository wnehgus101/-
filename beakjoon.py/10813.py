#목적: N번의 번호가 매겨져 있는 N개의 바구니가 있다. 각 바구니에는 N의 번호가 적힌 공이 한개 들어있다. M번 바구니의 공을 바꾸었을때 바구니에 들어있는 공을 알기 위함이다.

#n은 배열의 개수를 의미하고, m은 배열내의 원소를 바꿀 횟수를 의미한다.
n, m = map(int, input().split())

#배얄을 생성한다. 이때 범위는 1 ~ n+1까지 이다.
my_list = list(range(1, n + 1))

#m번 만큼 배열내의 원소를 교체한다.
for _ in range(m):
    i, j = map(int, input().split())
    temp = my_list[i - 1]
    my_list[i - 1] = my_list[j - 1]
    my_list[j - 1] = temp

#배열의 각 원소를 공백으로 구별하며 출력한다. 
for i in range(n):
    print(my_list[i], end = " ")