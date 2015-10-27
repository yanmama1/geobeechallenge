#!/usr/bin/python

import cgi, cgitb, random
import mysql.connector

cnx = mysql.connector.connect(user='geobeeshop', database='beeworld', host='mysql.geobeeshop.com', password='geobeemaster1')

cur = cnx.cursor(dictionary=True)
query = ("select n.name country, c.name capital from country n join city c on n.capital = c.id order by rand() limit 40;")
cur.execute(query)
rows = cur.fetchall()
# print(rows)

cur.close()
cnx.close()


statesinfo = dict((rows[i]["country"], rows[i]["capital"]) for i in range(0, len(rows)))

'''
for country in my_dict.keys():
        print "the capital of {} is {}".format(country.encode('utf-8'), my_dict[country].encode('utf-8'))
'''

questions = 0
# Import modules for CGI handling
'''
statesinfo = {'Alabama':'Montgomery','Montana':'Helena','Alaska':'Juneau','Nebraska':'Lincoln','Arizona':'Phoenix','Nevada':'Carson City',
'Arkansas':'Little Rock','New Hampshire':'Concord','California':'Sacramento','New Jersey':'Trenton','Colorado':'Denver','New Mexico':'Santa Fe',
'Connecticut':'Hartford','New York':'Albany','Delaware':'Dover','North Carolina':'Raleigh','Florida':'Tallahassee','North Dakota':'Bismarck',
'Georgia':'Atlanta','Ohio':'Columbus','Hawaii':'Honolulu','Oklahoma':'Oklahoma City','Idaho':'Boise','Oregon':'Salem','Illinois':'Springfield',
'Pennsylvania':'Harrisburg','Indiana':'Indianapolis'}	
'''

print "Content-type:text/html; charset=utf8 \r\n\r\n"
print "<html>"
print "<head>"
print "<title>Chloe's geobee state test</title>"
print "</head> <meta charset='UTF-8'>"
cap=statesinfo.values()
l=statesinfo.keys()
random.shuffle(l)
print('<form action="/cgi-bin/cntr-cap.py" method="post" target="_blank">')
while questions < 5:
    state=l[questions]
    v = statesinfo[state]
    answer = cap.index(v)
    t=random.randint(0,3)
    random.shuffle(cap)
    choices = cap[0:4]
    if v not in choices:
        choices[t]=v
        
    qn=str(questions)
    print('What is the capital of ' + state +'?')
    print"<br>"
    for i in range(0,4):
        qstr= '<input type="radio" name="group'+qn+'"'+' value="'+state+'+'+choices[i]+'" /> '+choices[i]+' <br>'
        print qstr.encode('utf-8')

    print("<br>")
    questions=questions+1
print('<input type="submit" value="Submit Your Answers" />')
print('</form>')
print "</body>"
print "</html>"

  
