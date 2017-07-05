from datetime import datetime
class Spy:
    def __init__(self,salutation,name,rating,age):
        self.salutation = salutation
        self.name = name
        self.rating = rating
        self.age = age
        self.is_online = True
        self.chats =[]#list that will store chats
        self.current_status_message = None



class chat_message:
    def __init__(self,message,sent_by_me,time):
        self.message=message
        self.sent_by_me=True
        self.time=time

spy=Spy('Ms','annie',3.5,20)#existing user
#spy details of friends
ari=Spy("Ms","ari",4.8,21)
anjul=Spy("Ms","anjul",4.9,21)
rose=Spy("Mr","rose",4.8,19)

friends=[ari,anjul,rose]#list that stores name of all the friends