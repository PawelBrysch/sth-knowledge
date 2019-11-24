'''######################
side_effect vs return_value
######################'''
'''
Jak to dziala?                                                  side_effect przeslania niezaleznie od kolejnosci dodania
'''

from LESSON_pytest.lesson_mock.draft2_src import some_func

@patch("core.base.log.Log.TestEquipment._files_filter_with_versions", side_effect=[{}, {}]):
    pass



