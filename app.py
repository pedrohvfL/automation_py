import pyautogui as py
import time

class Refresh:

    

    def start(self):
        py.press('win')
        time.sleep(1)

    def navegation(self):
        py.write('chrome')
        time.sleep(1)

    def enter(self):
        py.press('ENTER')
        time.sleep(1)

    def searchSite(self):
        py.write('https://playspectre.com/twitch-drops')
        time.sleep(1)

    def enter1(self):
        py.press('ENTER')
        time.sleep(1)

    def reload(self):
        for _ in range(1000 ):
            py.press('f5')
            time.sleep(1)



refresh = Refresh()
refresh.start()
refresh.navegation()
refresh.enter()
refresh.searchSite()
refresh.enter1()
refresh.reload()


