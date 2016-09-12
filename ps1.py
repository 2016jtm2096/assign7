###### This is the first .py file ###########
str1 = raw_input(" enter the srting : ")
word_freq = {}
from collections import Counter
print ("top 3 frequent words:")
lis = sorted(Counter(str1.split()).items(),key=lambda (i,j):(-j,i))[:3]
for word,freq in lis:
 print word, freq
lis = sorted(Counter(str1.split()).items(),key=lambda (i,j):(-j,i))[:]
for word,freq in lis:
	def perms(s):        
	    if(len(s)==1): 
		return [s]
	    result=[]
	    for i,v in enumerate(s):
		result += [v+p for p in perms(s[:i]+s[i+1:])]
	    return result
	print('\n'.join(perms(word)))
