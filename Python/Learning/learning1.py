import webbrowser
import time

#time.sleep(x)
#open_webbrowser() 

def open_webbrowser():
    webbrowser.open("www.seznam.cz")

def time_backoff():
    time.sleep(5)

repetition = 1
while (repetition < 4 ):
    open_webbrowser()
    time_backoff()
    repetition = repetition + 1


