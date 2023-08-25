my_string = input()

check = 1
end = len(my_string) - 1

for i in range(len(my_string)):
    if (my_string[i] != my_string[end]):
        check = 0
        break
    end -= 1

print(check)