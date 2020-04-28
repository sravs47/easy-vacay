insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('American Airlines','AA330','San Antonio','Dallas',now(),'2018-12-10',100,150,5000,'On Time','Domestic','07:30','09:30');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('United Airlines','UA170','San Antonio','Chicago',now(),now(),100,250,15000,'On Time','Domestic','07:30','09:30');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('South west','SW130','San Antonio','Dallas','2018-12-05','2018-12-10',100,59,15000,'In Flight','Domestic','12:30','17:30');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('Frontier','FR227','San Antonio','Dallas','2018-12-05','2018-12-10',100,99,12000,'Delayed','Domestic','13:25','15:30');

insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('Frontier','FR227','San Antonio','Dallas','2020-11-02','2020-11-02',100,99,12000,'Delayed','Domestic','13:25','15:30');

insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('Frontier','FR227','Austin','Houston','2020-03-29','2020-03-30',100,99,12000,'On Time','Domestic','13:25','15:30');

insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('Frontier','FR227','austin','houston','2020-04-28','2020-04-30',100,110,12000,'On Time','Domestic','13:25','15:30');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('American Airlines','AA100','sanantonio','dallas','2020-04-28','2020-04-30',100,59,12000,'On Time','Domestic','13:25','15:30');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values('Southwest Airlines','SW200','houston','sanantonio','2020-04-28','2020-04-30',100,330,12000,'On Time','Domestic','13:25','15:30');


insert into flight_listings(id,airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values(1000,'American Airlines','AA456','New York','Orlando','2018-12-24','2018-12-27',100,500,5000,'On Time','Domestic','07:30','09:30');
insert into flight_listings(id,airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values(1001,'Emirates','EM234','California','Hyderabad','2018-12-24','2018-12-31',100,2000,5000,'On Time','International','01:30','23:30');
insert into flight_listings(id,airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type,begins,ends)
values(1002,'Southwest','SW236','Houston','Hawaii','2018-12-24','2018-12-27',100,2000,5000,'On Time','Domestic','05:30','11:30');





insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Dallas','Hilton Grand','101 South parkway',25,150,now(),'2020-12-30');
insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Chicago','Marriot hotels','102 North parkway',25,130,now(),'2020-12-30');
insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Dallas','Marriot hotels','102 Military parkway',105,130,now(),'2020-12-30');
insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Dallas','Omni Hotels','101 West parkway',225,130,now(),'2018-12-30');
insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Dallas','Opera hotels','102 Driveway parkway',45,130,now(),'2018-12-30');






insert into hotel_listings(id,city,hname,address,rooms,hprice,fromdate,todate)
values(1000,'Orlando','Hyatt','234 NW parkway, Airport blvd',25,500,'2018-12-24','2018-12-27');
insert into hotel_listings(id,city,hname,address,rooms,hprice,fromdate,todate)
values(1001,'Hyderabad','Greenpark','1234 Panjagutta,Hyderabad,500018',25,2000,'2018-12-24','2018-12-31');
insert into hotel_listings(id,city,hname,address,rooms,hprice,fromdate,todate)
values(1002,'Hawaii','Oceanview Resort','23 Beach road, Palm avenue',25,1500,'2018-12-24','2018-12-27');


create table testdates(dt Date,ts Timestamp,dtime Datetime);

select * from testdates;

select date_format(dt,'%d/%m/%Y') from testdates where dt='2018/12/05'

insert into testdates(dt,ts,dtime) values(now(),sysdate(),sysdate());

select * from flight_listings
