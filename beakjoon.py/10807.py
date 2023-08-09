# 목적: 주어진 숫자만큼의 숫자 리스트를 만들고 그 중 특정 숫자의 갯수를 찾기 위함

N = int(input()) # 변수를 입력받는다, N은 lst의 크기를 의미한다
lst = input().split()

print(lst.count(input())) # 입력받은 문자의 수를 센다, 이를 출력한다