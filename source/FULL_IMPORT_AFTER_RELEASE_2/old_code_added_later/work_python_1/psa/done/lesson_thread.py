'''
1. tuple = (...); func(tuple) vs func(*tuple)->               w pierwszym przypadku tupla przechodzi jako jeden argument
'''

'''########################################
WATKI
########################################'''
'''
1. jak puscic pojedyncza funckje w watku?->                                      thread.start_new_thread(func, ^*(args))
2. po co jest some_thread.join()?->             interpreter czeka, az watek wykona sie do konca (czekamy na tej linijce)
3. jak zatrzymac (i zwolnic) WSZYSTKIE(!) watki?->     lock = threading.Lock(); lock.acquire(); DO_STH!; lock.release();
4. dlaczego jest to wazne?->                        watki moga miec wspolna pamiec.  Jesli chca NARAZ z niej skorzystac, 
                                                    to moze stac sie tak, ze efektywnie skorzysta tylko jeden   
5. DEFINITION: acquired lock := fragment pomiedzy  "lock.acquire()", a "lock.release()"
        -czy musi byc wewnatrz metody "run"?->                                                                  nie wiem
6. lock.wait(), lock.notify() 
        - wymagania->                                                           musza byc wewnatrz obszaru acquired lock
        - tego samego?->             raczej nie. Wait we watku, ktory chcemy zatrzymac, notify w tym, ktory go odblokuje.
        - co robia?->                             lock trzyma interpreter na danej linii, notify go z powrotem uruchamia
        - czy to lock to "threading.Lock()"?->                                  nie, tym razem to: threading.Condition()
7. a  co jesli .wait() jest w kilku watkach? ->                                                     wtedy ".notifyAll()"
        dlaczego?                   .notify() dziala prawdopodobnie tylko wtedy, gdy .wait() zostalo uzyte tylko 1 raz. 
                                    Prawdopodobnie obiekt ma jakas liste zwaitowanych watkow.
'''
# import threading
#
#
# class myThread (threading.Thread):
#     def __init__(self, arg):
#         threading.Thread.__init__(self)
#         self.some_attr = arg
#
#     def run(self):
#         # o dziwo tutaj poleci, to co jest wywolywane start
#         pass
#
#
# thread1 = myThread(1)
# thread1.start()
