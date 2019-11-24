'''
1. czemu queue jest spoko?->                                                              chyba moze pomiescic cokolwiek
2. lock         - jak zrobic?->                                                                   multiprocessing.Lock()
                - jak uzyc?->                         jak thredowego, z tym, ze trzeba go przekazac jako argument proces
3. if __name__ == "__main__":
                - po co?->             metoda start uruchamia skrypt raz jeszcze (wraz z importami). Nie chcemy rekursji
                - czy zatem wystarczy, jak bedzie tam sam ".start"?->                                           nie wiem
'''
import multiprocessing

result_nonshared = []

def calc_square(numbers, array, queue):
    global result_nonshared
    for idx, n in enumerate(numbers):
        result_nonshared.append(n * n)
        array[idx] = n*n
        queue.put(n*n)
    print("inside nonshared " + str(result_nonshared) + " " + str(id(result_nonshared)))
    print("inside shared    " + str(array[:]) + " " + str(id(array)))

if __name__ == "__main__":
    arr = [2,3,8,9]
    result_shared = multiprocessing.Array("i", 4)
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result_shared, queue)) #argumenty sa kopiowane
    p1.start()
    p1.join()

    print("outside nonshared " + str(result_nonshared) + " " + str(id(result_nonshared)))
    print("outside shared    " + str(result_shared[:]) + " " + str(id(result_shared)))
    while queue.empty() is False:
        print(queue.get())
