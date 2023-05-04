
##################################
## Author: Mahammadali AGHABAYLI #
##################################

from datetime import datetime
import os
import sqlite3
import psutil
import shutil

def remove_passwords():

    # Find currently logged user.
    username = psutil.users()[0].name

    # Close Chrome.
    os.system("taskkill /F /IM chrome.exe /T")

    now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S.%f')

    # Create a backup of the SQLite database.
    shutil.copyfile("C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Default/Login Data", "C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Default/Login_Data_BACKUP_" + now)

    # Connect to main database.
    conn = sqlite3.connect("C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Default/Login Data")
    c = conn.cursor()

    # Delete rows which contains username.
    for row in c.execute('DELETE FROM logins WHERE username_value != ""'):
        print(row)

    conn.commit()
    conn.close()

#while True:
#    now = datetime.now()
#    if now.hour == 17 and now.minute == 0:  # 17:00
#        remove_passwords()
#    time.sleep(15)

remove_passwords()
