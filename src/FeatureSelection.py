import numpy as np

from src.t0n import t0n


class ExpectationPropagation:

    def run(self, data: np.ndarray, iterations =-1, untilConverged= True) -> np.ndarray:
        tn = t0n()
        d,n = data.shape
        tiNew = np.ones(n+1)
        tiOld = np.zeros(n+1)

        mu = np.random.uniform(0.0, 1.0, size=(d,)) # not sure how to initialize
        v = np.random.uniform(0.0, 1.0, size=(d,))  # not sure how to initialize

        vv = np.ones(shape=(d,n)) * 10000000    ## uniform initial condition of ti
        mmu = np.zeros(0.0,1.0, size=(d,n))     ## uniform initial condition of ti
        while(not self.converged(tiOld, tiNew)):
            for i in range(n):
                xi = data[:,i]
                vi = vv[:,i]
                mui = mmu[:,i]
                vOld = tn.getVOld(v, vi)
                muOld = tn.getMuOld(mu,vOld,vi,mui)
                z = tn.getZi(xi,muOld,vOld)
                ai = tn.getAlphai(xi,vOld,z)

                muNew = tn.getMuNew(muOld,vOld,xi,ai)
                vNew = tn.getVNew(vOld,xi,muNew,ai)
                vviNew = tn.getvViNew(vNew,vOld)
                miNew = tn.getMuNew(muOld,vOld,xi,ai)



                mu = muNew
                v = vNew

    def converged(self, tiOld:np.ndarray, tiNew: np.ndarray) -> bool:
        return NotImplemented




    #Here are Methods for equation 26 - 42
