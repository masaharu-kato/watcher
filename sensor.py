import mysql.connector
import datetime
import time
import random
import threading

cnx = mysql.connector.connect(
    database='location_db',
    user='location_db_user_inserter',
    password='heiKeenei0Qui9pi',
    host='127.0.0.1',
)
print('Connected to the database.')

class App:

    def __init__(self):
        self.loc_x = 0.0
        self.loc_y = 0.0
        self.walk_max_x = 10.0
        self.walk_max_y = 10.0
        self.time_interval = 1 # sec

    def refresh_location(self):
        self.loc_x += random.random() * self.walk_max_x
        self.loc_y += random.random() * self.walk_max_y

    def insert_to_db(self):
        con = cnx.cursor()
        datetime_str = datetime.datetime.now().isoformat()
        sql = "INSERT INTO location_log(datetime, x, y) VALUES('{}', '{}', '{}');".format(
            datetime_str, self.loc_x, self.loc_y)
        con.execute(sql)
        cnx.commit()
        con.close()

    def worker(self):
        self.refresh_location()
        print('Loc: ({}, {})'.format(self.loc_x, self.loc_y))
        self.insert_to_db()

    def mainloop(self):
        now = time.time()
        while True:
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            t.join()
            wait_time = self.time_interval - ( (time.time() - now) % self.time_interval )
            time.sleep(wait_time)

app = App()

try:
    app.mainloop()
except KeyboardInterrupt:
    pass

cnx.close()
print('Disconnected.')
