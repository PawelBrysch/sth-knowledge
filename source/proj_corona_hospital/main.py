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


n_after_time_in_minutes = []
for t_in_minutes in range(CONSIDERED_TIME_IN_MINUTES):
    n_after_time_in_minutes.append(n_after_time_in_hours(GLOBAL_N0, t_in_minutes/60))


def get_patients_for_1_day(prob, average_time_in_minutes):
    global MAXIMUM_NUMBER_OF_PATIENTS
    all_patients = np.random.binomial(n=1, p=prob, size=MAXIMUM_NUMBER_OF_PATIENTS)
    number_of_admitted_patients = math.ceil(MAXIMUM_NUMBER_OF_PATIENTS / average_time_in_minutes)
    return list(all_patients)[:number_of_admitted_patients]

def plot(cumulation_list):
    x = list(range(CONSIDERED_TIME_IN_MINUTES))
    y = cumulation_list[:CONSIDERED_TIME_IN_MINUTES]
    plt.plot(x, y)

def batch_contrib(absolute_start_time, cumulation_list):
    for time_from_beginning in range(CONSIDERED_TIME_IN_MINUTES):
        cumulation_list[absolute_start_time + time_from_beginning] += n_after_time_in_minutes[time_from_beginning]

def patient_contrib(absolute_start_time, length, cumulation_list):
    for time_from_beginning in range(length):
        batch_contrib(absolute_start_time + time_from_beginning, cumulation_list)

def all_contrib(admitted_patients, cumulation_list, average_time_in_minutes):
    for idx, patient in enumerate(admitted_patients):
        if patient == 0:
            continue
        time_of_admission = idx * average_time_in_minutes
        patient_contrib(time_of_admission, average_time_in_minutes, cumulation_list)


def get_1day_cumulation(prob, average_time_in_minutes):
    global CONSIDERED_TIME_IN_MINUTES
    cumulation = [0] * (2 * CONSIDERED_TIME_IN_MINUTES + 3)  # viruses on each minute
    some_patients = get_patients_for_1_day(prob, average_time_in_minutes)
    all_contrib(some_patients, cumulation, average_time_in_minutes)
    return cumulation

# CUMULATION = [0] * (2 * CONSIDERED_TIME_IN_MINUTES + 3) #viruses on each minute
# some_patients = get_patients_for_1_day(0.10, 10)
# all_contrib(some_patients, CUMULATION, 10)

# batch_contrib(100, CUMULATION)
# batch_contrib(200, CUMULATION)
# patient_contrib(100, 10, CUMULATION)
# all_contrib(ADMITTED_PATIENTS, CUMULATION)


cum1 = get_1day_cumulation(0.10, 10)
cum2 = get_1day_cumulation(0.02, 10)
plot(cum1)
plot(cum2)


# plot(CUMULATION)


