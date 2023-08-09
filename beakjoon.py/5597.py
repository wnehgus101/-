#목적: 과제를 제출하지 않은 학생을 찾아내는 프로그램 제작.

#배열을 핵생 수 만큼릐 범위로 생성.
stu_hw = [0] * 30

#과제를 내지 않은 사람이 2명이므로 28까지 반복, 과제를 낸 사람의 번호의 원소를 1로 변경.
for _ in range(28):
    hw_submit = int(input()) - 1
    stu_hw[hw_submit] = 1

#좌제를 내지 않은 학생을 찾고 번호를 출력함.    
for i in range(30):
    if stu_hw[i] == 0:
        print(i + 1)
        