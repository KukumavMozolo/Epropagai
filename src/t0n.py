import numpy as np


# Here are Methods for equation 17 - 21
class t0n:

    def getMuNew(self, muOld: np.ndarray, vOld: np.ndarray, xi: np.ndarray, ai: float) -> np.ndarray: #17
        return NotImplemented


    def getVNew(self, vOld: np.ndarray, xi: np.ndarray, muNew: np.ndarray, ai: float): #18
        return NotImplemented


    def getvViNew(self, vNew: np.ndarray, vOld: np.ndarray) -> np.ndarray:#19
        return NotImplemented


    def getMiNew(self, muOld: np.ndarray, viNew: np.ndarray, xi: np.ndarray, viOld: np.ndarray, ai: float) -> np.ndarray:#20
        return NotImplemented


    def getSi(self, viNew: np.ndarray, vOld: np.ndarray, miNew: np.ndarray, muOld: np.ndarray) -> float:#21
        return NotImplemented


    #after where statement

    def getvOld(self, v: np.ndarray, vi: np.ndarray) -> np.ndarray: #22
        return NotImplemented


    def getMuOld(self, mu: np.ndarray, vOld: np.ndarray, vi: np.ndarray, mi: np.ndarray) -> np.ndarray:#23
        return NotImplemented


    def getAlphai(self, xi: np.ndarray, vOld: np.ndarray, z: float) -> float: #24
        return NotImplemented


    def getZi(self, xi: np.ndarray, muOld: np.ndarray, vOld: np.ndarray) -> float: #25
        return NotImplemented