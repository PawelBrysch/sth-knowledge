''' ###################################
IMPORTS
####################################'''
# from core.base.log import Log
# from core.base.utilities import screenshot


''' ###################################
STOP 
####################################'''
# from core.base.exceptions import StopTestCase, StopScenario, StopExecution
#
# raise StopTestCase
# raise StopScenario
# raise StopExecution


''' ###################################
LOG
####################################'''
''' console printing level '''
# from core.base.config import LogConfig
# LogConfig.CONSOLE_PRINTING_LEVEL = 0
'''A) tc level'''
# from core.base.log import Log
#
# Log.step("Step 1")
# Log.step("Step 1.1", level=2)
#
# Log.comment("Field_1", "Field_2.")
# Log.step_status(status="pass",
#         header="CAN Message Transmission",
#         details=("An exception occurred", "Unexpected CAN message received", "Exception traceback"),
#         expected=("CAN message", "message id: 4"),
#         received=("CAN message", "message id: 3"))
'''B) module level'''
# from core.base.log import Log
#
# def log_sth_used_many_times():
#     with Log.Command(name="command name") as cmd:
#         cmd.details("some details")
#         cmd.received("CAN message", "message id:", 3)


''' ###################################
TYPE CHECKING
####################################'''
'''
1. na jakim poziomie uzywac tych funkcji?->                                                                 module level
2. jak używać?->                                                                                     if not func: return
'''
# from core.base.parameter_check import validate_file_extension, validate_length, validate_value, validate_range, relation, make_or, validate_type
#
# validate_type(parameter_name="sth", parameter_value=3.1, allowed_types=[int])
# validate_value(parameter_name="sth", parameter_value=31, allowed_parameter_values=[32])
# validate_file_extension(file_path_name="sth", file_path_value=r"C:\scripts\wpcp.bat", allowed_extensions=[".bat"])
# validate_length(parameter_name="sth", parameter_value=[1, 0, 0, 1, 0, 1, 0, 1, 1], allowed_lengths=(8, 16, 32))
# validate_range(parameter_name="sth", parameter_value=2, allowed_min=3.0, allowed_max=5.0)
# relation(parameter1_name="sth1", parameter1_value=11, allowed_operator="in", parameter2_name="sth2", parameter2_value=[4, 5, 8, 10, 16, 20])
# make_or(method1=validate_type, parameters1=("sth", (2, 3), [list]), method2=validate_length, parameters2=("sth", [1, 2, 3], (2, 4)))
''' type checker '''
# from core.base.parameter_check import type_checker
# from typing import Union
#
# @type_checker
# def some_func(arg1: Union[float, int], arg2: Union[float, int]):
#     pass

''' ###################################
SPECIAL LOG METHODS
####################################'''
# from core.base.log import Log
# import random
#
# def log_table():
#     with Log.Command(name="Waiting for measurement stop") as cmd:
#         first_row = ["col1", "col2", "col3", "col4"]
#         second_row = [str(4), str(9), str(16), str(25)]
#         cmd.table(data=[first_row, second_row], html_color="00FFFF")
#
#
# def log_image():
#     '''
#     hide/excluded znaczenie-> czasami wrzuci do htmla, czasami nie (zalezy od kombinacji)
#     '''
#     with Log.Command(name="Waiting for measurement stop") as cmd:
#         cmd.image(file_path=r"C:\\Users\\BryschP\\Desktop\\image-de-loup-6.jpg", caption="Snapshot from front camera",
#                           hide=False, included=True)
#
#
# def log_plot():
#     with Log.Command(name="Some command") as cmd:
#         cmd.plot(data={'signal_0':  [random.randint(0, 10) for i in range(10)],
#                        'signal_1':  [random.randint(0, 10) for i in range(10)],
#                        'signal_2': [random.randint(0, 10) for i in range(10)]},
#                  plot_steps=list(range(10)),
#                  x_axis_title='sth_x',
#                  y_axis_title='sth_y',
#                  caption='sth_cap',
#                  set_type=Log.Command.PlotTypes.NORMAL)
#
#
# def log_link_to_files():
#
#     with Log.Command(name="some command") as cmd:
#         cmd.link(caption="Link to web",
#                          link=r"//pl.wikipedia.org/wiki/Pomidor",
#                          protocol=Log.Command.Protocols.HTTP)
#
#         cmd.link(caption="Local to local machine",
#                          link="C:\\Users\\BryschP\\Desktop\\image-de-loup-6.jpg",
#                          protocol=Log.Command.Protocols.FILE)
#
#
# def log_tci():
#     with Log.tci("TC_test_coverage_item_002_001",
#                  "REQUIREMENT_999",
#                  "Drive straight and check availability of systems.",
#                  parameter1=True,
#                  parameter2=100):
#         pass


''' ###################################
CANOE
####################################'''
'''
1. gdzie ma byc baza .dbc?->                                                                         generators\\outputs
'''
# from core.base.test_functions import set_value, check_value
# from generators.outputs import tmp_dbc_dbc
# from core.vector.canoe import CANoe
# from core.vector.v_base import LogFormat
# # #Start app
# canoe = CANoe()
# canoe.open_application()
# canoe.start_measurement()
# # #Create log (?)
# canoe.start_log(log_name="test", folder="test_folder", log_format=LogFormat.ASC)
# # #Useful methods
# canoe.set_signal_value(tmp_dbc_dbc.Msg1.Sig1, 40)
# my_signal_val = canoe.signal_read_var(channel=0, msg_name=tmp_dbc_dbc.Msg1.name, sig_name=tmp_dbc_dbc.Msg1.Sig1.name)[0]
# check_value(given_value=my_signal_val, expected_relation=">=", expected_value=40.0)
# canoe.signal_write_var(channel=0, msg_name=tmp_dbc_dbc.Msg1.name, sig_name=tmp_dbc_dbc.Msg1.Sig1.name, value=1)