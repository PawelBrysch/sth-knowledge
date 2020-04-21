import pytest

"""
musi byc `pytestmark`
"""
# pytestmark = pytest.mark.skip("all tests still WIP")
pytestmark = pytest.mark.skipif(True, reason="S3 creds not found!")

# @pytest.mark.skipif(True, reason="S3 creds not found!")
def test_func():
    assert True

# @pytest.mark.skipif(True, reason="S3 creds not found!")
class TestClass:
    def test_inside_class(self):
        assert True
