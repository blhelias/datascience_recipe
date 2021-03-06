import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from KMeans import KMeans
from Regression import LinReg, LogReg, MultiReg
from ACP import PCA_scratch
#sklearn
from sklearn.linear_model import LinearRegression


#################################### PATH VARIABLES #####################################
#========================================================================================
# DATA_PATH = "C:\\Users\\brieuc.lhelias\\Desktop\\workspace\\datascience_recipe\\data"
DATA_PATH = "C:\\Users\\brieu\\Desktop\\workspace\\machine learning from scratch\\10_algos_from_scratch\\data\\"
#========================================================================================
#########################################################################################

def load_kmeans_data():
    """
    charger le dataset data_1024.csv()
    """
    data = pd.read_csv(os.path.join(DATA_PATH, 'data_1024.csv'), sep='\t')
    del data['Driver_ID']
    mean = data.mean(axis=0)
    data -= mean
    std = data.std(axis=0)
    data /= std
    return data.values

if __name__ == "__main__":
    #######################################
    # KMEANS
    #######################################
    X = load_kmeans_data()
#    instantiate KMeans class
    k_means = KMeans(K_clusters=4,
                     threshold=0.001,
                     n_iters = 1000,
                     initialization="forgy")
#    kmeans training
    k_means.fit(X)
    k_means.plot_training_history(X)
    #######################################
    # Simple Linear Regression
    #######################################
    # 1 - chargement du dataset
    data = pd.read_table(os.path.join(DATA_PATH, "data.txt"),sep="\t",header=None)
    x = np.array(data[0])
    y = np.array(data[1])
    # 2 - regression descente de gradient
    lin_reg_grad = LinReg(method="gradient_descent")
    # train liner regression model gradient descent
    lin_reg_grad.fit(x, y)
    print("linear_regression", lin_reg_grad.coefs)
    # Subplot comparison
    fig, (ax0, ax1) = plt.subplots(ncols=2, constrained_layout=True)

    ax0.set_title("our linear regression")
    ax0.scatter(x, y, c="red", s=100, edgecolor="black", alpha=0.5)
    ablines_values_ = [lin_reg_grad.coefs[1] * i + lin_reg_grad.coefs[0] for i in x]
    ax0.plot(x, ablines_values_)

    #4 - regression Scikit-Learn
    regr = LinearRegression(fit_intercept=True)    
    # Train the model using the training sets
    x_sk = x.reshape((100,1))
    y_sk = y.reshape((100,1))
    
    regr.fit(x_sk, y_sk)

    b = regr.intercept_[0]
    m = regr.coef_[0][0]
    ax1.set_title("sklearn linear regression")
    ax1.scatter(x, y, c="orange", edgecolor="black", s=100, alpha=0.5)
    ablines_values = [m * i + b for i in x]
    ax1.plot(x, ablines_values)
    plt.show()

    lin_reg_grad.plot_history(x, y)
    #######################################
    # Multiple Linear Regression
    #######################################
    x = np.c_[np.ones(len(x)), x]
    multi_reg = MultiReg(1e-4)
    multi_reg.fit(x, y)
    print(multi_reg.beta)

    x = [[1,49,4,0],[1,41,9,0],[1,40,8,0],[1,25,6,0],[1,21,1,0],[1,21,0,0],[1,19,3,0],[1,19,0,0],[1,18,9,0],[1,18,8,0],[1,16,4,0],[1,15,3,0],[1,15,0,0],[1,15,2,0],[1,15,7,0],[1,14,0,0],[1,14,1,0],[1,13,1,0],[1,13,7,0],[1,13,4,0],[1,13,2,0],[1,12,5,0],[1,12,0,0],[1,11,9,0],[1,10,9,0],[1,10,1,0],[1,10,1,0],[1,10,7,0],[1,10,9,0],[1,10,1,0],[1,10,6,0],[1,10,6,0],[1,10,8,0],[1,10,10,0],[1,10,6,0],[1,10,0,0],[1,10,5,0],[1,10,3,0],[1,10,4,0],[1,9,9,0],[1,9,9,0],[1,9,0,0],[1,9,0,0],[1,9,6,0],[1,9,10,0],[1,9,8,0],[1,9,5,0],[1,9,2,0],[1,9,9,0],[1,9,10,0],[1,9,7,0],[1,9,2,0],[1,9,0,0],[1,9,4,0],[1,9,6,0],[1,9,4,0],[1,9,7,0],[1,8,3,0],[1,8,2,0],[1,8,4,0],[1,8,9,0],[1,8,2,0],[1,8,3,0],[1,8,5,0],[1,8,8,0],[1,8,0,0],[1,8,9,0],[1,8,10,0],[1,8,5,0],[1,8,5,0],[1,7,5,0],[1,7,5,0],[1,7,0,0],[1,7,2,0],[1,7,8,0],[1,7,10,0],[1,7,5,0],[1,7,3,0],[1,7,3,0],[1,7,6,0],[1,7,7,0],[1,7,7,0],[1,7,9,0],[1,7,3,0],[1,7,8,0],[1,6,4,0],[1,6,6,0],[1,6,4,0],[1,6,9,0],[1,6,0,0],[1,6,1,0],[1,6,4,0],[1,6,1,0],[1,6,0,0],[1,6,7,0],[1,6,0,0],[1,6,8,0],[1,6,4,0],[1,6,2,1],[1,6,1,1],[1,6,3,1],[1,6,6,1],[1,6,4,1],[1,6,4,1],[1,6,1,1],[1,6,3,1],[1,6,4,1],[1,5,1,1],[1,5,9,1],[1,5,4,1],[1,5,6,1],[1,5,4,1],[1,5,4,1],[1,5,10,1],[1,5,5,1],[1,5,2,1],[1,5,4,1],[1,5,4,1],[1,5,9,1],[1,5,3,1],[1,5,10,1],[1,5,2,1],[1,5,2,1],[1,5,9,1],[1,4,8,1],[1,4,6,1],[1,4,0,1],[1,4,10,1],[1,4,5,1],[1,4,10,1],[1,4,9,1],[1,4,1,1],[1,4,4,1],[1,4,4,1],[1,4,0,1],[1,4,3,1],[1,4,1,1],[1,4,3,1],[1,4,2,1],[1,4,4,1],[1,4,4,1],[1,4,8,1],[1,4,2,1],[1,4,4,1],[1,3,2,1],[1,3,6,1],[1,3,4,1],[1,3,7,1],[1,3,4,1],[1,3,1,1],[1,3,10,1],[1,3,3,1],[1,3,4,1],[1,3,7,1],[1,3,5,1],[1,3,6,1],[1,3,1,1],[1,3,6,1],[1,3,10,1],[1,3,2,1],[1,3,4,1],[1,3,2,1],[1,3,1,1],[1,3,5,1],[1,2,4,1],[1,2,2,1],[1,2,8,1],[1,2,3,1],[1,2,1,1],[1,2,9,1],[1,2,10,1],[1,2,9,1],[1,2,4,1],[1,2,5,1],[1,2,0,1],[1,2,9,1],[1,2,9,1],[1,2,0,1],[1,2,1,1],[1,2,1,1],[1,2,4,1],[1,1,0,1],[1,1,2,1],[1,1,2,1],[1,1,5,1],[1,1,3,1],[1,1,10,1],[1,1,6,1],[1,1,0,1],[1,1,8,1],[1,1,6,1],[1,1,4,1],[1,1,9,1],[1,1,9,1],[1,1,4,1],[1,1,2,1],[1,1,9,1],[1,1,0,1],[1,1,8,1],[1,1,6,1],[1,1,1,1],[1,1,1,1],[1,1,5,1]]
    daily_minutes_good = [68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]
    random.seed(0)
    multi_reg = MultiReg(0.001)
    multi_reg.fit(x, daily_minutes_good)
    print(multi_reg.beta)

    ################################
    # PCA
    ###############################
    # 1 Get the data in a dataframe
    dataset = pd.read_csv("data/Sales.csv", sep=";")
    del dataset["Unnamed: 0"]

    list(dataset.columns.values)

    # Clean the Sales column
    dataset.Sales = dataset.Sales.apply(lambda x: x.replace(',','.'))
    dataset = dataset.astype(float)

    #separate Sales target
    dataset.Sales = dataset.Sales.astype(float)
    target = dataset.Sales
    del dataset["Sales"]

    pca_homemade = PCA_scratch(n_components=5)
    U,S,V = pca_homemade.fit(dataset)
    transformed_data_handmade = pca_homemade.transform(dataset.values)
    print(transformed_data_handmade)
        
    # pca_sklearn = PCA(n_components=5)
    # pca_sklearn.fit(dataset.values)
    # #print(pca.explained_variance_ratio_)  
    # transformed_data=pca_sklearn.transform(dataset.values)
    # print(transformed_data)