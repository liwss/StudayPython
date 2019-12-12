# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2019/9/20 10:02
# @describe : 


import logging
import logstash
import sys


test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.DEBUG)
test_logger.addHandler(logstash.TCPLogstashHandler('172.18.231.67', 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 2, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}

test_logger.info('python-logstash: test extra fields', extra=extra)
