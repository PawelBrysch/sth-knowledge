import threading
total_distance = 0
lock = threading.Lock()

class runner(threading.Thread):
    def __init__(self, nr_startowy):
        self.numer = nr_startowy
        threading.Thread.__init__(self)
    def run(self):
        global lock
        global total_distance
        dystans = 42000
        while dystans > 0:
            dystans = dystans - 1

            ''' Lock HERE!!!'''
            lock.acquire()
            total_distance = total_distance + 1
            lock.release()

            # if dystans % 10000 == 0:
            #     print "Zawodnik nr %i" % self.numer, " ",  dystans, "\n"
        print "Zawodnik %i na mecie" % self.numer, "\n"

r1 = runner(1)
r2 = runner(2)
r1.start()
r2.start()

'''join HERE'''
r1.join()
r2.join()
print "KOD DOSZEDL - dystans->", total_distance, "\n"

