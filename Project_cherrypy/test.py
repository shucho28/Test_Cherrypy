"""from cherrypy.process.plugins import Daemonizer
Daemonizer(cherrypy.engine).subscribe()"""

import os

import cherrypy
from mysql.connector import errorcode
import mysql.connector


connect = mysql.connector.connect(user="adminC41VckI", password = "jmL6CRYHJqfR")
cursor = connect.cursor()
DB_NAME = "project"
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    connect.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        connect.database = DB_NAME
    else:
        print(err)
        exit(1)

try:
    new_table = (
    "CREATE TABLE data_grievance ("
    "    complaint_id INT(11) NOT NULL AUTO_INCREMENT,"
    "    name VARCHAR(50) NOT NULL,"
    "    email VARCHAR(255) NOT NULL,"
    "    department VARCHAR(255) NOT NULL,"
    "    grievance text NOT NULL,"
    "    PRIMARY KEY (complaint_id))")
    
    cursor.execute(new_table)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)

class First():
    @cherrypy.expose
    def complain(self):
        return open("front/complaint.html")

    @cherrypy.expose
    def index(self):
        return open("front/index.html")
    
    @cherrypy.expose
    def submit(self,**kwargs):
        add_grievance = ("INSERT INTO data_grievance "
               "(name, email, department, grievance) "
               "VALUES (%s, %s, %s, %s)")
        data = (kwargs['name'],kwargs['email'],kwargs['department'],kwargs['grievance'])
        cursor.execute(add_grievance,data)
        return "<h1>{}</h1>".format(data)

if __name__ == '__main__':
    conf = {
            '/':{
                 'tools.staticdir.on':True,
                 'tools.staticdir.root':os.path.dirname(os.path.abspath(__file__)),
                 'tools.staticdir.dir':'./front',
            },
            '/favicon.ico':{
                            'tools.staticfile.on':True,
                            'tools.staticfile.root':os.path.dirname(os.path.abspath(__file__))+'\\template_6\\images',
                            'tools.staticfile.filename':'logo.ico'
                            }
    }
    """print(os.path.abspath(__file__))
    cherrypy.config.update({'server.socket_host':'10.206.160.183',
                            'server.socket_port':3128
                            }
                            )"""
    print(os.path.dirname(os.path.abspath(__file__))+'\\template_6\\images')
    cherrypy.quickstart(First(),'/', conf)
 
