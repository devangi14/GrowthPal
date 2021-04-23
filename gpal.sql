drop database Gpal;
create database Gpal;
use Gpal;

create table if not exists meeting(
start_Date date not null,
start_Time time not null,
Room_ID varchar(2) not null,
end_Time time not null

);

insert into meeting values("2020-09-08","13:04:38",2,"15:04:38");
insert into meeting values("2020-09-08","11:04:38",1,"15:04:38");
insert into meeting values("2020-10-08","13:04:38",3,"15:04:38");
insert into meeting values("2021-09-08","13:04:38",4,"15:04:38");
insert into meeting values("2020-09-28","13:04:38",5,"15:04:38");

select * from meeting;

-- Procedure to check if the time slot entered by user is causing any collision or not

Delimiter $$
create procedure meetSlot(IN dt date,IN startt time,IN rooms_id int,IN endt time,out count int)
begin

select count(*) into count from meeting where 
(startt between start_Time and end_Time
or endt between start_Time and end_Time)
and dt=start_Date
and rooms_id=Room_ID
;


end$$

-- count/c variable results in 0 incase of no collision else it results in 1

call meetSlot("2020-04-08","08:04:38",3,"09:04:38",@c);
select @c;

select  distinct Room_ID from meeting where Room_ID not in
(Select Room_ID from meeting where
( "13:04:38" between start_Time and end_Time
or "14:04:38" between start_Time and end_Time)
and "2020-04-08"=start_Date
)
;


