#!/usr/bin/env python
#coding: utf8

"""
    协议希望可以兼容 HTTP / RPC
"""


class Request(object):
    """
        表示对请求体的抽象，类似一个标准的HTTP Request
    """
    pass


class Response(object):
    """
        表示返回体的抽象
    """


class Client(object):
    def make_request(self, req: Request) -> Response:
        pass
