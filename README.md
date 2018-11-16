# 2018 Fall CS4501 Project

## Group members

> Group member 1:
> 
> Name: Liutong Chen
> 
> ComputingID: lc6re

> Group member 2:
> 
> Name: Fengxiang Chang
> 
> ComputingID: fc5kk

## Topic: University Accommodation office

Models:

Student, life advisor, hall manager, hall, room, lease

Description:

> Every student has a life advisor
>
> Every student is living in a room recorded by a lease
>
> Every hall has a manager


## To Start with

1. Go to https://github.com/gwlrz3/cs4501 to clone the repo.
2. Install Docker on yout computer(Recommend macOS).
3. Paste and run the code:
``` shell
docker pull mysql:5.7.23
mkdir ~/cs4501/db
docker run --name mysql -d -e MYSQL_ROOT_PASSWORD='$3cureUS' -v ~/cs4501/db:/var/lib/mysql  mysql:5.7.23
docker run -it --name mysql-cmdline --link mysql:db mysql:5.7.23 bash
mysql -uroot -p'$3cureUS' -h db
create user 'www'@'%' identified by '$3cureUS';
create database cs4501 character set utf8;
grant all on cs4501.* to 'www'@'%';
```
4. Go the /cs4501/4-tier-app/
5.```
docker-compose up
```
