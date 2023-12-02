with open('input.txt', 'r') as my_file:
    my_file = my_file.readlines()

input = []
nums = []
num = ''



sum = 0


for i in my_file:
    i = i.replace("one", 'o1e')
    i = i.replace("two", 't2o')
    i = i.replace("three", 't3e')
    i = i.replace("four", 'f4r')
    i = i.replace("five", 'f5e')
    i = i.replace("six", 's6x')
    i = i.replace("seven", 's7n')
    i = i.replace("eight", 'e8t')
    i = i.replace("nine", 'n9e')

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
