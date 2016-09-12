import random
#asking to enter total number of users in that area
x=input("enter total number of user in that area: ")
#generating random location of users in that area
numbers = {random.random()*2-1:random.random()*2-1  for i in range(x)}
print numbers
y = numbers.keys()
z = numbers.values()
count=0
#counting the number of people who are outside the circle
for i in range(x) :
 g=y[i]*y[i]+z[i]*z[i]
 if(g>1) :
  count=count+1
t=count*100/x
print  "percentange outside",t,"%"
