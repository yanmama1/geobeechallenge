#!/usr/bin/python

import cgi, cgitb 
import mysql.connector

cnx = mysql.connector.connect(user='geobeeshop', database='beeworld', host='mysql.geobeeshop.com', password='geobeemaster1')

cur = cnx.cursor(dictionary=True)
query = ("select n.name country, c.name capital from Country n join City c on n.capital = c.id where n.Population > 2000000;")
cur.execute(query)
rows = cur.fetchall()
# print(rows)

cur.close()
cnx.close()

statesinfo = dict((rows[i]["country"], rows[i]["capital"]) for i in range(0, len(rows)))

questions=0
points=0


 
form = cgi.FieldStorage() 

print "Content-type:text/html charset=utf8 \r\n\r\n"
print "<html>"
print "<head>"
print "<title>Radio - Fourth CGI Program</title>"
print "</head> <meta charset='UTF-8'>"
print "<body>"

for x in range(0,5):
   s='group'+str(x)
 #  print s
   if form.getvalue(s):
      subject = form.getvalue(s)
   else:
      subject = "Not set"

   
   #print "<h3>Selected capital is %s</h3>" % subject

   state=subject.split('+')[0]
   answer=subject.split('+')[1]
   right_answer=statesinfo[state]
   if right_answer == answer:
      print ('You are right! The capital of '+state +' is '+right_answer.encode('utf-8'))
      print ('<br/>')
      points=points+1
   else:
      print("Too bad! Your answer isn't correct. The capital of "+ state + " is "+ right_answer.encode('utf-8') +"!")
      print ('<br/>')
score=str(points)
print('You have '+score+' points. Yay!')
print('Do you think this is good? If you do click<a href="country-capital.py"> here</a> to try another test') 
print "</body>"
print "</html>"
