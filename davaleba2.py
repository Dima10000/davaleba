'''1)
num_list=[44, 23, 11, 8, 20, 56, 33, 55]
number=int(input("Enter a number:"))
if number in num_list:
    print("the number in list")
else:
     print("the number not in list")
'''
'''2)
number=int(input("Enter an integer:"))
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")
'''
'''3)
st1="hello world"
st2="hello world"
if st1 is st2:
    print("same object")
else:
    print("different object")
st3=input("your phrase:")
if st1 is st3:
    print("same object")
else:
    print("different object")

print(id(st3),id(st1))
st3=st1
print(id(st3),id(st1))
if st1 is st3:
    print("same object")
else:
    print("different object")
'''
'''4)'''
num_list=[44, 23, 11, 8, 20, 56, 33, 55]
number=int(input("Enter a number:"))
if num_list[2]<number<num_list[7]:
    print("More than list elements")
elif number==num_list[5]:
    print("equal")
else:
    print("None of the conditions were met")