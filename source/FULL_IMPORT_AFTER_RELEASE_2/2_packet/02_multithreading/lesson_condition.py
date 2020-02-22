import threading
lck = threading.Condition()
szklanka_mleka= 0


# nalewanie
class Thread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global lck
        global szklanka_mleka

        lck.acquire()
        for i in range(5):
            szklanka_mleka = szklanka_mleka + 1
            print("leje mleko \n")
        print("nalalem szklanke \n")
        lck.notify()
        lck.release()

        # wypijanie
class Thread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global lck
        global szklanka_mleka

        lck.acquire()
        while szklanka_mleka != 5:
            print("sprawdzam \n")
            lck.wait()
        while szklanka_mleka > 0:
            print "pije mleko \n"
            szklanka_mleka = szklanka_mleka - 1
        lck.release()

thread1 = Thread1()
thread2 = Thread2()

thread2.start()
thread1.start()