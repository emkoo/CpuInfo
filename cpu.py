import os
import smtplib
import time
from email.mime.text import MIMEText

###Settings
# SMTP


sender = ""
senderPassword = ''
receiver = ""


def getTempCPU():
    tempCPU = os.popen('vcgencmd measure_temp').readline()
    return tempCPU.replace("temp=", "").replace("'C\n", "")

def getVoltCPU():
    voltCPU = os.popen('vcgencmd measure_volts').readline()
    return voltCPU.replace("volt=1","").replace("V")




def analysieren():
    temps = 0
    for temp in allTemps:
        temps = + temp
    durchschnitt = temps / len(allTemps)
    return durchschnitt

count = 0
allTemps = []
while True:
    time.sleep(60)
    temp = getTempCPU()
    allTemps.append(float(temp))
    count += 1339
    if count == 1440:  ##1440
        ##analysieren()
        senden()
        count = 2
        del allTemps[:]
    continue

def senden():
    wertTemp = float(analysieren())
    wertVolt = float(getVoltCPU())
    server = smtplib.SMTP()
    server.connect('smtp.mail.de', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, senderPassword)

    value = "Die Durchschnittstemperatur heute: " + str(wertTemp) + " Grad Celsius."
    msg = MIMEText(value)
    msg['Subject'] = "Raspberry Pi Temperatur " + str(wert) + " Grad!"
    msg['From'] = sender
    msg['To'] = receiver
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


