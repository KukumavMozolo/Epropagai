import numpy as np
from scipy.stats import norm

#here are equations 26 -42
class tn1d:
    def getMuiNew(self, muiOld: float, c1:float, viOld:float) -> float: #26
        return muiOld + c1*viOld

    def getViNew(self, viOld: float, c3:float)-> float: #27
        return viOld - c3 *np.power(viOld,2)

    def getPiNew(self, piOld: float, g1: float, g0:float)->float:#28
        return piOld*g1/(piOld*g1 + (1.0-piOld)*g0)

    def getvViNew(self, viOld: float, c3: float)->float: #29
        return np.reciprocal(c3) - viOld

    def getmMiNew(self, muiOld: float, c1: float, vviNew:float, viOld: float) -> float: #30
        return muiOld + c1*(vviNew + viOld)

    def getaAiNew(self, piNew: float, piOld:float)->float:#31
        return piNew/piOld

    def getbBiNew(self, piNew: float, piOld: float)->float:#32
        return (1.0 - piNew)/(1.0 - piOld)

    def getSi(self, z: float, viOld:float, vviiNew: float, c1: float, c3: float)-> float:#33 i think viiNew denotes the v comming from eq.19
        return z * np.sqrt((viOld +vviiNew)/vviiNew) * np.exp(0.5 * np.power(c1,2)/c3 )

    #from after where
    def getViOld(self, vi: float, vvi) ->float: #34
        return np.reciprocal(np.reciprocal(vi) - np.reciprocal(vvi))

    def getMuiOld(self, mui: float, viOld: float, vvi: float, mmi: float) ->float: #35
        return mui + viOld *np.reciprocal(vvi) * (mui - mmi)

    def getZ(self, piOld: float, g1: float, g0: float) -> float: #36
        return piOld * g1 + (1.0 - piOld)*g0

    def getC1(self, z: float, piOld: float, g0:float, g1: float, muiOld: float, viOld: float, sigma1: float, sigma0: float)-> float: #37
        return np.reciprocal(z)  *(piOld*g1 *(-muiOld)/(viOld + np.power(sigma1,2)) + (1.0-piOld) *g0 * (-muiOld)/(viOld + np.power(sigma0,2)))

    def getC2(self, z: float, piOld: float, g1:float, g0:float, muiOld: float, viOld: float, sigma1: float, sigma0: float) -> float: #38
        def helper(muiOld: float, viOld: float, sigma: float):
            return np.power(muiOld, 2) / np.power(viOld + np.power(sigma,2), 2) - 1.0/(viOld + np.power(sigma,2))

        return np.reciprocal(z) * 0.5 * (piOld*g1*helper(muiOld, viOld, sigma1) + (1.0 -piOld) * g0 * helper(muiOld, viOld, sigma0))

    def getC3(self, c1: float, c2: float)-> float: #39
        return np.power(c1,2) - 2.0*c2

    def getG0(self, muiOld: float, viOld: float, sigma0: float)->float: #40
        return norm.pdf(0.0, muiOld, viOld + np.power(sigma0,2))

    def getG1(self, muiOld: float, viOld: float, sigma1: float)->float: #41
        return norm.pdf(0.0, muiOld, viOld + np.power(sigma1,2))

    def getPiOld(self, pi: float, aai:float, bbi:float)->float: #42
        return (pi/aai)/(pi/aai + (1.0 -pi)/bbi)

