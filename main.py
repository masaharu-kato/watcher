from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import mysql.connector
from datetime import datetime

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

cnx = mysql.connector.connect(
    database='location_db',
    user='location_db_user_reader',
    password='aetoeLeexeeVah6u',
    host='127.0.0.1',
)
print('Connected to the database.')

@app.get("/api/status")
async def root():
    return {"status": "OK"}

@app.get("/api/location")
async def api_location(since: str):
    con = cnx.cursor()
    dt_since = datetime.strptime(since, "%Y-%m-%dT%H:%M:%S")
    con.execute(
        "SELECT datetime, x, y FROM location_log WHERE datetime >= '{}'".format(
            dt_since.isoformat()))
    data_locs = [
        {'datetime': datetime_, 'x': x, 'y': y}
        for (datetime_, x, y) in con
    ]
    con.close()
    return data_locs

@app.on_event("shutdown")
async def event_shutdown():
    cnx.close()
    print("Disconnected from the database.")
