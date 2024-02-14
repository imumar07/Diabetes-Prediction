import pywhatkit
from datetime import datetime 
def do_message():
    today=datetime.now()
    hours=int(today.strftime("%H"))
    minutes=(int(today.strftime("%M"))+2)
    pywhatkit.sendwhatmsg("+916309346330","Hi From Umar's Laptop :), This is to test the python whatsapp module",hours, minutes)