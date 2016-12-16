import numpy as np

from src.t0n import t0n
from src.tn1d import tn1d


class ExpectationPropagation:

    def run(self, data: np.ndarray, sparsety: float, sigma0: float = 0.000001, sigma1: float = 1.0 , iterations =-1, untilConverged= 0.0) -> np.ndarray:
        tn = t0n()
        tn1 = tn1d()
        d,n = data.shape

        mu = np.random.uniform(0.0, 1.0, size=(d)) # not sure how to initialize
        v = np.random.uniform(0.0, 1.0, size=(d))  # not sure how to initialize
        p = np.ones(shape=(d)) * sparsety


        vv = np.ones(shape=(d,n +d)) * 10000000    ## uniform initial condition of ti
        mmu = np.zeros(shape=(d,n + d))     ## uniform initial condition of ti
        s = np.zeros(shape=(n + d))
        a =  np.ones(shape=(n + d))
        b = np.ones(shape=(n + d))
        while(not self.converged(a,b, vv, mmu)):
            for i in range(n + d):
                xi = data[:,i]
                vvi = vv[:,i]
                mmi = mmu[:,i]
                if(i <=n):

                    #missing whenever likelihood is negative ignores rule


                    #where statement
                    vOld = tn.getVOld(v, vvi)
                    muOld = tn.getMuOld(mu,vOld,vvi,mmi)
                    z = tn.getZi(xi,muOld,vOld)
                    ai = tn.getAlphai(xi,vOld,z)
                    z = tn.getZi(xi,muOld,vOld)

                    muNew = tn.getMuNew(muOld,vOld,xi,ai)
                    vNew = tn.getVNew(vOld,xi,muNew,ai)
                    vviNew = tn.getvViNew(vNew,vOld)
                    mmiNew = tn.getMuNew(muOld,vOld,xi,ai)
                    si = tn.getSi(z,vviNew,vOld,mmiNew,muOld)
                else:
                    # 26 - 42
                    vi = v[i-n]
                    mui= mu[i-n]
                    pi = p[i-n]
                    aai = a[i]
                    bbi = b[i]

                    viOld = tn1.getViOld(vi, vvi)
                    muiOld = tn1.getMuiOld(mui,viOld,vvi,mmi)
                    g0 = tn1.getG0(muiOld,viOld,sigma0)
                    g1 = tn1.getG1(muiOld,viOld,sigma1)
                    piOld = tn1.getPiOld(pi,aai,bbi)
                    z = tn1.getZ(piOld,g1,g0)
                    c1 = tn1.getC1(z,piOld,g0,g1,muiOld,viOld,sigma1,sigma0)
                    c2 = tn1.getC2(z,piOld,g1,g0,muiOld,viOld,sigma1,sigma0)
                    c3 = tn1.getC3(c1,c2)

                    muiNew = tn1.getMuiNew(muiOld,c1,viOld)
                    viNew = tn1.getViNew(viOld,c3)
                    piNew = tn1.getPiNew(piOld,g1,g0)
                    vviNew = tn1.getvViNew(viOld,c3)
                    mmiNew = tn1.getmMiNew(muiOld,c1,vviNew,viOld)
                    aaiNew = tn1.getaAiNew(piNew,piOld)
                    bbiNew = tn1.getbBiNew(piNew,piOld)
                    si = tn1.getSi(z,viOld,vviNew,c1,c3)

                    a[i] = aaiNew
                    b[i] = bbiNew
                    v[i] = viNew
                    mu[i - n] = muiNew
                    p[i-n] = piNew
                vv[:,i] = vviNew
                mmu[:,i] = mmiNew
                s[i] = si




    def converged(self, tiOld:np.ndarray, tiNew: np.ndarray) -> bool:
        return NotImplemented







    #Here are Methods for equation 26 - 42
