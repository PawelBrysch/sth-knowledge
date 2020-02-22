var dataSource = {
  testcase: {
    0: {
      'expanded': 'all',
      'pinned': 'False',
      'status': 'pass',
      'has_warning': 'false',
      'header': {
        'Identifier': 'tc_screenshot_001',
        'Objective': 'Takes all possible screenshots.',
        'Priority': 'High',
        'Traceability': '',
        'Test Method': '["Analysis of interfaces"]',
        'Type': 'Automated test',
        'Test Environment': 'Connected display'
      },
      'uut': {
        'Sw version': 'SW version',
        'Hw version': 'HW version',
        'Hw part number': 'HW part number',
        'Serial number': 'Serial number'
      },
      'content': [{
        'tag': 'requirements',
        'content': ['req_111', 'req_222', 'req_3333', 'req_123456', 'req_988654321', 'req_777777']
      }, {'tag': 'section', 'name': 'Precondition'}, {'tag': 'step', 'name': 'Power ON', 'tab': '1'}, {
        'tag': 'command',
        'name': 'Vision mode',
        'status': 'pass',
        'content': [{'tag': 'details', 'content': ['Vision ON']}],
        'time': '0.012033',
        'relative_time': '0.002006'
      }, {'tag': 'section', 'name': 'Action'}, {'tag': 'section', 'name': 'End condition'}]
    }, length: 1
  },
  teardown: {length: 0}
};

// var testcaseListForFilters = [{
//   'id': 0,
//   'active': true,
//   'status': ['pass', false],
//   'pinned': false,
//   'values': ['tc_screenshot_001', 'Takes all possible screenshots.', 'req_111', 'req_222', 'req_3333', 'req_123456', 'req_988654321', 'req_777777'
//   ],
//   'markup': "<li id='testcase_li_0' class='testcase_border testcase_height testcase-click-pass' onclick='createDetailedView(\"testcase\",0)'><div class='boxes'><div class='pin_box'></div><div class='test_size testcase_element text_center font_bold_17px color_white test_border_gray test_green'></div><div class='testcase_element test_size '></div></div><div class='testcase_element'><div class='testcase_button'>1</div></div><div class='testcase_text_title long_text searchThat '>tc_screenshot_001</div><div class='testcase_text_subtitle long_text searchThat'>Takes all possible screenshots.</div><div class='float_right'><div class='testcase_req long_text searchThat' onmouseover=\"setTitle(this,['req_111', 'req_222', 'req_3333', 'req_123456', 'req_988654321', 'req_777777'])\">req_111, req_222, req_3333, req_123456, req_988654321, req_777777</div></div></li>"
// },];
// var testCasesIdDict = {tc_screenshot_001: "testcase_li_0",};


var testcaseListForFilters = [{
  'id': 0,
  'active': true,
  'status': ['pass', false],
  'pinned': false,
  'values': ['tc_screenshot_001', 'Takes all possible screenshots.', 'req_111', 'req_222', 'req_3333', 'req_123456', 'req_988654321', 'req_777777'
  ],
  'markup': "<li id='testcase_li_0' class='testcase_border testcase_height testcase-click-pass' onclick='createDetailedView(\"testcase\",0)'><div class='boxes'><div class='pin_box'></div><div class='test_size testcase_element text_center font_bold_17px color_white test_border_gray test_green'></div><div class='testcase_element test_size '></div></div><div class='testcase_element'><div class='testcase_button'>1</div></div><div class='testcase_text_title long_text searchThat '>tc_screenshot_001</div><div class='testcase_text_subtitle long_text searchThat'>Takes all possible screenshots.</div><div class='float_right'><div class='testcase_req long_text searchThat' onmouseover=\"setTitle(this,['req_111', 'req_222', 'req_3333', 'req_123456', 'req_988654321', 'req_777777'])\">req_111, req_222, req_3333, req_123456, req_988654321, req_777777</div></div></li>"
}, {
  'id': 1,
  'active': true,
  'status': ['pass', false],
  'pinned': false,
  'values': ['tc_screenshot_001', 'Takes all possible screenshots.', 'req_101', 'req_010'
  ],
  'markup': "<li id='testcase_li_1' class='testcase_border testcase_height testcase-click-pass' onclick='createDetailedView(\"testcase\",1)'><div class='boxes'><div class='pin_box'></div><div class='test_size testcase_element text_center font_bold_17px color_white test_border_gray test_green'></div><div class='testcase_element test_size '></div></div><div class='testcase_element'><div class='testcase_button'>2</div></div><div class='testcase_text_title long_text searchThat '>tc_screenshot_001</div><div class='testcase_text_subtitle long_text searchThat'>Takes all possible screenshots.</div><div class='float_right'><div class='testcase_req long_text searchThat' onmouseover=\"setTitle(this,['req_101', 'req_010'])\">req_101, req_010</div></div></li>"
},];
var testCasesIdDict = {tc_screenshot_001: "testcase_li_0", tc_screenshot_001: "testcase_li_1",};
