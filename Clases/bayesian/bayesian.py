import numpy as np 
import matplotlib.pyplot as plt

obs_data = np.loadtxt("obs_data.dat")
x_data = obs_data[:,0]
y_data = obs_data[:,1]

plt.scatter(x_data,y_data)

def likehood(y_obs,y_model):
	chi_squared = (1.0/2.0)