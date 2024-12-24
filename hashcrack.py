import fade
from fade import *
import os
import hashlib
import platform

def clear():
    opsys = platform.system()
    if opsys == "Windows":
       os.system("cls")
    else:
       os.system("clear")

def banner():
   bansys = """
   ╦ ╦┌─┐┌─┐┬ ┬╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
   ╠═╣├─┤└─┐├─┤║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘
   ╩ ╩┴ ┴└─┘┴ ┴╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─
   |-------------------------------|
   |                               |
   |         HASHCRACKER           |
   |     Pyhton Hash Cracking      |
   |          Software             |
   |_______________________________|
   """
   print(fade.fire(bansys)) 

def banner2():
   clear()
   bansys = """
       ___     ___     ___   .___   ____   .____  _      _
     .   '   \  .'   `. .'   `. /   `  /   \  /       `.   / 
     |       |     | |     | |    | |,_-<  |__.      `./  
     |    _  |     | |     | |    | |    ` |         ,'   
     `.___|  `.__.'  `.__.' /---/  `----' /----/ _-'     
     |------------------------------------------------|
     |              CODED BY:G3K45                    |
     |________________________________________________|                                                
   """
   print(fade.random(bansys))


def exit():
   print("Do you want to exit the program?")
   option = input("[y]yes [n]no:")
   if option == "y":
      banner2()
   elif option == "n":
      main()
   else:
      clear()
      print("Try again")
      exit()

 
def main():
   clear() 
   banner()
   print("[1]Crack a Hash with a single payload")
   print("[2]Crack a Hash with multiple payloads")
   print("[3]Exit the program")
   option = input(">>>")
   if option == "1":
      print("[1]MD5")
      print("[2]SHA-1")
      print("[3]SHA-256")
      print("[4]SHA-384")
      print("[5]SHA-512")
      option2 = input("Enter the type of HASH:")
      if option2 == "1":
         estring = input("Enter the HASH STRING:")
         dstring = input("Enter the decrypted string:")
         hash = hashlib.md5(dstring.encode())
         shash = hash.hexdigest()
         if shash == estring:
            print(f"Hash String:{dstring}")
         else:
            print("The Payload is not correct")
         exit()
      elif option2 == "2":
         estring = input("Enter the HASH STRING:")
         dstring = input("Enter the decrypted string:")
         hash = hashlib.sha1(dstring.encode())
         shash = hash.hexdigest()
         if shash == estring:
            print(f"Hash String:{dstring}")
         else:
            print("The payload is not correct")
         exit()
      elif option2 == "3":
         estring = input("Enter the HASH STRING:")
         dstring = input("Enter the decrypted string:")
         hash = hashlib.sha256(dstring.encode())
         shash = hash.hexdigest()
         if shash == estring:
            print(f"Hash String:{dstring}")
         else:
            print("The Payload is not correct")
         exit()
      elif option2 == "4":
         estring = input("Enter the HASH STRING:")
         dstring = input("Enter the decrypted string:")
         hash = hashlib.sha384(dstring.encode())
         shash = hash.hexdigest()
         if shash == estring:
            print(f"Hash String:{dstring}")
         else:
            print("The Payload is not correct")
         exit() 
      elif option2 == "5":
         estring = input("Enter the HASH STRING:")
         dstring = input("Enter the decrypted string:")
         hash = hashlib.sha512(dstring.encode())
         shash = hash.hexdigest()
         if shash == estring:
            print(f"Hash String:{dstring}")
         else:
            print("The Payload is not correct")
         exit()
      else:
         clear()
         print("Try again")
         main() 
   elif option == "2":
      print("[1]MD5")
      print("[2]SHA-1")
      print("[3]SHA-256")
      print("[4]SHA-384")
      print("[5]SHA-512")
      option = input(">>>")
      if option == "1":
        estring = input("Enter HASH STRING:")
        dir = input("Enter directory or name of the file with the payloads:")
        files = open(dir, "r")
        for sys in files.readlines():
            words = sys.replace("\n","")
            payload = words.encode('utf-8')
            shash = hashlib.md5(payload.strip()).hexdigest()
            if shash == estring:
                print(f"Hash String:{payload}")
                break
            else:
                print("The payload is not correct")
        files.close()
        exit()
      elif option == "2":
        estring = input("Enter HASH STRING:")
        dir = input("Enter directory or name of the file with the payloads:")
        files = open(dir, "r")
        for sys in files.readlines():
            words = sys.replace("\n","")
            payload = words.encode('utf-8')
            shash = hashlib.sha1(payload.strip()).hexdigest()
            if shash == estring:
                print(f"Hash String:{payload}")
                break
            else:
                print("The payload is not correct")
        files.close()
        exit()
      elif option == "3":
        estring  = input("Enter HASH STRING:")
        dir = input("Enter directory or name of the file with the payloads:")
        files = open(dir, "r")
        for sys in files.readlines():
            words = sys.replace("\n","")
            payload = words.encode('utf-8')
            shash = hashlib.sha256(payload.strip()).hexdigest()
            if shash == estring:
                print(f"Hash String:{payload}")
                break
            else:
                print("The payload is not correct")
        files.close()
        exit()
      elif option == "4":
        estring = input("Enter HASH STRING:")
        dir = input("Enter directory or name of the file with the payloads:")
        files = open(dir, "r")
        for sys in files.readlines():
            words = sys.replace("\n","")
            payload = words.encode('utf-8')
            shash = hashlib.sha384(payload.strip()).hexdigest()
            if shash == estring:
                print(f"Hash String:{payload}")
                break
            else:
                print("The payload is not correct")
        files.close()
        exit()
      elif option == "5":
        estring = input("Enter HASH STRING:")
        dir = input("Enter directory or name of the file with the payloads:")
        files = open(dir, "r")
        for sys in files.readlines():
            words = sys.replace("\n","")
            payload = words.encode('utf-8')
            shash = hashlib.sha512(payload.strip()).hexdigest()
            if shash == estring:
                print(f"Hash String:{payload}")
                break;
            else:
                print("The payload is not correct")
        files.close()
        exit() 
   elif option == "3":
     banner2() 
   else:
     clear()
     print("Try again")
     main()

main()
