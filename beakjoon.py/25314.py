# 목적: 주어진 4의 배수를 4로 나누었을 때의 몫 만큼 "long"이라는 단어를 반복해서 출력 하기 위함

multiples_of_4 = int(input()) # 4의 배수인 수를 입력받는다.

number_of_iterations = multiples_of_4 // 4 # 반복 횟수를 계산한다

for i in range(number_of_iterations) : # 횟수만큼 반복하여서 long을 출력한다, 이때 end = " "를 통해 띄어쓰기로 끝을 낸다
    print("long", end = " ")
    
print("int") # 붙여서 int를 출력한다