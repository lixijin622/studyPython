for num in range(2, 20):
    for div in range(2, num):
        if num % div == 0:
            print(num, 'equals ', div, ' * ', num//div)
            break
    else:
        print(num, ' is a prime number')
