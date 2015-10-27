#!/usr/bin/python

import cgi, cgitb 
questions=0
points=0
statesinfo = {'Alabama':'Montgomery','Montana':'Helena','Alaska':'Juneau','Nebraska':'Lincoln','Arizona':'Phoenix','Nevada':'Carson City',
'Arkansas':'Little Rock','New Hampshire':'Concord','California':'Sacramento','New Jersey':'Trenton','Colorado':'Denver','New Mexico':'Santa Fe',
'Connecticut':'Hartford','New York':'Albany','Delaware':'Dover','North Carolina':'Raleigh','Florida':'Tallahassee','North Dakota':'Bismarck',
'Georgia':'Atlanta','Ohio':'Columbus','Hawaii':'Honolulu','Oklahoma':'Oklahoma City','Idaho':'Boise','Oregon':'Salem','Illinois':'Springfield',
'Pennsylvania':'Harrisburg','Indiana':'Indianapolis'}

 
form = cgi.FieldStorage() 

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Radio - Fourth CGI Program</title>"
print "</head>"
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
      print ('You are right! The capital of '+state +' is '+right_answer)
      print ('<br/>')
      points=points+1
   else:
      print("Too bad! Your answer isn't correct. It is "+ right_answer +"!")
      print ('<br/>')
score=str(points)
print('You have '+score+' points. Yay!')
print('Do you think this is good? If you do click<a href="questions.py"> here</a> to try another test') 
print "</body>"
print "</html>"
