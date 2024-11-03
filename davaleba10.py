#ბატონო პაატა მინდა გითხრათ,რომ მე შესრულებული მქონდა წინა ორი დავალებაც,მაგრამ სავარაუდოდ დამავიწყდა მათი ატვირთვა და დღეს აღმოვაჩინე,რომ ისინი ასატვირთი მქონია.მესმის შეუძლებელია მათი შეფასება,მაგრამ გთხოვთ გადაავლოთ თვალი.პატივისცემით თქვენი სტუდენტი დიმა მერებაშვილი.
'''1
def zipfunc(list1,list2):
    return list(zip(list1,list2))
list1 =  [1, 2, 3]
list2 = ['a', 'b', 'c']  

print(zipfunc(list1,list2)))
'''
'''2
from functools import reduce

def multiply_of_numbers(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers)
    except TypeError:
        return "Error: The list must contain only numbers."

numbers = list(map(int, input("Enter your numbers: ").split()))
print(multiply_of_numbers(numbers))
'''
'''3
lambda_func = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))
numbers = list(map(int, input("Enter your numbers: ").split()))
print(lambda_func(numbers))
'''
'''4'''
def filter_string(string, last_parametrs):
    try:
        return list(filter(lambda string: string.endswith(last_parametrs), string))
    except TypeError:
        return "Error: The list must contain only strings."

string = list(map(str, input("Enter your numbers: ").split()))
last_parametrs = input("Enter your last parametrs: ")
print(filter_string(string, last_parametrs))
