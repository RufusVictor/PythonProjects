class Booking:
    def __init__(self,booking_id,operation,flight,seat_class,total_seats,meal):
        self.id=booking_id
        self.operation=operation
        self.flight=flight
        self.seat_class=seat_class
        self.total_seats=total_seats
        self.meal=meal
        
    def BookingID(self):
        global seats101_EC,seats101_BC,seats102_EC,seats102_BC,summary_total101,summary_total102,r101,r102,meals_req101,meals_req102
        print("Booking Id :",self.id)
        print("Flight Number :",self.flight)
        r=[]
        total_cost=0
        if(self.seat_class=='EC' and self.flight==101):
            for x in range(7+seats101_EC,((19-(18-(self.total_seats+seats101_EC))))+6):
                r.append(x)
                r101.append(x)
            print("Economy Class :",','.join(map(str,r)))
            seats101_EC+=self.total_seats
        elif(self.seat_class=='BC' and self.flight==101):
            for x in range(1+seats101_BC,((7-(6-(self.total_seats+seats101_BC))))):
                r.append(x)
                r101.append(x)
            print("Business Class :",','.join(map(str,r)))
            seats101_BC+=self.total_seats
        if(self.seat_class=='EC' and self.flight==102):
            for x in range(7+seats102_EC,((19-(18-(self.total_seats+seats102_EC))))+6):
                r.append(x)
                r102.append(x)
            print("Economy Class :",','.join(map(str,r)))
            seats102_EC+=self.total_seats
        elif(self.seat_class=='BC' and self.flight==102):
            for x in range(1+seats102_BC,((7-(6-(self.total_seats+seats102_BC))))):
                r.append(x)
                r102.append(x)
            print("Business Class :",','.join(map(str,r)))
            seats102_BC+=self.total_seats
        if(self.meal=="Y"):
            print("Meals Required : Yes")
            if(self.flight==101):
                meals_req101+=r
            elif(self.flight==102):
                meals_req102+=r
        elif(self.meal=='N'):
            print("Meals Required : No")
        if(self.seat_class=='EC'):
            if (self.meal=="Y"):
                for y in r:
                    total_cost+=1200
            elif(self.meal=="N"):
                for y in r:
                    total_cost+=1000
        elif(self.seat_class=='BC'):
            if (self.meal=="Y"):
                for y in r:
                    total_cost+=2200
            if (self.meal=="N"):
                for y in r:
                    total_cost+=2000
        print("Total Cost :",total_cost)
        if self.flight==101:
            summary_total101+=total_cost
        elif self.flight==102:
            summary_total102+=total_cost
        
class cancel(Booking):
    def cancellation(self):
        global seats101_EC,seats101_BC,seats102_EC,seats102_BC,summary_total101,summary_total102,r101,r102,cancel_fees,meals_req101,meals_req102
        print("Booking Id :",self.id)
        print("Flight Number :",self.flight)
        if(self.seat_class=='EC' and self.flight==101):
            for x in range(7+seats101_EC-self.total_seats,((19-(18-(self.total_seats+seats101_EC))))+6):
                if x in r101:
                    r101.remove(x)
                if x in meals_req101:
                    meals_req101.remove(x)
            seats101_EC-=self.total_seats
        elif(self.seat_class=='BC' and self.flight==101):
            for x in range(1+seats101_BC-self.total_seats,((7-(6-(self.total_seats+seats101_BC))))):
                if x in r101:
                    r101.remove(x)
                if x in meals_req101:
                    meals_req101.remove(x)
            seats101_BC-=self.total_seats
        if(self.seat_class=='EC' and self.flight==102):
            for x in range(7+seats102_EC-self.total_seats,((19-(18-(self.total_seats+seats102_EC))))+6):
                if x in r102:
                    r102.remove(x)
                if x in meals_req102:
                    meals_req102.remove(x)
            seats102_EC-=self.total_seats
        elif(self.seat_class=='BC' and self.flight==102):
            for x in range(1+seats102_BC-self.total_seats,((7-(6-(self.total_seats+seats102_BC))))):
                if x in r102:
                    r102.remove(x)
                if x in meals_req102:
                    meals_req102.remove(x)
            seats102_BC-=self.total_seats
        print("Cancelled")
        for x in range(self.total_seats):
            cancel_fees+=200
        print("Total Cost :",cancel_fees)
        if self.flight==101:
            summary_total101+=cancel_fees
            for z in range(self.total_seats):
                if self.seat_class=='EC':
                    if self.meal=='Y':
                        summary_total101-=1200
                    elif self.meal=='N':
                        summary_total101-=1000
                elif self.seat_class=='BC':
                    if self.meal=='Y':
                        summary_total101-=2200
                    elif self.meal=='N':
                        summary_total101-=2000
        elif self.flight==102:
            summary_total102+=cancel_fees
            for z in range(self.total_seats):
                if self.seat_class=='EC':
                    if self.meal=='Y':
                        summary_total102-=1200
                    elif self.meal=='N':
                        summary_total102-=1000
                elif self.seat_class=='BC':
                    if self.meal=='Y':
                        summary_total102-=2200
                    elif self.meal=='N':
                        summary_total102-=2000

seats101_EC=0
seats101_BC=0
seats102_EC=0
seats102_BC=0
cancel_fees=0
summary_total101=0
summary_total102=0
r101=[]
r102=[]
meals_req101=[]
meals_req102=[]
while(1):
    a=(input('Enter Booking ID:'))
    if(a.lower()=='off'):
        break
    else:
        b=input('Enter Operation, B or C:').upper()
        c=int(input('Enter Flight Number:'))
        d=input('Enter Seat Class, EC or BC:').upper()
        e=int(input('Enter Total Number of Seats:'))
        f=input("Enter Meal Preference, Y or N:").upper()
        test=Booking(a,b,c,d,e,f)
        can=cancel(a,b,c,d,e,f)
        if(b=="B"):
            test.BookingID()
        elif(b=='B'):
            test.BookingID()
        elif(b=='C'):
            can.cancellation()
            if c==101 and d=='EC':
                seats101_EC-=e
            elif c==101 and d=='BC':
                seats101_BC-=e
            elif c==102 and d=='EC':
                seats102_EC-=e
            elif c==102 and d=='BC':
                seats102_BC-=e
r1=[]
r2=[]
print('\nSummary of Flight 101:-')
print('Seats Booked:',','.join(map(str,sorted(r101))))
print('Meals Booked:',','.join(map(str,sorted(meals_req101))))
print('Total Cost:',summary_total101)
for i in range(1,19):
    if i not in r101:
        r1.append(i)
print('Available Seats:',','.join(map(str,sorted(r1))))

print('\nSummary of Flight 102:-')
print('Seats Booked:',','.join(map(str,sorted(r102))))
print('Meals Booked:',','.join(map(str,sorted(meals_req102))))
print("Total Cost:",summary_total102)
for i in range(1,19):
    if i not in r102:
        r2.append(i)
print('Available Seats:',','.join(map(str,sorted(r2))))
