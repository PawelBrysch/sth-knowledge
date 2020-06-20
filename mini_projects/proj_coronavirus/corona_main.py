# TODO jak elegancko napisac te property, by w podgladzie nie bylo widac podwojnych (chyba sie nie da)

import random
import copy
import numpy as np
from collections import deque

MAX_TIME = 30
MAX_MORTALITY_RATE = 50


class TimeSeries:
    def __init__(self, cumulations=None, differences=None):
        self._cumulations = cumulations
        self._differences = differences

    @property
    def differences(self):
        if self._differences is None:
            self._differences = [self._cumulations[0]]
            for day_number, _ in enumerate(self._cumulations[:-1]):
                self._differences.append(self._cumulations[day_number + 1] - self._cumulations[day_number])
        return self._differences

    @property
    def cumulations(self):
        if self._cumulations is None:
            self._cumulations = []
            cumulation = 0
            for difference in self.differences:
                cumulation += difference
                self._cumulations.append(cumulation)
        return self._cumulations

    @property
    def number_of_days(self):
        return len(self._cumulations)


def draw_positive_differences(number_of_days, max_value):
    value = [0] * number_of_days
    mortality_rate = random.randint(1, max_value)
    for i in range(mortality_rate):
        value[random.randint(0, number_of_days - 1)] += 1
    return value


# random_vector = MortalityVector(differences=draw_positive_differences(
#     number_of_days=MAX_TIME,
#     max_value=MAX_MORTALITY_RATE
# ))

class Confirmed(TimeSeries):
    def __init__(self, *args, **kwargs):
        TimeSeries.__init__(self, *args, **kwargs)
        self.magic_array_size = self.number_of_days - 1
        self._magic_array = None

    @property
    def magic_array(self):
        if self._magic_array is None:
            self._magic_array = np.zeros(shape=(self.magic_array_size, self.magic_array_size))
            next_row = deque(reversed(self.differences[:-1]))
            for row in range(self.magic_array_size - 1, -1, -1):
                self._magic_array[row, :] = next_row
                next_row.popleft()
                next_row.append(0)
        return self._magic_array


class MortalityVector(TimeSeries):
    def __init__(self, *args, **kwargs):
        TimeSeries.__init__(self, *args, **kwargs)
        self.mortality_rate = sum(self.differences)

    def calculate_aligned_cumulations(self, desired_length):
        aligned_cumulations = copy.copy(self.cumulations)
        last_element = aligned_cumulations[-1]
        while len(aligned_cumulations) < desired_length:
            aligned_cumulations.append(last_element)
        aligned_cumulations = aligned_cumulations[:desired_length]
        as_percentages = list(map(
            lambda x: x / 100,
            aligned_cumulations
        ))
        as_column_vector = np.array(as_percentages).reshape(desired_length, 1)
        return as_column_vector



def calculate_deaths(confirmed, mortality_vector):
    deaths_as_column_vector = np.matmul(
        confirmed.magic_array,
        mortality_vector.calculate_aligned_cumulations(confirmed.magic_array_size)
    )
    as_list = list(deaths_as_column_vector[:, 0])
    taking_into_account_zero_deaths_at_the_beginning = [0] + as_list
    as_time_series = TimeSeries(cumulations=taking_into_account_zero_deaths_at_the_beginning)
    return as_time_series

# confirmed_it = [0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,20,62,155,229,322,453,655,888,1128,1694,2036,2502,3089,3858,4636,5883,7375,9172,10149,12462,12462,17660,21157,24747,27980,31506,35713,41035,47021]
# deaths_it = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,7,10,12,17,21,29,34,52,79,107,148,197,233,366,463,631,827,827,1266,1441,1809,2158,2503,2978,3405,4032]

confirmed_it = [3,20,62,155,229,322,453,655,888,1128,1694,2036,2502,3089,3858,4636,5883,7375,9172,10149,12462,12462,17660,21157,24747,27980,31506,35713,41035,47021]
deaths_it = [0,1,2,3,7,10,12,17,21,29,34,52,79,107,148,197,233,366,463,631,827,827,1266,1441,1809,2158,2503,2978,3405,4032]


# confirmed = Confirmed(cumulations=[0, 1, 5, 12, 20])
# deaths_exp = TimeSeries(cumulations=[0, 0, 0.01, 0.06, 0.18])

confirmed = Confirmed(cumulations=confirmed_it)
deaths_exp = TimeSeries(cumulations=deaths_it)

deaths_as_vector = np.array(deaths_exp.cumulations[1:]).reshape(confirmed.magic_array_size, 1)
res = np.linalg.lstsq(confirmed.magic_array, deaths_as_vector, -1)
print(res[0])


# vector = MortalityVector(differences=[1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
# deaths_calc = calculate_deaths(confirmed, vector)
# mortality_as_vector = vector.calculate_aligned_cumulations(4)
# np.matmul(
#     confirmed.magic_array,
#     mortality_as_vector
# )


