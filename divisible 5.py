def listnumbers(a):
    print('Your given in the list:',a)
    print('List of numbers divisible by 5')
    for i in a:
        if (i%5 == 0):
            print(i)
number=[10,20,33,46,10,100,350,400,670,700,333,444]
listnumbers(number)
