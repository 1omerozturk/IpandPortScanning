""" TCP/IP PORT LİSTESİ:
FTP:21
SSH:22
TELNET:23
SMTP:25
HTTP:80
NETBIOS:139
HTTPS:443
SMB:445
RDB:3389
 """

from tkinter import*
import socket


def tarama():
    s1=str(enturl.get())
    liste=[21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 
    445, 587, 993, 1433, 3306, 3389, 5900, 8080]
    try:
        for port in liste:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result=sock.connect_ex((s1,port))
            if result==0:
                listsonuc.insert(1,"Port{} açık".format(port))
            else:
                listsonuc.insert(1,"Port{} kapalı".format(port))
        sock.close()
    except socket.error:
        print("Bilgisayara ulaşılamadı")

pen=Tk()
pen.geometry("330x500")
pen.title("Açık port tarama")
pen.resizable(FALSE,FALSE)

lblurl=Label(pen,text="URL veya IP ADRESİ",font="Verdana 12 bold",fg="white",bg="black")
lblurl.place(x=60,y=20)
listsonuc=Listbox(pen,font="Verdana 12 bold",width=25,height=17,fg="white",bg="black")
listsonuc.place(x=27,y=140)
enturl=Entry(pen,font="Verdana 12 bold",fg="blue")
enturl.place(x=50,y=50)
btntara=Button(pen,text="Taramayi Başlat",font="Verdana 12 bold",fg="white",bg="black",command=tarama)
btntara.place(x=80,y=90)
            
                
            


pen.mainloop()