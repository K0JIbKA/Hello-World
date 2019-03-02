def collatz(number):
    if number % 2 == 0 # If number is even
        print('number // 2' + number)
    elif number % 2 == 1 # If number is odd
        print(3 * number + 1)  
        
