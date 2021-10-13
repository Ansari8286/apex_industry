from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from datetime import datetime
from apex.models import Register, Timmer
from apex.helper import SetTimer

# def tick():
#     SetTimer(register=Register.objects.all())


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(tick, 'interval', seconds=55)
#     scheduler.start()
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
