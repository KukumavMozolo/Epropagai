import numpy as np

#here are equations 26 -42
class tn1d:
    def getMuiNew(self, muiOld: float, c1:float, viOld:float) -> float: #26
        return NotImplemented
    def getViNew(self, viOld: float, c3:float)-> float: #27
        return NotImplemented
    def getPiNew(self, piOld: float, g1: float, g0:float)->float:#28
        return NotImplemented
    def getvViNew(self, viOld: float, c3: float)->float: #29
        return NotImplemented
    def getmMiNew(self, muiOld: float, c1: float, vviNew:float, viOld: float) -> float: #30
        return NotImplemented
    def getaAiNew(self, piNew: float, piOld:float)->float:#31
        return NotImplemented
    def getbBiNew(self, piNew: float, piOld: float)->float:#32
        return NotImplemented
    def getSi(self, viOld:float, vviiNew: float, c1: float, c3: float)-> float:#33 i think viiNew denotes the v comming from eq.19
        return NotImplemented

    #from after where
    def getViOld(self, vi: float, vvi) ->float: #34
        return NotImplemented
    def getMuiOld(self, mui: float, viOld: float, vvi: float, mmi: float) ->float: #35
        return NotImplemented
    def getZ(self, piOld: float, g1: float, g0: float) -> float: #36
        return NotImplemented
    def getC1(self, z: float, piOld: float, g1: float, muiOld: float, viOld: float, sigma1: float, sigma2: float)-> float: #37
        return NotImplemented
    def getC2(self, z: float, piOld: float, g1:float, g0:float, muiOld: float, viOld: float, sigma1: float, sigma2: float) -> float: #38
        return NotImplemented
    def getC3(self, c1: float, c2: float)-> float: #39
        return NotImplemented
    def getG0(self, muiOld: float, viOld: float, sigma0: float)->float: #40
        return NotImplemented
    def getG1(self, muiOld: float, viOld: float, sigma1: float)->float: #41
        return NotImplemented
    def getPiOld(self, pi: float, aai:float, bbi:float)->float: #42
        return NotImplemented

