import mysql.connector


con = mysql.connector.connect(
    user="root",
    password="mysql@ommsneha20032006##*",
    host="localhost",
    port=3306,
    database="giet"

)
if con.is_connected():
    print("connected")

cur=con.cursor()
cur.execute("show databases")
for x in cur:
    print(x)

cur.execute("show tables")
for x in cur:
    print(x)
    
cur.execute("select * from gietu")
for x in cur:
    print(x)
    
cur.execute("select name from gietu")
for x in cur:
    print(x)
    
cur.execute("select name,address from gietu")
for x in cur:
    print(x)
    
cur.execute("select roll,salary from gietu")
for x in cur:
    print(x)

cur.execute("select * from gietu where name='aman'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address='delhi'")
for x in cur:
    print(x)
       
cur.execute("select * from gietu where gender='m'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where desig='doctor'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary=15000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary > 20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary < 30000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='m' and salary>20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='f' or address='raipur'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like 'a%'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like '%h'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address like '%pur%'")
for x in cur:
    print(x)
cur.execute("show databases")
for x in cur:
    print(x)

cur.execute("show tables")
for x in cur:
    print(x)
    
cur.execute("select * from gietu")
for x in cur:
    print(x)
    
cur.execute("select name from gietu")
for x in cur:
    print(x)
    
cur.execute("select name,address from gietu")
for x in cur:
    print(x)
    
cur.execute("select roll,salary from gietu")
for x in cur:
    print(x)

cur.execute("select * from gietu where name='aman'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address='delhi'")
for x in cur:
    print(x)
       
cur.execute("select * from gietu where gender='m'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where desig='doctor'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary=15000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary > 20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary < 30000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='m' and salary>20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='f' or address='raipur'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like 'a%'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like '%h'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address like '%pur%'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu order by name asc")
for x in cur:
    print(x)

cur.execute("select * from gietu order by salary desc")
for x in cur:
    print(x)
cur.execute("show databases")
for x in cur:
    print(x)

cur.execute("show tables")
for x in cur:
    print(x)
    
cur.execute("select * from gietu")
for x in cur:
    print(x)
    
cur.execute("select name from gietu")
for x in cur:
    print(x)
    
cur.execute("select name,address from gietu")
for x in cur:
    print(x)
    
cur.execute("select roll,salary from gietu")
for x in cur:
    print(x)

cur.execute("select * from gietu where name='aman'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address='delhi'")
for x in cur:
    print(x)
       
cur.execute("select * from gietu where gender='m'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where desig='doctor'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary=15000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary > 20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary < 30000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='m' and salary>20000")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where gender='f' or address='raipur'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like 'a%'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where name like '%h'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where address like '%pur%'")
for x in cur:
    print(x)
    
cur.execute("select count(*) from gietu")
for x in cur:
    print(x)
    
cur.execute("select count(*) from gietu where gender='m'")
for x in cur:
    print(x)
    
cur.execute("select * from gietu where salary between 15000 and 30000")
for x in cur:
    print(x)
cur.execute("select * from gietu where address != 'delhi'")
for x in cur:
    print(x)
cur.execute("select * from gietu where desig != 'teacher'")
for x in cur:
    print(x)
   
cur.execute("select * from gietu where name in ('aman','naman')")
for x in cur:
    print(x)
   
cur.execute("select * from gietu where name like '%a%a%'")
for x in cur:
    print(x)
    
   
cur.execute("select * from gietu where name like '_____'")
for x in cur:
    print(x)
   
cur.execute("select * from gietu where address like 'r%'")
for x in cur:
    print(x)
   
cur.execute("select * from gietu order by salary desc limit 3")
for x in cur:
    print(x)
    
   
cur.execute("select * from gietu where salary = (select min(salary) from gietu)")
for x in cur:
    print(x)
   
cur.execute("select sum(salary) from gietu where gender='m'")
for x in cur:
    print(x)
  
cur.execute("select avg(salary) from gietu where gender='f'")
for x in cur:
    print(x)
      
cur.execute("select count(*) from gietu where salary > 20000")
for x in cur:
    print(x)
  
cur.execute("select desig , count(*) from gietu group by desig")
for x in cur:
    print(x)
 
cur.execute("select gender , count(*) from gietu group by gender")
for x in cur:
    print(x)
 
cur.execute("select address , sum(salary) from gietu group by address")
for x in cur:
    print(x)
 
cur.execute("select desig from gietu group by desig having avg(salary) > 20000 ")
for x in cur:
    print(x)
 
cur.execute("select address,count(*) from gietu group by address having count(*) > 1 ")
for x in cur:
    print(x)
 
cur.execute("select * from gietu where salary > (select avg(salary) from gietu) ")
for x in cur:
    print(x)
 
 
cur.execute("select * from gietu where salary = (select max(salary) from gietu) ")
for x in cur:
    print(x)
 
cur.execute("select * from gietu where salary = (select min(salary) from gietu) ")
for x in cur:
    print(x)
 

cur.close()
con.close()


