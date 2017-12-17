create database if not exists test_ads;
use test_ads;

create table if not exists member_table(
chat_id int not null unique primary key,
state int not null
);

create table if not exists ad_table(
id int not null AUTO_INCREMENT primary key,
title varchar(250) not null,
price int,
mileage int,
transmission int,
release_year int,
model varchar(250),
brand varchar(250)
);

ALTER TABLE ad_table AUTO_INCREMENT = 4;  

alter table ad_table add column chat_id int,
add foreign key chat_id(chat_id) references member_table(chat_id);

select * from member_table;

select * from ad_table;

call is_new_member('180618224',@yes);
select @yes;

call add_new_member('123456');
call update_state('111111','2');
call fetch_state('111111',@nstate);
select @nstate;
call insert_ad('111111','تست از استورد');
call update_state_new_title_added('111111','87');
CALL update_int_field('87','mileage','123456789');
CALL update_string_field('87','brand','horse');
CALL get_ad_id('111111');
select * from ad_table where chat_id='12345' ;


CALL search_year('1200','1398');

CALL insert_ad_transaction('123456','از ترنراکشن');
