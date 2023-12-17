import selenium
import common.db as db
import time


def test():
    now = time
    df = db.dataBase
    df.loc[df['studentNumber'] == 'admin', 'data'] = now.strftime('%Y-%m-%d %H:%M:%S')
