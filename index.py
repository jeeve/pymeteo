# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:14:12 2020

@author: JV
"""

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon 1er python programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""

print(html)