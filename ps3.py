###### this is the third .py file ###
#intialisation has been done
state={"BIHAR":'000',"HARYANA":'001',"NEW DELHI":'010',"KERALA":'011'}
city={"PATNA":'111',"NEW DELHI":'110',"CHANDIGARH":'101',"CALICUT":'100'}
district={"IIT PATNA":'000',"NIT HARYANA":'001',"IIT DELHI":'010',"NIT JALANDHAR":'011'}
print "1.add 2.modify 3.delete 4.query"
a=input("enter the operation you want to perform")
#to do the stuffs for condition 1
if a==1:
	s=raw_input("enter the state name  to add")
	m=raw_input("enter the code name to add for state")
	state.update({s:m})
	c=raw_input("enter the city name to add")
	n=raw_input("enter the code name to  add for city")
	city.update({c:n})
	d=raw_input("enter the district name you want to add")
	q=raw_input("enter the code name  to be add for district")
	district.update({d:q})
#to do the stuffs for condition 2	
if a==3:	
	b=raw_input("enter the state to deleted\n")
	if b in state.keys():	
		del state[b]
	else :
		print "not a valid key"
	b=raw_input("enter the city  to deleted\n")
	if b in city.keys():	
		del city[b]
	else :
		print "not a valid key" 
	b=raw_input("enter the district  to deleted\n")
	if b in district.keys():	
		del district[b]
	else :
		print "not a valid key"
#to do the stuffs for condition 2
if a==2:
	t1=raw_input("enter the state whose code y to modify\n")
	t11=raw_input("enter the new code\n")
	if t1 in state.keys():
		state.update({t1:t11})
	else :
		print 'not a valid state'
	t2=raw_input("enter the district whose c to modify\n")
	t21=raw_input("enter the new code\n")
	if t2 in district.keys():
		district.update({t2:t21})
	else :
		print 'not a valid district'
	t3=raw_input("enter the city whose code  to modify\n")
	t31=raw_input("enter the new code\n")
	if t3 in city.keys():
		city.update({t3:t31})
	else :
		print 'not a valid city'
#to do the stuffs for else condition
else :
	l1=raw_input("enter the customer name\n")
	l2=raw_input("enter the customer district\n")
	l3=raw_input("enter the customer city\n")
	l4=raw_input("enter the customer state\n")
	if l1 in state.keys():
		print "CC_NO = ",state.get(l4, default=None)
	if l1 in district.keys():
		print district.get(l2, default=None)
	if l1 in city.keys():
		print city.get(l3, default=None)
	print "Human Readable code"
	if l1 in state.keys():
		print 
	if l1 in state.keys():
		print state.get(l4, default=None)
	if l1 in district.keys():
		print district.get(l2, default=None)
	if l1 in city.keys():
		print city.get(l3, default=None)
	
print state
####### write your code here ##########
