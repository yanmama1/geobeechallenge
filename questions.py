#!/usr/bin/python

import cgi, cgitb, random
questions = 0
# Import modules for CGI handling
statesinfo = {'Alabama':'Montgomery','Montana':'Helena','Alaska':'Juneau','Nebraska':'Lincoln','Arizona':'Phoenix','Nevada':'Carson City',
'Arkansas':'Little Rock','New Hampshire':'Concord','California':'Sacramento','New Jersey':'Trenton','Colorado':'Denver','New Mexico':'Santa Fe',
'Connecticut':'Hartford','New York':'Albany','Delaware':'Dover','North Carolina':'Raleigh','Florida':'Tallahassee','North Dakota':'Bismarck',
'Georgia':'Atlanta','Ohio':'Columbus','Hawaii':'Honolulu','Oklahoma':'Oklahoma City','Idaho':'Boise','Oregon':'Salem','Illinois':'Springfield',
'Pennsylvania':'Harrisburg','Indiana':'Indianapolis'}	

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Chloe's geobee state test</title>"
print "</head>"
cap=statesinfo.values()
l=statesinfo.keys()
random.shuffle(l)
print('<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">')
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
    print('<input type="radio" name="group'+qn+'"'+' value="'+state+'+'+choices[0]+'" /> '+choices[0]+' <br>')
    print('<input type="radio" name="group'+qn+'"'+' value="'+state+'+'+choices[1]+'" /> '+choices[1]+' <br>')
    print('<input type="radio" name="group'+qn+'"'+' value="'+state+'+'+choices[2]+'" /> '+choices[2]+' <br>')
    print('<input type="radio" name="group'+qn+'"'+' value="'+state+'+'+choices[3]+'" /> '+choices[3]+' <br>')
    print"<br>"
    questions=questions+1
print('<input type="submit" value="Select Subject" />')
print('</form>')
print "</body>"
print "</html>"

  
