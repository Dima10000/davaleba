'''1
number=int(input("your number:"))
result=0

for i in range(0, number+1):
    result+=i
  
print("result:",result)
'''
'''2
number=int(input("write number:"))
while number>0:
    print(number)
    number-=1
'''
'''3
number_to_guess=9

while True:
    guess=int(input("your guess:"))
    if guess==number_to_guess:
        print("it is right answer")
        break
    else:
      print("try again")
'''
'''4'''
total_sum=0
while True:
    user_input=input("write your number or sum:")
    if user_input=='sum':
        print("sum is:",total_sum)
        break
    else:
        number = int(user_input)
        if number>0:

            total_sum+=number
        else:
                print("only number>0")

