
def fun(x):
    sum1 = 0
    for item in x:
        if item.isdigit():
            print(f'{item} is digit')
            sum1 += int(item)

    return sum1

str1 = input('zifuchuan:')
print('Sum:',fun(str1))
