#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

#code:-
n=int(input("enter a number :- ",))
nn=int(str(n)+str(n))
nnn=int(str(n)+str(n)+str(n))
x=n+nn+nnn
print(x)