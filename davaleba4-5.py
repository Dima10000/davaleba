# davaleba 4
'''1
string=input("your string:")
st1_UTF1_CODE=string.encode('utf-8')
print(st1_UTF1_CODE)
st1_UTF1_deCODE=st1_UTF1_CODE.decode('utf-8')
print(st1_UTF1_deCODE, "\n")
'''
'''2
st=input("your string:")
st=st.strip()
st=st.lower() +" " + "Python"
st=st.replace("python","Python")
print(st)
'''
'''3
st = input("your string: ")
half_st = len(st) // 2
st1 = st[:half_st]

print(f"half text:",st1)
'''
'''4
st = input("your text:")
number = any(c.isdigit() for c in st)
alpha = any(c.isalpha() for c in st)

if alpha and number and st.isalnum():
    print("string has both")
else:
    print("text contains other symbols")
'''
'''5
st = input("your text:")

st_encode = st.encode('utf-8')
print(st_encode)

st_decode = st_encode.decode('utf-8')
print("\n",st_decode)
'''
# davaleba 5
'''1
my_list = []
import random

while True:
    task = input("your letter(choose betwen:a,r or e): ")
    
    random_number = random.randint(1,10)
    if task.lower == "a":
         my_list.append(random_number)
    elif task.lower == "r":
            del my_list[0]
    elif task.lower == "e":
        print(my_list)
        break
  
'''
'''
my_list = []

while True:
    task = input("your letter(choose betwen:a,r or e): ")

    
    if task.lower == "a":
         number = int(input("your number"))
         my_list.append(number)
    elif task.lower == "r":
        del my_list[0]
    elif task.lower == "e":
        print(my_list)
        break
 '''
'''2
my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

print(my_list_1.index(210))

my_list_1[-1].append('hello')

del my_list_1[2]
print(my_list_1)

my_list_2 = my_list_1.copy
my_list_2.clear()

print(my_list_1)
print(my_list_2)
'''
'''3'''
import re

phone_number = input("your phone number:")

pattern = r"\(\d{3}\) \d{3}-\d{3}"

if re.fullmatch(pattern, phone_number):
    print("valid phone number")
else:
    print("invalid forme")
