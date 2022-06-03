#!/usr/bin/python3
import base64

logo = '''
██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║
██████╔╝███████║███████╗█████╗  ███████╗ ███████║
██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║
██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝
'''

def crypt():
  print ("")
  print (logo)
  print ("[1] Encode")
  print ("[2] Decode")
  print ("")
  i = int(input(">>> Enter Your Choice : "))
  if i==1:
    encode = input(">>> Type Your Text : ")
    a = encode.encode('ascii')
    b = base64.b64encode(a)
    c = b.decode('ascii')
    print ("")
    print ("Text You Encoded")
    print ("")
    print(c)
    print ("")
  elif i==2:
    decode = input(">>> Type Your Text : ")
    a = decode.encode('ascii')
    b = base64.b64decode(a)
    c = b.decode('ascii')
    print ("")
    print ("Text You decoded")
    print ("")
    print(c)
    print ("")
  else:
    print("")
    print ("  Wrong Input Please Try Again")
    print("")
    exit()
crypt()