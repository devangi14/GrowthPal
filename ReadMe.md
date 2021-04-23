# Growth Pal-Schedule Management System

## The Task
### For a person:
- Schedule a meeting with the input of Date, Time, Room ID and Time Period (or to and from time)
- Should be able to detect any collisions if scheduling a new meeting
- Room should be selected from a fixed set: (R1, R2, R3, R4, R5)

## Requirements
* Python 3.x
* MySQL

## Proposed Solution
##### The program takes input from user involving following information
* Date of the meeting in the form YY-MM-DD
* starting time in the form HH:MM:SS
* ending time in the form HH:MM:SS
* RoomId they want to conduct their meeting in.(1-5)

##### It aims on detecting any collision with other meetings being conducted in the room selected by user.If a collision is detected it provides the user with a list of rooms if any where he/she can have their meeting smoothly without any interruption on the date and time provided by them.

## Usage Instructions
- main.py:The main file that is executed and is responsible for user interactions i.e. user input and output
- conn.py:This file acts a middleware that handles the user request and connects us with database.It involves three functions-
 avail-calls the procedure defined in sql to check for any meeting collisions
 ins_meet-responsible for inserting details of the meeting if its not clashing with another meeting.
 option-provides user with different room option incase the room user selected is occupied.
- sql file:consists of database creation and procedure creation.