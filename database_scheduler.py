import schedule
import time
import datetime
import web_scraper as ws


# Schedule the function to run daily
schedule.every().day.at("00:00").do(ws.refreshdatabase)  

last_run = None

while True:
    schedule.run_pending()
    now = datetime.datetime.now()
    if last_run is None or (now - last_run).days >= 7:
        ws.refreshdatabase()
        last_run = now

    time.sleep(1)
