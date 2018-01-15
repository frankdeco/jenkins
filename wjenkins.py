import jenkins
import datetime
import sqlite3
#this is to intialise the database
def initialise_db():
    db= sqlite3.connect('job.sqlite')
    cursor =db.cursor()
    cursor.execute('''

                    CREATE TABLE IF NOT EXISTS info(id INTEGER PRIMARY KEY, name TEXT, status TEXT, time TEXT)''')
    db.commit()
    db.close()
#this saves the database
def save2db(name, buildno):
        db= sqlite3.connect('job.sqlite')
        cursor =db.cursor()
        cursor.execute('''INSERT INTO info(name, status, time)
                  VALUES(?,?, DATETIME('NOW'))''', (name, buildno))
        print('saved in database')
        db.commit()
        db.close()
#this method connects to the jenkin jobs
def connect2job():
    initialise_db()
    url = 'http://localhost:8080'
    name = input('enter the name of the server:')
    password= input('enter the password:')
    server = jenkins.Jenkins(url, username=name, password=password)
    check = 0
    try:
        server.get_whoami()
        check = 1
    except(jenkins.JenkinsException):
        print('Authentication error')
        server.get_info
        check = 0
    if(check):
        jobs=server.get_all_jobs()
        for item in jobs:
            time= datetime.datetime.now().time()
            jname=item['name']
            lastbuildnumber= server.get_job_info(jname)['lastBuild']['number']
            save2db(jname,lastbuildnumber)
            print('done')

connect2job()
            
        
        
