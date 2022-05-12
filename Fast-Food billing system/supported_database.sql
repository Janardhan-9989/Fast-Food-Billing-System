create database fastfood;
use fastfood;
select database();
show tables;
select * from Tables_in_fastfood;
create table EMP_DETAILS (
	EID int,
    NAME varchar(50), 
    PASSWORD varchar(50),
    PHNO int
);
select * from emp_details;
insert into emp_details(EID, NAME, PASSWORD, PHNO)
values (1, 'emp', 'emp', 123);
drop table admin_details;
desc emp_details;
create table admin_details(
	AID int,
    NAME varchar(50),
    PASSWORD varchar(50),
    PHNO int
);
desc admin_details;
insert into admin_details(AID, NAME, PASSWORD, PHNO)
values (1, 'admin', '123', 1234),
	   (2, 'admin1', 'admin', 12345);
drop table admin_details;
select * from item_details;

create table item_details(
	IID int,
    NAME varchar(50),
    COST int
);
drop table item_details;
insert into item_details(IID, NAME, COST)
values (1, 'samosa', 30),
(2, 'pav bhaji', 15);

create table bills (
	DATETIME varchar(40),
    EID int, 
    AMOUNT int, 
    REFNO int
);
insert into bills(DATETIME, EID, AMOUNT, REFNO)
values ('15-04-2022 12:09', 1, 242, 548220);

SET SQL_SAFE_UPDATES = 0;
delete from bills where EID = 1;
delete from deleted_bills where EID = 1;
create table deleted_bills(
	DATETIME varchar(40),
    EID int,
    AMOUNT int, 
    REFNO int
);

insert into deleted_bills(DATETIME, EID, AMOUNT, REFNO)
values ('20-04-2022  00:07', 1, 97, 284821);

select * from deleted_bills;
select * from bills;