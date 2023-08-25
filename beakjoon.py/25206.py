rate = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

sum_credit = 0
total_grade = 0

for _ in range(20):
    s, c, r = input().split()
    c = float(c)
    
    if (r != 'P'):
        sum_credit += c
        total_grade += c * grade[rate.index(r)]

print('%.6f' % (total_grade / sum_credit))