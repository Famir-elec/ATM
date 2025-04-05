from services import Services
from os import system


def clear():
    system('cls')


s = Services()


def main():
    cardnumber = input("please enter card number: ")
    password = input("please enter password: ")
    if s.Authentcation(cardnumber, password):
        while True:
            n = input(
                "enter the option number to use each service:\n1.transfer to cart\n2.transfer to acccount\n3.show inventory\n4.show transaction\n")

            if n == "1":
                another_card_number = input("please enter the destination card: ")
                amount = input("enter the transfer amount: ")
                s.mony_transfer_to_cart(cardnumber, another_card_number, amount)
                d = input("Do you any other request?(y/n) ")
                if d.capitalize() == "Y":
                    continue
                elif d.capitalize() == "N":
                    break
                else:
                    print("the incorrect phrase")
            elif n == "2":
                another_card_account = input("please enter the destination account: ")
                amount = input("enter the transfer amount: ")
                s.mony_transfer_to_acccount(cardnumber, another_card_account, amount)
                d = input("Do you any other request?(y/n) ")
                if d.capitalize() == "Y":
                    continue
                elif d.capitalize() == "N":
                    break
                else:
                    print("the incorrect phrase")
            elif n == "3":
                s.show_inventory(cardnumber)
                d = input("Do you any other request?(y/n) ")
                if d.capitalize() == "Y":
                    continue
                elif d.capitalize() == "N":
                    break
                else:
                    print("the incorrect phrase")
            elif n == "4":
                s.show_transaction(cardnumber)
                d = input("Do you any other request?(y/n) ")
                if d.capitalize() == "Y":
                    continue
                elif d.capitalize() == "N":
                    break
                else:
                    print("the incorrect phrase")
            else:
                print("please enter again.")


if __name__ == "main":
    main()
