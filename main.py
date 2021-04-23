import conn
import datetime

#checks for any collision with other time slots
def avail_slot():
    res=conn.avail(date1,time1,room,time2," ")
    if(res[4]>0):
        print("Room",room," is occupied during the time slot provided by you either select one of the available rooms given in the list below or another time slot")
        #gets list of rooms where meeting can be conducted
        rows=conn.option(time1,time2,date1)
        for row in rows:
            print("Room",row[0],"\n")
            

    else:
        conn.ins_meet(date1,time1,room,time2)
        
        print("Your meeting has been booked!!")

#converts the entered string date to datetime date
date_entry = input('Enter meeting date in YYYY-MM-DD format\n')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

#converts the entered string start time to datetime time
time_entry = input('Enter meeting start time in HH:MM:SS format\n')
hour, min, sec = map(int, time_entry.split(':'))
time1 = datetime.time(hour, min, sec)


print('Enter 1 for Room1\n')
print('Enter 2 for Room2\n')
print('Enter 3 for Room3\n')
print('Enter 4 for Room4\n')
print('Enter 5 for Room5\n')
#takes roomid as input
room=int(input())

#converts the entered string end time to datetime time
time_end = input('Enter meeting end time in HH:MM:SS format\n')
hour1, min1, sec1 = map(int, time_end.split(':'))
time2 = datetime.time(hour1, min1, sec1)


avail_slot()


        

