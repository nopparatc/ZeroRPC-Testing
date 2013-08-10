﻿import zerorpc

class ExceptionalRPC(object):
    def bad(self):
        raise Exception(":P")

s = zerorpc.Server(ExceptionalRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()