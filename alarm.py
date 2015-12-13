import time, threading, os

FAVOURITE_YOUTUBE_PLAYLIST = "https://www.youtube.com/watch?v=5Uc2t4AoE3A&list=PLGGw37RuWoSZ3ai9QsKWL6UyfStRWVJKz"
ONE_MINUTE_IN_SECONDS = 1
class AlarmClock(threading.Thread):
    def __init__(self, hours, minutes):
        threading.Thread.__init__(self)
        self.h = int(hours)
        self.m = int(minutes)
        self.keep_alive = True

    def run(self):
        while self.keep_alive:
            now = time.localtime()
            if now.tm_hour == self.h and now.tm_min == self.m:
                os.system("start ", FAVOURITE_YOUTUBE_PLAYLIST)
                self.keep_alive = False
            else:
                time.sleep(ONE_MINUTE_IN_SECONDS)

def gui_add_alarm():
    wake_up = input("when do you want to wakt up?\n(in the format hh:mm please)\n")
    alarm = AlarmClock(*(wake_up.split(':')))
    alarm.start()
    print("time got is {}:{}".format(*(wake_up.split(':'))))
    print("daemon has started, the process will be closed now.",
          "Your favorite youtube playlisy",
          "{}".format(FAVOURITE_YOUTUBE_PLAYLIST),
          "will be played in time to wake you up",
          sep='\n')

if __name__ == '__main__':
    now = time.localtime()
    print("the time now is {}:{}".format(now.tm_hour, now.tm_min))
    gui_add_alarm()
    


    
