"""#######################################
Jak zmockowac generator (przeciez nie ma `return`).
#######################################"""
from unittest.mock import patch
from clesson_mock_generator.source import wrapper

with patch("clesson_mock_generator.source.some_generator", return_value=iter([1, 2, 3])) as gen_mck:
    wrapper()

