import User
import json

with open("user_data.json","r") as file:
    data=json.load(file)
def create():
    list_data=list(data)
    f=int(list_data[0])
    for c in list_data:
        if int(c)>f:
            f=int(c)

    account_number=str(int(data[str(f)]["accountnumber"])+1)
    card_number=str(f+1)
    name=input("enter name: ")
    lastname=input("enter last name: ")
    passcode=input("enter passcode: ")
    inventory=int(input("enter amount: "))

    user1=User.User(card_number)
    user1.data(name=name,last_name=lastname,passcode=passcode,inventory=inventory,
            account_number=account_number)
create()


