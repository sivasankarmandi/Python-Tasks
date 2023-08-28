#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

#code:-

sdata=input("enter the comma separated values:- ",)
splitting=sdata.split(',')
slist = [int(num) for num in splitting]
stuple=tuple(slist)
print(slist)
print(stuple) 