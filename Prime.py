"""Prime number Checker
program for beginners"""
num = int(input("Enter a number: "))
#we just took the input in the form of integer
if num > 1:
#smallest primme number is two
   for i in range(2,int(num/2)):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num) #two times back slash, one for providing escape char
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")