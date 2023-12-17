import selenium
import db
import time


while True:
    now = time
    df = db.dataBase
    df.loc[df['studentNumber'] == 'admin', 'data'] = now.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(60)
