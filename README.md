# 2018 Fall CS4501 Project

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





## Project2

Topic: University Accommodation office

Models:

Student, life advisor, hall manager, hall, room, lease

Description:

Every student has a life advisor;
Every student is living in a room recorded by a lease;
Every hall has a manager;


## API examples:
list the halls: /myapp/hall/list

Create a new hall: /myapp/hall/create
by POSTing { "name" : "name1", "address" : "add1"}

Delete a hall with pk=2: /myapp/hall/delete/2

Update a hall with pk=1: /myapp/hall/update/1
by POSTing { "name" : "name2", "address" : "add2"}
