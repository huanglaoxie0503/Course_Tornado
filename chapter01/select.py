# -*- coding: utf-8 -*-
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()


class Fetcher(object):

    def get_url(self, url):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        host = "kuaixun.stcn.com"
 
