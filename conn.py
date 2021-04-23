import mysql.connector
#connects to sql

#function to call procedure from sql to check for collision
def avail(start_date,start_time,roomid,end_time,ret):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "Gpal"
    
    )
    cur=con.cursor()
    result=cur.callproc('meetSlot',[start_date,start_time,roomid,end_time,ret])
    con.close()
    return result

#function to insert meeting details incase of no collision
def ins_meet(date1,time1,room,date2):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "Gpal"
    
    )
    cur=con.cursor()
    cur.execute("INSERT INTO meeting VALUES(%s,%s,%s,%s)",(date1,time1,room,date2))
    con.commit()
    con.close()


#function to provide user with other available options of rooms
def option(startt,endt,date):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "Gpal"
    
    )
    cur=con.cursor()
    cur.execute("select  distinct Room_ID from meeting where Room_ID not in(Select Room_ID from meeting where( %s between start_Time and end_Time or %s between start_Time and end_Time) and %s=start_Date    )",(startt,endt,date))
    
    rows=cur.fetchall()
    con.close()
    return rows

