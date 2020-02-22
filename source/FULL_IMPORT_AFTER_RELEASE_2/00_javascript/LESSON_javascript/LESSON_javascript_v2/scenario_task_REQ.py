# -*- encoding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Author:  Pawel Brysch
# E-mail:  pawel.brysch@zf.com
# Company: ZF TRW
# Created: 04.09.2019
# ----------------------------------------------------------------------------------------------------------------------
# This  copyrighted  document is the  property of ZF Friedrichshafen AG and its affiliates, including ZF TRW Automotive
# Holdings Corp. and its subsidiary  companies ("ZF").  This document and the information contained herein is disclosed
# in  confidence  and  may  not be  copied, disclosed to  others, or  used  for any  purpose  unless  authorized  by ZF.
# This  document must  be returned  to ZF upon request  and  may not  be  stored in any  database  or retrieval  system.
#                                     © ZF Friedrichshafen AG 2019.
# ----------------------------------------------------------------------------------------------------------------------

from core.base.config import Path
from core.base.test_runner import TestRunner
from core.base.log import Log

Log.UUT.sw_version = 'SW version'
Log.UUT.hw_version = 'HW version'
Log.UUT.hw_part_number = 'HW part number'
Log.UUT.serial_number = 'Serial number'


TestRunner.execute_test_case(rf"{Path.TEST_CASES}\task_req\tc_101.py")
TestRunner.execute_test_case(rf"{Path.TEST_CASES}\task_req\tc_102.py")
TestRunner.execute_test_case(rf"{Path.TEST_CASES}\task_req\tc_103.py")



