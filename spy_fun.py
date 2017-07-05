
from spy_details import Spy,spy,friends,chat_message
from datetime import datetime
from steganography.steganography import Steganography
spy_status=None
status_message=["What's up!","Busy","Available"]


def start_chat():#function that is called to display the menu
    show_menu=True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send  secret message \n 4. Read  secret message \n 5. Read Chats from a friend \n 6. Close the Application "
        menu_choice=  raw_input(menu_choices)
        if menu_choice=='1':
            print "#you chose to update the status#"
            spy.chats=add_status(spy_status)
        elif menu_choice=='2':
            print "#you chose to add a friend#"
            num_of_friends=add_friend()
            print "spy has %d friends"%num_of_friends
        elif menu_choice=='3':
            print "#you chose to send a secret message#"
            send_message()
        elif menu_choice=='4':
            print "#you chose to read a secret message#"
            read_message()
        elif menu_choice=='5':
            print "#you chose to read chat#"
            read_chat()
        else:
            print"#application closed!#"
            show_menu= False #menu dissapears




def add_friend(): #function for adding a new friend to the list friends
    new_friend = Spy("", "", 0.0, 0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.age = raw_input("Age?:")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?:")
    new_friend.rating = float(new_friend.rating)
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating > spy.rating:#conditions for being a spy friend
        friends.append(new_friend)
        print "Friend Added!"
    else:
        print "Sorry!your friend cant be a spy!!"

    return len(friends)



def add_status(current_status_message):# function that lets user update new status or chose old status
    if current_status_message!=None:
        print "your current status message is: "+current_status_message + "\n"
    else:
        print "you dont have any status message from before!!\n"
        default=raw_input("do u want to select from older status?y/n:")
        if default.upper()=='N':
            new_status_message=raw_input("what status message you want to set?:")
            if len(new_status_message)>0:
                updated_status_message=new_status_message
                status_message.append(updated_status_message)
                print "*your status message is :%s*" % (updated_status_message)
        if default.upper() == 'Y':
                print "what status you want to choose?:"
                item_position=1

                for e in status_message:
                    print str(item_position)+ ".  " +e
                    item_position=item_position+1
                status_choice=raw_input("what status number  you wanna chose?:")
                if int(status_choice)>len(status_message):
                    print "buzzz!error!!!!!"
                if len(status_message)>=int(status_choice):
                    updated_status_message=status_message[int(status_choice)-1]
                    print "*your status message is :%s*"%(updated_status_message)
                return updated_status_message


def select_friend():#function that lets select friend from the list for another operations
    item = 0
    for friend in friends:
          print '%d.%s %s with a spy rating %.2f is online aged %d !!' % (item+ 1, friend.salutation,friend.name, friend.rating, friend.age)
          item = item+ 1

    friend_choice = raw_input("Choose the number from your friends:")
    friend_choice_position = int(friend_choice)-1
    return friend_choice_position#returns index of friend in the friends list


def send_message():#function for sending secret message via image through steganography
    print "whom do you wanna send message??"
    friend=select_friend()
    original_image=raw_input("name of image:")#path for input file
    output_path="C:\Users\DRFBGH\Desktop\secret\output.jpg"#output file path
    text=raw_input("what do u wanna say?:")
    if text=="hi":
        print "*spy wants to communicate*"
    elif text=="S0S":
        print "*spy not interested*"
    elif text=="save me":
        print "spy needs help"
    word_limit=len(text)
    if word_limit==0:
        print "You havent typed any message! "
    else:
        print "*Plz wait while message is being sent*"
        Steganography.encode(original_image, output_path, text)
        message = chat_message(text, True, datetime.now())
        friends[friend].chats.append(message)
        print "secret msg sent!"



def read_message():#functiion to decode the secret message
  sender=select_friend()
  if friends[sender].chats == []:
      print "No image sent yet!"
  else:
      secret_text = Steganography.decode("C:\Users\DRFBGH\Desktop\secret\output.jpg")
      word_count = len(secret_text)
      if word_count == 0:#message not existing
          print "No message has been sent.Image not encoded"
      elif word_count <= 100:
          timestamp = datetime.now()
          print "the secret message is :%s" % (secret_text)
          new_message = chat_message(secret_text, False, timestamp)
          friends[sender].chats.append(new_message)
      else:
          print "You speak too much!"
          del friends[sender]


def read_chat():# function for reading chats with spy friends
    friend_choice=select_friend()
    if friends[friend_choice].chats==[]:#list of chats empty
        print "You have no chats as of now!"
    else:
      for chat in friends[friend_choice].chats:
           if chat.sent_by_me==True:#if sender is ourself
               print("\033[1;31m Me:\033[1;m")
               print "%s\n sent at:"%chat.message
               print("\033[1;34m %s\033[1;m")%chat.time.strftime("%d %b %Y %H:%M")
           else:
               print ("\033[1;31m %s:\033[1;m")%(friends[friend_choice])
               print "%s"%chat.message
               print "sent at:"
               print("\033[1;34m %s\033[1;m") % chat.time.strftime("%d %b %Y %H:%M")





