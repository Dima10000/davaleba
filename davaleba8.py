'''1
def fibonachi(n):
    
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        number = fib[-1] + fib[-2]
        fib.append(number)

    return fib

n = int(input("your number: "))
print(fibonachi(n))
'''
'''2)
def anagrama(arr1, arr2):
    if sorted(arr1) == sorted(arr2):
        return "it is anagrama"
    else:
        return "it is not anagrama"

arr1 = input("your text: ")
arr2 = input("your second text: ")

print(anagrama(arr1, arr2))
'''
'''3)
def factorial(number):
    
    if number == 0:
        return 0
    elif number == 1:
        return 1
    
    else:
        fac = 1
        while number>0:
            fac *= number
            number -= 1
        return fac

number = int(input("your number: "))
print(factorial(number))
'''
'''4)'''
def character(arr, char):
    num = 0
    for i in range(len(arr)):
        if arr[i] == char:
            num +=1
        
    if num == 0:
        return "there is no such character"
    else:
        return num
arr = input("your text: ")
char = input("your character: ")
print(character(arr, char))
