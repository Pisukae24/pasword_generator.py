import random
print("password generator project")
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['~','!','@','#','$','%','^','&','*','(',')']
t1= int(input("enter the alphabets of characters you want to make password of"))
t2=int(input("how many numbers you want to keep in you password"))
t3=int(input("enter the symbols you want to enter"))
pass_list=[]
for i in range(1,t1+1):
    char=random.choice(alphabets)
    pass_list+=char
for i in range(1,t2+1):
    char=random.choice(numbers)
    pass_list+=char
for i in range(1,t3+1):
    char=random.choice(symbols)
    pass_list+=char
random.shuffle(pass_list)
print(pass_list)
password=""
for char in pass_list:
    password+=char
print(password)
