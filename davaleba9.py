'''1
def appendnumber(number):
    global int_list
    int_list.append(number)
 

int_list = [10, 20, 30, 40]
number = int(input("number to append: "))
appendnumber(number)
print(int_list)
'''
'''2
def sum_of_number(int_list):
    sums = 0
    for i in int_list:
        sums += i
    return sums

#int_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
number_input = input("input your list: ")
int_list = [int(num) for num in number_input.split( )]
sum = sum_of_number(int_list)
print(sum)
'''
'''3
def local_gt_str():
    gt_str =  "local"
    return gt_str
gt_str = "Global"
print(local_gt_str())
print(gt_str)
'''
'''4
def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number%10 + sum_of_digits(number//10)

number = int(input("your number: "))
summary = sum_of_digits(number)
print(summary)
'''
'''5'''
def reversed_string(string):
    if len(string) == 0:
        return ""
    else:   
        return string[-1] + reversed_string(string[:-1])

string = input("your string: ")
reverse = reversed_string(string)
print(reverse)
