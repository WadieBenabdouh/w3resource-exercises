# FUNCTION OF EXERCISE 1
def find_max(list):
    for x in list:
        if x > min(list) and x >= max(list):
            print(x)

# FUNCTION OF EXERCISE 2
def sumNumbers(list):
    print(list)
    sumList = sum(list)
    print(sumList)
    
# FUNCTION OF EXERCISE 3
def multiplyNumbers(list):
    total = 1
    for number in list:
        print(number)
        total = total * number
    print(total)
