print("Content-Type: text/html")
import cgi
form = cgi.FieldStorage
searchTerm = form.getvalue("name")
print("<h1>{}</h1>".format(searchTerm))
print()