import random
import string
def records(p):
    print(f"Total number of pulls you did is {pity}!")
    print('Thank you! (っ˘ω˘ς )')
    print("Don't forget to pull again! ૮₍ ˃ ⤙ ˂ ₎ა")
def headpat(p):
    if p<200:
        print("Do 200 pulls first! ૮₍ ˃ ⤙ ˂ ₎ა No cheating!!!")
    else:
        print(f"{'<˘<`'*2}    (づ ￣ ³￣)づ     {'`>˘>'*2}\nMei-chan loves the headpats! (っ˘ω˘ς )")
def gacha():
    c = string.digits
    l = random.choice(c)+random.choice(c)+random.choice(c)
    return l
five_pity=0
four_pity=0
pity=0
print(f"{'<˘<`'*4} Welcome to Mei-chan's Gacha Center! (っ˘ω˘ς ) {'`>˘>'*4}")
print(f"{'<˘<`'*1} You can give Mei-chan some 'headpats' if you did more than 200 pulls! {'`>˘>'*1}")
while(1):
    b=(input('Type how many pulls you want to pull or Press "Enter" to pull a quick 10x or Type "Record" to check how many pulls you did!\n'))
    if b.lower()=='record':
        record=records(pity)
        record
    if b.lower()=='headpats':
        headpats=headpat(pity)
        headpats
    if b.lower()=='off':
        break;
    c=0
    d=0
    pot=0
    if b.isnumeric() or b=='':
        if b=='':
            b=10
            for i in range(int(b)):
                pity+=1
                five_pity+=1
                four_pity+=1
                a=gacha()
                if five_pity%80==0: # For every 80 pulls you will get a guaranteed 5 star
                    print('5 Star')
                    c+=1
                    five_pity=0
                elif five_pity%70==0 or five_pity%71==0 or five_pity%72==0 or five_pity%73==0 or five_pity%74==0 or five_pity%75==0 or five_pity%76==0 or five_pity%77==0 or five_pity%78==0 or five_pity%79==0: #Soft pity from 70th to 79th pulls for 5 star
                    pot=random.choice(string.digits)+random.choice(string.digits)
                    if int(pot)>=90 and int(pot)<=97: # From 70th to 79th pull you'll have a much higher chance to get a 5 star
                        print('5 Star')
                        c+=1
                        five_pity=0
                    else:
                        if int(a)>=980:
                            print('5 Star')
                            c+=1
                        elif (int(a)>=850 and int(a)<970) or four_pity%10==0: # Also For every 10 pulls you will get a guaranteed 4 star
                            print('4 Star')
                            d+=1
                            four_pity=0
                        else:
                            print('3 Star')
                elif int(a)>=980:
                    print('5 Star')
                    c+=1
                    five_pity=0
                elif (int(a)>=850 and int(a)<970) or four_pity%10==0: # Also For every 10 pulls you will get a guaranteed 4 star
                    print('4 Star')
                    d+=1
                    four_pity=0
                else:
                    print('3 Star')
            if d!=0:
                print(f'The Amount of times you got 4 star character is {d}!')        
            if c!= 0:
                print(f'The Amount of times you got 5 star character is {c}!')
        else:
            for i in range(int(b)):
                pity+=1
                five_pity+=1
                four_pity+=1
                a=gacha()
                if five_pity%80==0: # For every 80 pulls you will get a guaranteed 5 star
                    print('5 Star')
                    c+=1
                    five_pity=0
                elif five_pity%70==0 or five_pity%71==0 or five_pity%72==0 or five_pity%73==0 or five_pity%74==0 or five_pity%75==0 or five_pity%76==0 or five_pity%77==0 or five_pity%78==0 or five_pity%79==0: #Soft pity from 70th to 79th pulls for 5 star
                    pot=random.choice(string.digits)+random.choice(string.digits)
                    if int(pot)>=90 and int(pot)<=97: # From 70th to 79th pull you'll have a much higher chance to get a 5 star
                        print('5 Star')
                        c+=1
                        five_pity=0
                    else:
                        if int(a)>=980:
                            print('5 Star')
                            c+=1
                        elif (int(a)>=850 and int(a)<970) or four_pity%10==0: # Also For every 10 pulls you will get a guaranteed 4 star
                            print('4 Star')
                            d+=1
                            four_pity=0
                        else:
                            print('3 Star')
                elif int(a)>=980:
                    print('5 Star')
                    c+=1
                    five_pity=0
                elif (int(a)>=850 and int(a)<970) or four_pity%10==0: # Also For every 10 pulls you will get a guaranteed 4 star
                    print('4 Star')
                    d+=1
                    four_pity=0
                else:
                    print('3 Star')
            if d!=0:
                print(f'The Amount of times you got 4 star character is {d}!')        
            if c!= 0:
                print(f'The Amount of times you got 5 star character is {c}!')
    elif b.lower()!= 'record' and b.lower()!= 'headpats':
        print("Please enter a valid command if you want to pull! ૮₍ ˃ ⤙ ˂ ₎ა")
