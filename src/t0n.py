import numpy as np
from scipy.stats import norm

# Here are Methods for equation 17 - 21
class t0n:

    def getMuNew(self, muOld: np.ndarray, vOld: np.ndarray, xi: np.ndarray, ai: float) -> np.ndarray: #17
        return muOld + ai* np.multiply(vOld, xi)

    def getVNew(self, vOld: np.ndarray, xi: np.ndarray, muNew: np.ndarray, ai: float): #18
        return vOld - ai * (np.dot(xi,muNew) + ai)/(np.dot(xi,np.multiply(vOld,xi)) +1.0) * np.multiply(vOld, xi) * np.multiply(vOld,xi)

    def getvViNew(self, vNew: np.ndarray, vOld: np.ndarray) -> np.ndarray:#19
        return np.reciprocal(np.reciprocal(vNew) - np.reciprocal(vOld))

    def getMiNew(self, muOld: np.ndarray, viNew: np.ndarray, xi: np.ndarray, viOld: np.ndarray, ai: float) -> np.ndarray:#20
        return muOld + ai*np.multiply(viNew, xi) + ai * np.multiply(viOld, xi)

    def getSi(self, z:float, viNew: np.ndarray, vOld: np.ndarray, miNew: np.ndarray, muOld: np.ndarray) -> float:#21
        #not sure about this
        return norm.cdf(z) * np.prod(np.sqrt(np.divide(viNew + vOld, viNew))) * np.exp(np.sum(np.divide(np.power(miNew - muOld,2), 2 *(vOld + viNew))))


    #after where statement

    def getVOld(self, v: np.ndarray, vi: np.ndarray) -> np.ndarray: #22
        return np.reciprocal(np.reciprocal(v) - np.reciprocal(vi))

    def getMuOld(self, mu: np.ndarray, vOld: np.ndarray, vi: np.ndarray, mi: np.ndarray) -> np.ndarray:#23
        return mu + np.multiply(vOld, np.multiply(np.reciprocal(vi), mu-mi))

    def getAlphai(self, xi: np.ndarray, vOld: np.ndarray, z: float) -> float: #24
        #maybe norm requires params?
        return 1.0/np.sqrt(np.dot(xi,np.multiply(vOld,xi)) +1) * norm.pdf(z)/norm.cdf(z)

    def getZi(self, xi: np.ndarray, muOld: np.ndarray, vOld: np.ndarray) -> float: #25
        return np.dot(xi,muOld)/np.sqrt(np.dot(xi, np.multiply(vOld,xi)) +1.0)
