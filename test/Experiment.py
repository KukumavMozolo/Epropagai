import numpy as np
from matplotlib import pyplot as plt

from src.FeatureSelection import ExpectationPropagation


class Experiment:
    def __init__(self):
        pass

    def getExampleData(self, nrPoints: int, noise = 0.0):
        x = np.random.uniform(0,10,size=(2,nrPoints))
        y = np.ones(shape=(1,nrPoints))
        y[0,np.where(x[0,:] <=5.0)] = 0
        if(noise > 0.0):
            y[0,np.random.binomial(1, noise, (1,nrPoints)).tolist()] = 1
        return x,y

    def plot(self, x:np.ndarray, y:np.ndarray):
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.scatter(x[0,:], y)
        ax1.set_title('Sharing Y axis')
        ax2.scatter(x[1,:], y)
        plt.show()



def main():
    experiment = Experiment()
    ep = ExpectationPropagation()
    x,y = experiment.getExampleData(50,noise=0.8)
    ep.run(x,y,0.5, conv_tol=0.0001)
    experiment.plot(x,y)


if  __name__ =='__main__':main()