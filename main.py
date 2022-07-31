import pandas as pd
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader

import random
from win10toast import ToastNotifier
from datetime import date
import pdf_to_list
import athan_class
import schedule
import time

# Global values for the position each item is at in the list
DAY = 0
F_TIME = 1
SUN_TIME = 2
D_TIME = 3
A_TIME = 4
M_TIME = 5
I_TIME = 6

# This line detects what date it is
TODAY = int(date.today().strftime("%d"))

# This is the list of ahadith that will be used in the notification
HADITH = [
    "A companion asked, “O Messenger of Allah, which deeds are best?” Rasool Allah (SAW) replied, “Prayer on time\" "
    "(al-Mu’jam al-Kabīr 9687)",
    "\"Verily, prayer restrains (oneself) from shameful and unjust deeds…” (Quran 29:45)",
    "\"“Without a doubt, in the remembrance of Allah do hearts find satisfaction.” (Quran 13:28)",
    "\"“And perform prayer... surely the good deeds remove the evils deeds.” (Quran 11:114)",
    "\"“Seek help in patience and prayer.” (Quran 2:153)",
    "Rasool Allah said, “Whoever preserves the prayers, they will be his light, proof, and salvation on the Day of "
    "Resurrection...” (Ṣaḥīḥ Ibn Ḥibbān 1467)",
    "“(the people in Hell will be asked) What has caused you to enter Hell? They will say: We were not of those who "
    "used to pray…” (Quran 74:42-43)",
    "“Guard strictly your (habit of) prayers...\"  (Quran 2:238-9)"
]

# This function runs the first time the program is opened in order retrieve a list of prayer times from the PDF
list_of_times = pdf_to_list.new_times()


# Prayer Objects
F = athan_class.Athan("Fajr", list_of_times[TODAY][F_TIME])
D = athan_class.Athan("Dhur", list_of_times[TODAY][D_TIME])
A = athan_class.Athan("Asr", list_of_times[TODAY][A_TIME])
M = athan_class.Athan("Magreb", list_of_times[TODAY][M_TIME])
I = athan_class.Athan("Isha", list_of_times[TODAY][I_TIME])


# The function that sends the notification when its time to pray
def notification(prayer):
    toast = ToastNotifier()
    toast.show_toast(
        prayer.time_to_pray(),
        random.choice(HADITH),
        duration=120,
        threaded=True,
    )


# The function that sends the notification for a reminder when its time to pray
def reminder(prayer):
    toast = ToastNotifier()
    toast.show_toast(
        prayer.reminder(),
        random.choice(HADITH),
        duration=120,
        threaded=True,
    )


# scheduled Fajr time and reminder before sunrise
schedule.every().day.at(F.time).do(notification, F)
# schedule.every().day.at(F.time).do(reminder(F))

# scheduled Dhur time and reminder before Asr
schedule.every().day.at(D.time).do(notification, D)
# schedule.every().day.at(list_of_times[TODAY][A_TIME]).do(reminder(D))

# scheduled Asr time and reminder before Magreb
schedule.every().day.at(A.time).do(notification,A)
# schedule.every().day.at(list_of_times[TODAY][M_TIME]).do(reminder(A))

# scheduled Magreb time and reminder before Isha
schedule.every().day.at(M.time).do(notification, M)
# schedule.every().day.at(list_of_times[TODAY][I_TIME]).do(reminder(M))

# scheduled Isha time
schedule.every().day.at(I.time).do(notification, I)

# updates the list at the start of each month


while True:
    schedule.run_pending()
    time.sleep(1)
