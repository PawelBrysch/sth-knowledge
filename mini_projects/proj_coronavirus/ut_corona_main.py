import numpy as np
from pytest import mark
from proj_coronavirus import corona_main


class TestName:
    def test_mortality_vector(self):
        assert corona_main.TimeSeries(differences=[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]).cumulations == [1, 2, 3, 4, 4, 4, 4, 4, 4, 4]

    def test_confirmed(self):
        assert corona_main.TimeSeries(cumulations=[0, 1, 5, 12, 20]).differences == [0, 1, 4, 7, 8]

    @mark.parametrize("length, expected_as_list", [
        (3, [0.01, 0.02, 0.03]),
        (4, [0.01, 0.02, 0.03, 0.04]),
        (5, [0.01, 0.02, 0.03, 0.04, 0.04])
    ])
    def test_dimensions(self, length, expected_as_list):
        vector = corona_main.MortalityVector(differences=[1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        assert (vector.calculate_aligned_cumulations(length) == np.array(expected_as_list).reshape(length, 1)).all()