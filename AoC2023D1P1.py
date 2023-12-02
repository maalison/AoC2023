with open('input.txt', 'r') as my_file:
    my_file = my_file.readlines()

input = []
nums = []
num = ''



sum = 0


for i in my_file:
    for c in i:
        if c.isdigit():
            input.append(c)
            break
    for c in i[-1::-1]:
        if c.isdigit():
            input.append(c)
            break
    print(input)
    for i in input:
        num += i
    sum += int(num)
    print(num)
    num = ''
    input = []
    print(sum)
