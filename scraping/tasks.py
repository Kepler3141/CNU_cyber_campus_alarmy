import selenium
import common.db as db
import time


def test():
    db.dataBase['data'] = time.localtime().tm_min
