import matplotlib.pyplot as plt
import numpy as np
import math
EXP_A = 0.588
GLOBAL_N0 = 1000
CONSIDERED_TIME_IN_MINUTES = 480
MAXIMUM_NUMBER_OF_PATIENTS = 480

def n_after_time_in_hours(N0, t):
    global EXP_A
    return int(N0 * EXP_A ** t)

NUMBER_AFTER_MINUTES = []
for t_in_minutes in range(CONSIDERED_TIME_IN_MINUTES):
    NUMBER_AFTER_MINUTES.append(n_after_time_in_hours(GLOBAL_N0, t_in_minutes/60))



def get_patients_for_1_day(prob, average_time_in_minutes):
    global MAXIMUM_NUMBER_OF_PATIENTS
    all_patients = np.random.binomial(n=1, p=prob, size=MAXIMUM_NUMBER_OF_PATIENTS)
    number_of_admitted_patients = math.ceil(MAXIMUM_NUMBER_OF_PATIENTS / average_time_in_minutes)
    return list(all_patients)[:number_of_admitted_patients]

def plot(cumulation):
    global CONSIDERED_TIME_IN_MINUTES
    x = list(range(CONSIDERED_TIME_IN_MINUTES))
    y = cumulation.value[:CONSIDERED_TIME_IN_MINUTES]
    plt.plot(x, y, label=cumulation.get_label())
    plt.legend(loc='best')


def batch_contrib(absolute_start_time, cumulation_list):
    global CONSIDERED_TIME_IN_MINUTES, NUMBER_AFTER_MINUTES
    for time_from_beginning in range(CONSIDERED_TIME_IN_MINUTES):
        cumulation_list[absolute_start_time + time_from_beginning] += NUMBER_AFTER_MINUTES[time_from_beginning]

def patient_contrib(absolute_start_time, length, cumulation_list):
    for time_from_beginning in range(length):
        batch_contrib(absolute_start_time + time_from_beginning, cumulation_list)

def all_contrib(admitted_patients, cumulation_list, average_time_in_minutes):
    for idx, patient in enumerate(admitted_patients):
        if patient == 0:
            continue
        time_of_admission = idx * average_time_in_minutes
        patient_contrib(time_of_admission, average_time_in_minutes, cumulation_list)

class Cumulation:
    def __init__(self, prob, average_time_in_minutes):
        global CONSIDERED_TIME_IN_MINUTES
        self.prob = prob
        self.average_time_in_minutes = average_time_in_minutes
        self.value = [0] * (2 * CONSIDERED_TIME_IN_MINUTES + 3)  # viruses on each minute
        some_patients = get_patients_for_1_day(prob, average_time_in_minutes)
        all_contrib(some_patients, self.value, average_time_in_minutes)

    def get_label(self):
        return f"{self.prob} {self.average_time_in_minutes}"


class TenDayCumulation:
    def __init__(self, prob, average_time_in_minutes):
        global CONSIDERED_TIME_IN_MINUTES
        self.prob = prob
        self.average_time_in_minutes = average_time_in_minutes

        self.value = []
        for i in range(10):
            self.value += Cumulation(prob, average_time_in_minutes)


    def get_label(self):
        return f"{self.prob} {self.average_time_in_minutes}"

def get_1day_cumulation(prob, average_time_in_minutes):
    global CONSIDERED_TIME_IN_MINUTES
    cumulation = [0] * (2 * CONSIDERED_TIME_IN_MINUTES + 3)  # viruses on each minute
    some_patients = get_patients_for_1_day(prob, average_time_in_minutes)
    all_contrib(some_patients, cumulation, average_time_in_minutes)
    return cumulation




# TODO 10 dni zamiast jednego
     # TODO ogranicz value na koniec obliczania
     # TODO plot robi w zaleznosc od dlugosci
cum1 = Cumulation(0.10, 10)
cum2 = Cumulation(0.02, 10)
plot(cum1)
plot(cum2)

# NOTE sprawdzamy, czy rozklady sa dobrze liczone
# prob = 0.20
# real_probs = []
# for i in range(100):
#     some_res = list(np.random.binomial(n=1, p=prob, size=MAXIMUM_NUMBER_OF_PATIENTS))
#     freq = some_res.count(1)
#     real_probs.append(freq/MAXIMUM_NUMBER_OF_PATIENTS)
# avg_prob = sum(real_probs) / len(real_probs)