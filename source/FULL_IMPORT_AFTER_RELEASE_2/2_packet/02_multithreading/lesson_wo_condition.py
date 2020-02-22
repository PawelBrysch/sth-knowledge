import threading
lck = threading.Lock()
szklanka_mleka= 0

class Thread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global lck
        global szklanka_mleka

        # nalewanie
        #lck.acquire()
        for i in range(5):
            szklanka_mleka = szklanka_mleka + 1
            print("leje mleko \n")
        #lck.release()
        print("nalalem szklanke \n")

class Thread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global lck
        global szklanka_mleka

        # wypijanie

        while szklanka_mleka != 5:
            print("sprawdzam \n")
            #pass
        #lck.acquire()
        while szklanka_mleka > 0:
            print("pije mleko \n")
            szklanka_mleka = szklanka_mleka - 1
        #lck.release()

thread1 = Thread1()
thread2 = Thread2()


''' Niewlasciwa kolejnosc'''
thread2.start()
thread1.start()




