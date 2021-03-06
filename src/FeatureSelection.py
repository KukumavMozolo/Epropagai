import numpy as np
from scipy.stats import norm

from src.t0n import t0n
from src.tn1d import tn1d


class ExpectationPropagation:

    def run(self, x: np.ndarray, y: np.ndarray, sparsety: float, sigma0: float = 0.00000000000001, sigma1: float = 1.0, iterations =-1, conv_tol= 0.00001) -> np.ndarray:
        xshape = x.shape
        yshape = y.shape
        assert xshape[1] == yshape[1], "x and y have different sample dimensions, x.shape = " + str(xshape)  + " y.shape = " + str(yshape)
        assert y.shape[0] == 1, "y should be one dimensional"
        x = np.multiply(x,y)
        assert sparsety <1.0, "sparsety should be inbetween 0 and 1"
        assert sparsety >0.0, "sparsety should be inbetween 0 and 1"
        tn = t0n()
        tn1 = tn1d()
        d,n = x.shape

        self.iterationCounter = 0
        max = 9999999999

        self.mu = np.random.uniform(0.0, 1.0, size=(d))#np.zeros(shape=(d)) # not sure how to initialize
        self.v = np.random.uniform(0.0, 1.0, size=(d))#  # not sure how to initialize
        self.p = np.ones(shape=(d)) * sparsety

        ## uniform initial condition of ti
        self.s = np.zeros(shape=(n + d))
        self.a =  np.ones(shape=(d,n + d))
        self.b = np.ones(shape=(d,n + d))
        self.vv = np.ones(shape=(d,n +d)) * max
        self.mmu = np.zeros(shape=(d,n + d))

        #these are only for convergence checking
        self.a_c =  np.ones(shape=(n + d)) * max
        self.b_c = np.ones(shape=(n + d))
        self.vv_c = np.ones(shape=(d,n +d)) * max
        self.mmu_c = np.zeros(shape=(d,n + d))
        self.mu_c = np.random.uniform(0.0, 1.0, size=(d))#np.zeros(shape=(d)) # not sure how to initialize
        self.v_c = np.random.uniform(0.0, 1.0, size=(d))#  # not sure how to initialize
        self.p_c = np.ones(shape=(d)) * sparsety
        while(self.notConverged2(conv_tol)):
            for i in range(n + d):  #refine approximation of ti
                self.iterationCounter += 1
                xi = x[:,np.random.random_integers(0,n-1)]
                # xi = x[:, i%n]
                if(np.sum(np.abs(xi)) == 0):
                    continue
                vvi = self.vv[:,i]
                mmi = self.mmu[:,i]
                if(i <n): #the likelihoods

                    #where statement
                    vOld = tn.getVOld(self.v, vvi)
                    if(np.where(vOld <0)[0].shape[0] >0): #whenever likelihood is negative ignore rule
                        continue
                    muOld = tn.getMuOld(self.mu,vOld,vvi,mmi)
                    z = tn.getZi(xi,muOld,vOld)
                    ai = tn.getAlphai(xi,vOld,z)

                    muNew = tn.getMuNew(muOld,vOld,xi,ai)
                    vNew = tn.getVNew(vOld,xi,muNew,ai)
                    vviNew = tn.getvViNew(vNew,vOld)
                    mmiNew = tn.getMiNew(muOld,vviNew,xi,vOld,ai)
                    si = tn.getSi(z,vviNew,vOld,mmiNew,muOld)
                    #i think one can conclude that we should update only these(17-21)
                    self.vv[:, i] = vviNew
                    self.mmu[:, i] = mmiNew
                    self.mu = muNew
                    self.v = vNew
                else: #the priors
                    # 26 - 42
                    vi = self.v[i-n]         #mentioned in eq.34. what is it?
                    mui= self.mu[i-n]        # so is this in eq.35. what is it?
                    pi = self.p[i-n]         #same here eq. 42 what is it?
                    aai = self.a[:,i]
                    bbi = self.b[:,i]
                    print(aai)

                    viOld = tn1.getViOld(vi, vvi[i-n])
                    muiOld = tn1.getMuiOld(mui,viOld,vvi[i-n],mmi[i-n])
                    g0 = tn1.getG0(muiOld,viOld,sigma0)
                    g1 = tn1.getG1(muiOld,viOld,sigma1)
                    piOld = np.prod(np.multiply(np.power(sparsety,self.p) , (1.0-np.power(sparsety,self.p))))# what was proposed in mail
                    # piOld = tn1.getPiOld(pi, aai[i - n], bbi[i - n]) # what is written in paper
                    z = tn1.getZ(piOld,g1,g0)
                    c1 = tn1.getC1(z,piOld,g0,g1,muiOld,viOld,sigma1,sigma0)
                    c2 = tn1.getC2(z,piOld,g1,g0,muiOld,viOld,sigma1,sigma0)
                    c3 = tn1.getC3(c1,c2)

                    muiNew = tn1.getMuiNew(muiOld,c1,viOld)
                    viNew = tn1.getViNew(viOld,c3)
                    piNew = tn1.getPiNew(piOld,g1,g0)
                    vvniiNew = tn1.getvViNew(viOld,c3)
                    mmniiNew = tn1.getmMiNew(muiOld,c1,vvniiNew,viOld)
                    aaniiNew = tn1.getaAiNew(piNew,piOld)
                    bbniiNew = tn1.getbBiNew(piNew,piOld)
                    si = tn1.getSi(z,viOld,vvniiNew,c1,c3) #unsure

                    #and here we should update only these (26 - 33)
                    self.a[i - n,i] = aaniiNew
                    self.b[i - n,i] = bbniiNew
                    self.vv[i - n,i] = vvniiNew
                    self.mmu[i - n,i]= mmniiNew
                    self.v[i - n] = viNew
                    self.mu[i - n] = muiNew
                    self.p[i-n] = piNew


                self.s[i] = si
        print("the algorithm took " + str(self.iterationCounter) + " iterations to converge!")
        def f(x) : return (norm.cdf(np.dot(x.T, self.mu)/np.sqrt(np.dot(x.T,np.multiply(self.v,x.T).T) +1.0)) -
                                  norm.cdf(
                                      np.dot(-x.T, self.mu) / np.sqrt(np.dot(-x.T, np.multiply(self.v, -x.T).T) + 1.0)) -0.5)
        return f




    def notConverged(self, conv_tol) -> bool:
        d, n = self.a.shape
        delta = np.sum(np.abs(self.a-self.a_c)) \
                + np.sum(np.abs(self.b-self.b_c))\
                + np.sum(np.abs(self.vv-self.vv_c))\
                + np.sum(np.abs(self.mmu-self.mmu_c))
        # delta /= d * n * 4
        print("Parameter difference is " + str(delta) +" at iteration " + str(self.iterationCounter))

        if(delta > conv_tol):
            self.a_c = self.a.copy()
            self.b_c = self.b.copy()
            self.vv_c = self.vv.copy()
            self.mmu_c = self.mmu.copy()
            return True
        return False

    def notConverged2(self, conv_tol) -> bool:
        d, n = self.a.shape
        delta = np.sum(np.abs(self.v - self.v_c)) \
                + np.sum(np.abs(self.mu - self.mu_c)) \
                + np.sum(np.abs(self.p - self.p_c))
        # delta /= d * n * 4
        print("Parameter difference is " + str(delta) + " at iteration " + str(self.iterationCounter))

        if (delta > conv_tol):
            self.v_c = self.v.copy()
            self.mu_c = self.mu.copy()
            self.p_c = self.p.copy()
            return True
        return False




    #Here are Methods for equation 26 - 42
