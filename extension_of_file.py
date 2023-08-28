#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java


#code :-
import pathlib
extension = pathlib.Path("siva.py").suffix
print(extension)
