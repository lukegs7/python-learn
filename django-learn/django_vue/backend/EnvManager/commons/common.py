#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 5:05 下午
# @Author  : lukegs7
# @File    : common.py
# @Software: PyCharm

import traceback
from functools import wraps
from commons.error_code import *
from commons.custom_response import CustomResponse


def rest_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            res = CustomResponse({'code': SUCCESS, 'msg': 'success', 'data': data})
        except Exception as ex:
            traceback.print_exc()
            res = CustomResponse({'code': THROW_EXP, 'msg': str(ex), 'data': ''})
        return res

    return wrapper
