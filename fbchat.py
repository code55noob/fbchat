from fbchat import Client
from fbchat.models import*

username = str(input("username : "))
password = str(input("password : "))
id_target = int(input("id : "))
number = int(input("Number of turns : "))
msg = str(input("message : "))

client = Client(username,password)

for x in range(number):
    
 print('Own id: {}'.format(client.uid))
 client.send(Message(text=msg), thread_id=id_target, thread_type=ThreadType.USER)
 
client.logout()