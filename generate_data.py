import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
import math
from sklearn.utils import shuffle


def GenerateGaussianData(means, stds, datapoints):
    nrClasses = len(means)
    nrFeatures = len(means[0])
    Xdata = []
    Ydata = []
    for i in range(nrClasses):
        for j in range(datapoints[i]):
            features = []
            for k in range(nrFeatures):
                features.append(np.random.normal(
                    loc=means[i][k], scale=stds[i][k], size=None))
            Xdata.append(features)
            Ydata.append(i)
    Xdata = np.array(Xdata)
    Ydata = np.array(Ydata)
    Xdata, Ydata = shuffle(Xdata, Ydata)
    return Xdata, Ydata


def gaussian_clusters(nr_features=2, nr_classes=4, nr_data_points=10):
    sigma = [np.append([1]*(nr_features//2), [0.01]
                       * (nr_features-nr_features//2))]*nr_classes
    means = np.random.normal(0, 2*10, (nr_classes, nr_features))
    dataPoints = [nr_data_points] * nr_classes
    Xdat, Ydat = GenerateGaussianData(means, sigma, dataPoints)
    return Xdat, Ydat
