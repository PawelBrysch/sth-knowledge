import matplotlib.pyplot as plt
import numpy as np
import math
EXP_A = 0.588
GLOBAL_N0 = 1000
CONSIDERED_TIME_IN_MINUTES = 480
MAXIMUM_NUMBER_OF_PATIENTS = 480



par_prob = 0.10
par_average_time_in_minutes = 10

def n_after_time_in_hours(N0, t):
    global EXP_A
    return int(N0 * EXP_A ** t)


n_after_time_in_minutes = []
for t_in_minutes in range(CONSIDERED_TIME_IN_MINUTES):
    n_after_time_in_minutes.append(n_after_time_in_hours(GLOBAL_N0, t_in_minutes/60))


# all_patients = np.random.binomial(n=1, p=par_prob, size=MAXIMUM_NUMBER_OF_PATIENTS)
# number_of_admitted_patients = math.ceil(MAXIMUM_NUMBER_OF_PATIENTS/par_average_time_in_minutes)
# ADMITTED_PATIENTS = list(all_patients)[:number_of_admitted_patients]

def get_patients_for_1_day(prob, average_time_in_minutes):
    global MAXIMUM_NUMBER_OF_PATIENTS
    all_patients = np.random.binomial(n=1, p=par_prob, size=MAXIMUM_NUMBER_OF_PATIENTS)
    number_of_admitted_patients = math.ceil(MAXIMUM_NUMBER_OF_PATIENTS / par_average_time_in_minutes)
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

def all_contrib(admitted_patients, cumulation_list):
    global par_average_time_in_minutes
    for idx, patient in enumerate(admitted_patients):
        if patient == 0:
            continue
        time_of_admission = idx * par_average_time_in_minutes
        patient_contrib(time_of_admission, par_average_time_in_minutes, cumulation_list)



CUMULATION = [0] * (2 * CONSIDERED_TIME_IN_MINUTES + 3) #viruses on each minute
# batch_contrib(100, CUMULATION)
# batch_contrib(200, CUMULATION)
# patient_contrib(100, 10, CUMULATION)
some_patients = get_patients_for_1_day(0.10, 10)
all_contrib(some_patients, CUMULATION)
# all_contrib(ADMITTED_PATIENTS, CUMULATION)

plot(CUMULATION)


