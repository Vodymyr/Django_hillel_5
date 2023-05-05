< !-- teachers.html -->

{ % extends
'base.html' %}

{ % block
content %}
< h1 > Teachers
List < / h1 >
< ul >
{ %
for teacher in teachers %}
< li > {{teacher.name}} - {{teacher.subject}} < / li >
{ % empty %}
< li > No
teachers
found. < / li >
{ % endfor %}
< / ul >

< h2 > Add
a
new
teacher: < / h2 >
< form
method = "post" >
{ % csrf_token %}
{{form.as_p}}
< button
type = "submit" > Save < / button >
< / form >
{ % endblock %}

< !-- groups.html -->

{ % extends
'base.html' %}

{ % block
content %}
< h1 > Groups
List < / h1 >
< ul >
{ %
for group in groups %}
< li > {{group.name}} < / li >
{ % empty %}
< li > No
groups
found. < / li >
{ % endfor %}
< / ul >

< h2 > Add
a
new
group: < / h2 >
< form
method = "post" >
{ % csrf_token %}
{{form.as_p}}
< button
type = "submit" > Save < / button >
< / form >
{ % endblock %}
