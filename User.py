import json
from os import path
class User:
    def __init__(self,card_number):
        self.card_number=card_number
        self.user=self.reloud_json()
    def reloud_json(self):
        if path.exists("user_data.json"):
            with open("user_data.json","r") as file:
                return json.load(file)
        return {}
    def data(self,passcode,account_number,name,last_name,inventory):
        user_info={
            "passcode":passcode,
            "accountnumber":account_number,
            "name":name,
            "lastname":last_name,
            "inventory":inventory
        }
        self.user[self.card_number]=user_info
        self.save_file()
    def save_file(self):
        with open("user_data.json","w") as file:
                json.dump(self.user,file,indent=4)




