import hashlib
from termcolor import colored
path = input(" Enter the path for the file : ")
def hash_file(filename):

   h = hashlib.sha1()

   with open(filename,'rb') as file:


       chunk = 0
       while chunk != b'':

           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()

message = hash_file(path)
print()
print(" The hash of the file is :" , message )
print()
print()
print(colored("This project is developed by Techno", 'yellow'))
print()
print(colored("GitHub : https://github.com/IM-TECHNO", 'blue'))
