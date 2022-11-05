# find the arm strong number.
#Incase ofan Armstrong number of3digits,the sum of cubes of each digit is equal to the number itself.
#For example: 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.
num=int(input('enter the number'))
sum=0
temp=num
while num:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if temp==sum:
    print('num is arm')
else:
    print('num is not arm')
