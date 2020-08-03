#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 5:05 下午
# @Author  : lukegs7
# @File    : error_code.py
# @Software: PyCharm


SUCCESS = 0
THROW_EXP = 1000
OP_DB_FAILED = 1001
CHECK_PARAM_FAILED = 1002
FILE_FORMAT_ERR = 1003
NOT_POST = 1004
NOT_GET = 1005
CAL_FEATURE_ERR = 2001
READ_FEATURE_FAILED = 2002
TRAIN_ERR = 2003
LACK_SAMPLE = 2004

ERR_CODE = {
    SUCCESS: "操作成功",
    THROW_EXP: "抛出异常",
    OP_DB_FAILED: "数据库操作失败",
    CHECK_PARAM_FAILED: "参数检查失败",
    FILE_FORMAT_ERR: "文件格式有误",
    NOT_POST: "非post请求",
    NOT_GET: "非get请求",
    CAL_FEATURE_ERR: "特征计算出错",
    READ_FEATURE_FAILED: "读取特征数据失败",
    TRAIN_ERR: "训练出错",
    LACK_SAMPLE: "缺少正样本或负样本"
}