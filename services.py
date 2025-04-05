import os
from json import dump, load
import csv
from datetime import datetime


class Services:

    def __init__(self):
        with open("user_data.json", "r") as file:
            self.data = load(file)

    def save_transaction(self, card_number, type,time, transaction_amount=0,Destination="-"):
        if os.path.isfile("transaction.csv"):
            with open(f"{card_number}_transaction.csv", "r") as cfile:
                cdata = list(csv.reader(cfile))
            newdata = [type, transaction_amount,time,Destination]
            cdata.append(newdata)
            with open(f"{card_number}_transaction.csv", "w") as c2file:
                writer = csv.writer(c2file)
                writer.writerow(["type", "transaction_amount", "time"])
                writer.writerow(cdata)
        else:
            with open(f"{card_number}_transaction.csv", "w") as c3file:
                writer = csv.writer(c3file)
                writer.writerow(["type", "transaction_amount", "time"])
                writer.writerow([type,transaction_amount,time,Destination])

    def mony_transfer_to_cart(self, self_card_number, another_card_nember, amount):
        if self.data[self_card_number]["inventory"] >= amount:
            self.data[self_card_number]["inventory"] -= amount
            self.data[another_card_nember]["inventory"] += amount
            with open("user_data.json", "w") as file:
                dump(self.data, file, indent=4)
            self.save_transaction(self_card_number,"transfer to card",f"{str(datetime.today())}",amount,another_card_nember)
            print("The operation was successfully carried out")
        else:
            print("Not enough inventory")

    def mony_transfer_to_acccount(self, self_card_number, another_account_number, amount):
        if self.data[self_card_number]["inventory"] >= amount:
            self.data[self_card_number]["inventory"] -= amount
            code_number = another_account_number[5:8]
            another_card_number = "515253510" + code_number
            self.data[another_card_number]["inventory"] += amount
            with open("user_data.json", "w") as file:
                dump(self.data, file, indent=4)
            self.save_transaction(self_card_number, "transfer to account", f"{str(datetime.today())}", amount,another_card_number)
            print("The operation was successfully carried out")
        else:
            print("Not enough inventory")

    def show_inventory(self, self_card_number):
        inventory = self.data[self_card_number]["inventory"]
        self.save_transaction(self_card_number, "show inventory",f"{str(datetime.today())}")
        print(f"your account inventory is:{inventory}")

    def show_transaction(self,card_number):
        with open(f"{card_number}_transaction.csv","r")as file:
            cdata=list(csv.reader(file))
        if len(cdata)>=3:
            print(cdata[-1:-4:-1])
        elif len(cdata)==2:
            print(cdata[-1:-3:-1])
        elif len(cdata)==1:
            print(cdata[0])
        else:
            print("You have not had any transactions")

        self.save_transaction(card_number, "show inventory", f"{str(datetime.today())}")
    def Authentcation(self,card_number,password):
        if self.data[card_number]["passcode"] == password:
            return True
        else:
            return False
