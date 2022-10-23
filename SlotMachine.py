import os
import random
import time
import sys

class Client:
    credits = 0

    def printCredits(self):
        message = "You currently have: \u001b[32m" + str(self.credits)
        message+= "\u001b[0m credits\n"
        print(message)

    def creditsUpdate(self, incomingCredits):
        self.credits+=incomingCredits

class Slot:

    def __init__(self):
        self.symbols = ["#","$","%","&","@","£","€"]
        self.winningBonus = [5,10,20,70,200,1000,100000]

    def randomSymbol(self):
        weights = [50, 40, 30, 20, 10, 5, 1]
        symbolList = random.choices(self.symbols,weights,k = 1)
        return symbolList[0]

    def animate(self, symb1, symb2, symb3):
        index1 = random.randint(0,6)
        index2 = random.randint(0,6)
        index3 = random.randint(0,6)
        size = len(self.symbols)
        print()
        for i in range(62):
            time.sleep((0.01*i)**2+0.045)

            pres1 = self.symbols[(index1+i)%size]
            pres2 = self.symbols[(index2+i)%size]
            pres3 = self.symbols[(index3+i)%size]

            sys.stdout.write("\r\t"+pres1+pres2+pres3)
            sys.stdout.flush()
        sys.stdout.write("\r\t"+symb1+symb2+symb3)

    def winnings(self,symbol,bet):
        gains = bet * self.winningBonus[self.symbols.index(symbol)]
        return gains

    def win(self,symbol,bet):
        creditsWon = self.winnings(symbol,bet)
        print("\u001b[32mYou won!")
        print("Credits gained: " + str(creditsWon)+"\n\u001b[0m")
        return creditsWon

    def loss(self,bet):
        print("\u001b[31mYou lost.\u001b[0m\n")

    def outcome(self,bet):
        symb1 = self.randomSymbol()
        symb2 = self.randomSymbol()
        symb3 = self.randomSymbol()
        self.animate(symb1, symb2, symb3)
        print("\n\nResults:\n")
        creditsAfterPlaying = 0
        if (symb1 == symb2 == symb3):
            creditsAfterPlaying = self.win(symb1,bet)
        else:
            self.loss(bet)
        return creditsAfterPlaying

client = Client()

def displayRules():
    rules = "Every round, you are asked how many credits "
    rules+= "you want to bet. Those credits are instantly removed from "
    rules+= "your account. After that, the Slot Machine will roll. "
    rules+= "Three symbols will come out. If they are all identical, "
    rules+= "you win accordingly to each symbol's probability "
    rules+= "and your initial bet. Otherwise, you lose.\n"
    rules+= "\nThe probabilities for each symbol are as follow:\n "
    symbols = ["#","$","%","&","@","£","€"]
    winningBonus = [5,10,20,70,200,1000,100000]
    weights = [50, 40, 30, 20, 10, 5, 1]
    for i in range(7):
        rules+="\""+symbols[i]+"\" "+str(weights[i])+"/156"
        rules+=" -> "+str(winningBonus[i])+" * initial bet\n"
    print(rules)

def displayCredits():
    credits = "This program was made by \u001b[32mTomás Fonseca\u001b[0m "
    credits+= " for the Hacker School recruitment Python project.\n"
    credits+= "More info: tomas.s.fonseca@tecnico.ulisboa.pt\n"
    print(credits)

def eraseDisplay():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def getCreditsToBet():
    invalid = True
    while (invalid):
        creditsToBet=(input("\nHow many credits do you want to bet? "))
        try:
            creditsBetted = int(creditsToBet)
            if creditsBetted>client.credits:
                print("\nNot enough credits.")
            elif creditsBetted<=0:
                eraseDisplay()
                print("Invalid value inserted.")
            else:
                invalid = False
        except:
            eraseDisplay()
            print("Invalid value inserted.")
    return creditsBetted

def play():
    creditsToBet=getCreditsToBet()
    slot = Slot()
    client.creditsUpdate(0-creditsToBet)
    client.creditsUpdate(slot.outcome(creditsToBet))

def welcome():
    eraseDisplay()
    welcomeMessage = "Welcome To \u001b[31mTh\u001b[32me S\u001b[33mlo\u001b[34"
    welcomeMessage += "mt M\u001b[35mac\u001b[36mhi\u001b[37mne\u001b[0m.\n"
    print(welcomeMessage)
    invalid = True
    while (invalid):
        credits = input("How many tokens would you like to insert? ")
        try:
            credits = int(credits)
            if credits>=0:
                client.credits = credits
                invalid = False
            else:
                eraseDisplay()
                print("Please invert a valid number.\n")
        except:
            eraseDisplay()
            print("Please invert a valid number.\n")
    eraseDisplay()

def main():
    welcome()
    while(client.credits>0):
        print("Options:\n1. Display Credits (D)")
        print("2. Play (P)\n3. End Session (E)")
        print("4. How to Play (H)\n5. Credits (C)\n")
        answer = input("What do you want to do (D/P/E/H/C)? ")
        eraseDisplay()
        if (answer=="E"):
            print("Thank you for playing.\n")
            break
        elif(answer=="P"):
            print("Let's play.")
            play()
        elif(answer=="D"):
            client.printCredits()
        elif (answer=="H"):
            displayRules()
        elif (answer=="C"):
            displayCredits()
        else:
            print("Invalid Answer.\n")
    if(client.credits<=0):
        eraseDisplay()
        print("You ran out of credits.\n")

if __name__=="__main__":
    main()
