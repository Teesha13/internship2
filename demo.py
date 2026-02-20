import os
#p=os.getcwd()
#rint(p)
#if not os.path.exists("TempDir"):
 #   os.mkdir('TempDir')

#os.chdir('D://')
#print(os.getcwd())

# name = input("enter your name : ")
# print("Your Name is ", name)
# os.mkdir(name)

# n = 5
# for i in range(1, n+1):
#     print("*" * i)

# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))

user='mac'
age=20
amount=100.12
print('ab',end='')
print('12',end='')
print(f'Welcome {user}, you are {age} years old and your bank amount is ${amount:1.4f}')

a=[3,2,0,5]
col=len(a)
row=max(a)
for i in range(row):
    for j in a:
        if row-j>=i:
            print('*  ',end='')
        else:
            print('   ',end='')
        print()