#!/usr/bin/env python
#coding: utf8

class QueueBase(object):
    """
        用来收集测试用例,From case generator
    """
    def __init__(self):
        self._size = 0

    def get(self):
        """
            阻塞调用
        """
        pass

    def put(self):
        """
            阻塞调用
        """
        pass
