from ast import literal_eval

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import pylab
import scipy.stats as stats
from pandas.plotting import *

targetFile = "/run/media/aditya/EXTRA/repos/kaggle/tests/resources/train.csv"
fields = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']


def plotQuartile(data, columnIndex):
    colData = []
    for row in data:
        colData.append(float(row[columnIndex]))
    stats.probplot(colData, dist="norm", plot=pylab)
    pylab.show()


def plotDataFrame(dataFrame, plotting_function, *functionArgs, **keyArgs):
    plot.figure()
    plotting_function(dataFrame, *functionArgs, **keyArgs)
    plot.show()


def convertCategoricalToNumerical(dataFrame, columns=None):
    """

    :type dataFrame: pandas.DataFrame
    :type columns: list
    """
    if columns is None:
        columns = []
    catColumns = set()
    for column in dataFrame.columns:
        if (dataFrame[column]).dtype is np.dtype(object):
            dataFrame[column] = dataFrame[column].astype('category')
    for column in columns:
        dataFrame[column] = dataFrame[column].astype('category')
    cat_columns = dataFrame.select_dtypes(['category']).columns
    dataFrame[cat_columns] = dataFrame[cat_columns].apply(lambda x: x.cat.codes)
    return dataFrame


def getNormalizedForm(df):
    return (df - df.mean()) / (df.max() - df.min())


def corrMatrixPlot(dataFrame):
    """

    :type dataFrame: pandas.DataFrame
    """
    corMat = dataFrame.corr(method='kendall')
    plot.pcolor(corMat)
    plot.show()


def main():
    function_mappings = {
        'scatter_matrix': scatter_matrix,
        'parallel_coordinates': parallel_coordinates,
        'andrews_curves': andrews_curves,
        'lag_plot': lag_plot,
        'radviz': radviz
    }
    df = pd.read_csv(targetFile, skipinitialspace=True, usecols=fields)
    df = df.dropna(how='any')
    df = convertCategoricalToNumerical(df)
    df_norm = getNormalizedForm(df)
    plottingFunction = function_mappings[input("Enter function name: ")]
    keyArgs = literal_eval(input("Enter args, if any in list form: "))
    keyWords = literal_eval(input("Enter args, if any in dictionary form: "))
    plotDataFrame(df_norm, plottingFunction, *keyArgs, **keyWords)


df = pd.read_csv(targetFile, skipinitialspace=True, usecols=fields)
corrMatrixPlot(df)
