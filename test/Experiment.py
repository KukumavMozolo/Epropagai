import numpy as np
from matplotlib import pyplot as plt

from src.FeatureSelection import ExpectationPropagation


class Experiment:
    def getExampleData(self, nrPoints: int, noise = 0.0):
        x = np.random.uniform(0,1,size=(2,nrPoints))
        y = np.ones(shape=(1,nrPoints))
        y[0,np.where(x[0,:] >=0.5)] = -1
        if(noise > 0.0):
            y[0,np.random.binomial(1, noise, (1,nrPoints)).tolist()] = 1
        return x,y

    def plot(self, x:np.ndarray, y:np.ndarray):
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.scatter(x[0,:], y)
        ax1.set_title('x1 vs Y')
        ax2.scatter(x[1,:], y)
        ax2.set_title('x2 vs Y')
        plt.show()



def main():
    experiment = Experiment()
    ep = ExpectationPropagation()
    x,y = experiment.getExampleData(100,noise=0.0)
    experiment.plot(x,y)
    f = ep.run(x,y,0.5, conv_tol=0.01)
    testx, _ = experiment.getExampleData(1, noise=0.0)
    x_test  =np.array([[0.1,0],[0.2,0],[0.3,0],[0.4,0],[0.5,0],[-0.6,0],[-0.7,0],[-0.8,0],[-0.9,0]])
    x_test2  =-1.0*x_test
    y_pred = [f(x) for x in x_test]
    y_pred2 = [f(x) for x in x_test2]
    print(x_test)
    print(y_pred)
    plt.scatter(x_test[:,0],y_pred)
    plt.show()
    print(x_test2)
    print(y_pred2)
    plt.scatter(x_test2[:,0],y_pred2)
    plt.show()


if  __name__ =='__main__':main()