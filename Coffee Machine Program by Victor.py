class coffee_machine:
    def __init__(self,drink):
        self.drink=drink
       
    def ordered_drink(self):
        global w,m,c,mon
        if(self.drink=='espresso'):
            if(w<200):
                print('Sorry,there is not enough water')
                print(f"Given money ${total} is being refunded")
            elif(m<100):
                print('Sorry,there is not enough milk')
                print(f"Given money ${total} is being refunded")
            elif(c<40):
                print('Sorry,there is not enough coffee')
                print(f"Given money ${total} is being refunded")
            elif(total>=3):
                print("Payment is successful!")
                w-=200
                m-=100
                c-=40
                mon+=3.00
                if(total>3):
                    print(f"Here is ${round((total-3),2)} dollars in change")
                    print(f'Enjoy your {self.drink} :)')
                else:
                    print(f'Enjoy your {self.drink} :)')
            elif(total<3):
                print("Not enough amount given for the selected drink")
                print(f"Given money ${total} is being refunded")
                
        if(self.drink=='latte'):
            if(w<200):
                print('Sorry,there is not enough water')
                print(f"Given money ${total} is being refunded")
            elif(m<100):
                print('Sorry,there is not enough milk')
                print(f"Given money ${total} is being refunded")
            elif(c<40):
                print('Sorry,there is not enough coffee')
                print(f"Given money ${total} is being refunded")
            elif(total>=4.50):
                print("Payment is successful!")
                w-=150
                m-=200
                c-=20
                mon+=4.50
                if(total>4.50):
                    print(f"Here is ${round((total-4.50),2)} dollars in change")
                    print(f'Enjoy your {self.drink} :)')
                else:
                    print(f'Enjoy your {self.drink} :)')
            elif(total<4.50):
                print("Not enough amount given for the selected drink")
                print(f"Given money ${total} is being refunded")
                
        if(self.drink=='cappuccino'):
            if(w<200):
                print('Sorry,there is not enough water')
                print(f"Given money ${total} is being refunded")
            elif(m<100):
                print('Sorry,there is not enough milk')
                print(f"Given money ${total} is being refunded")
            elif(c<40):
                print('Sorry,there is not enough coffee')
                print(f"Given money ${total} is being refunded")
            elif(total>=2.00):
                print("Payment is successful!")
                w-=200
                m-=100
                c-=50
                mon+=2.00
                if(total>2.00):
                    print(f"Here is ${round((total-2),2)} dollars in change")
                    print(f'Enjoy your {self.drink} :)')
                else:
                    print(f'Enjoy your {self.drink} :)')
            elif(total<2.00):
                print("Not enough amount given for the selected drink")
                print(f"Given money ${total} is being refunded")
                
    def report(self):
        print(f'Water:{w}ml')
        print(f'Milk:{m}ml')
        print(f'Coffee:{c}g')
        print(f"Money:${round(mon,2)}")
w=1000
m=800
c=350
mon=0
print("Welcome to Coffee Maker Menu")
while(1):
    order=input("What would you like? (espresso/latte/cappuccino):").lower()
    if order=='off':
        break
    elif order=='add_resources':
        water=int(input('Enter the amount of water you want to add:'))
        milk=int(input('Enter the amount of milk you want to add:'))
        coffee=int(input('Enter the amount of coffee you want to add:'))
        w+=water
        m+=milk
        c+=coffee
        print("Report after adding resources:-")
        a=coffee_machine(order)
        a.report()
    elif order=='report':
        a=coffee_machine(order)
        a.report()
    elif order=='espresso' or order== 'latte' or order=='cappuccino':
        print("Give coins for payment")
        q=int(input("Number of quarters:"))
        d=int(input("Number of dimes:"))
        n=int(input("Number of nickel:"))
        p=int(input("Number of pennies:"))
        total=0
        total=round((q*0.25)+(d*0.10)+(n*0.05)+(p*0.01),2)
        print(f'Given amount for payment:${round(total,2)}')
        a=coffee_machine(order)
        a.ordered_drink()
    else:
        print("Invalid drink selected")
