#14. Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

#code:-

from datetime import date
d0 = date(2014, 7, 2)
d1 = date(2014 ,7, 11) 
delta = d1 - d0 
print(delta.days)