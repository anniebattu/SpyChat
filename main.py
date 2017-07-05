import spy_fun
from spy_details import Spy,spy

print "welcome!!!let's get started!"
question="continue as %s %s?y/n:"%(spy.salutation,spy.name)
#choose whether new user or existing user
existing=raw_input(question)
if(existing.upper()=='Y'):
   print "*****\nspy name:%s %s\nspy age:%.2f\nspy rating:%d\n spy online?: %s\n*****"%(spy.salutation,spy.name,spy.age,spy.rating,spy.is_online)
   spy_fun.start_chat()
else:
# details for new user
  spy_name=raw_input("Hi!Welcome to SpyChat .What's your name??:")
  if len(spy_name)>0:
       print "Welcome " + spy_name + " glad to have you with us! :)"
       spy_salutation=raw_input("What should we call you?? Mr/Ms?:")
       spy_name= spy_salutation + " " + spy_name
       print "Alright!! " + spy_name + "\n*** I'd like to know  a bit more about you***"
       spy_age = raw_input("What's your age?:")
       spy_age = int(spy_age)
       if spy_age > 12 and spy_age < 50:
           spy_rating = raw_input("What's your spy rating?:")
           spy_rating = float(spy_rating)
           if spy_rating >= 4.5:
               print "*You are good ace!!*"
           elif spy_rating >= 3.5 and spy_rating < 4.5:
               print "*You are among good one's!!*"
           elif spy_rating >= 2.5 and spy_rating < 3.5:
               print "*You can do better!!*"
           else:
               print "*There's always someone in office for help!*"

           print "***Authentication complete.!!***\nSpy name:" + spy_name + " Spy age:" + str(
               spy_age) + "\nSpy rating:" + str(spy_rating) + "\nProud to have you onboard!! :)"
           spy_fun.start_chat()
       else:
           print "Sorry u can't be a Spy!!:("
  else:
      #spy should fulfill all the conditions
       print "Spy needs to have a valid name.try again!"


