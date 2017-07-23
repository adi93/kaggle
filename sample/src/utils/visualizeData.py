import urllib
import sys
import numpy as np
import csv
import pylab
import scipy.stats as stats


def tabularData(data, delimiter=",", quoteCharacter="\""):
    """
    Converts data into 2D matrix form, where rows denote samples, and
    columns denote features.
    :param data: read from a file or url
    :return:
    """
    begin = 1 if isinstance(data[0][0], str) is True else 0
    tabData = list(csv.reader(data[begin:]))
    return tabData


def __summaryStatisticsNumerical(data, columnIndex, percentile):
    mean, variance, percentileBoundary = 0, 0, []
    colData = []
    for row in data:
        colData.append(float(row[columnIndex]))

    colArray = np.array(colData)
    mean = np.mean(colArray)
    variance = np.std(colArray)
    for i in range(percentile + 1):
        percentileBoundary.append(np.percentile(colArray, i * 100 // percentile))
    return [mean, variance, percentileBoundary]


def __summaryStatisticsCategorical(data, column):
    categoryMap = {}
    for row in data:
        if categoryMap.get(row[column]) is None:
            categoryMap[row[column]] = 1
        else:
            categoryMap[row[column]] = categoryMap.get(row[column]) + 1
    return categoryMap


def summaryStatistics(data, columnIndex, columnType='NUMERICAL', percentile=4):
    """
    Prints statistical info about a particular feature, like mean, variance and
    percentiles
    :param data: 2d matrix, where row represent data point, and column represent
     features.
    :param columnIndex: index of column for which summary is to be generated
    :param columnType: 'NUMERICAL' or 'CATEGORICAL'
    :param percentile: percentiles
    :return: dictionary containing percentiles, and (mean, variance)
            if NUMERICAL, (categoriesCount) otherwise
    """
    if columnType is 'NUMERICAL':
        mean, variance, percentile = __summaryStatisticsNumerical(data, columnIndex, percentile)
        return {"mean": mean, "variance": variance, "percentile": percentile}
    else:
        categoryCount = __summaryStatisticsCategorical(data, columnIndex)
        return {"categoriesCount": categoryCount}


def test_summary_stats():
    targetFile = "/run/media/aditya/EXTRA/repos/kaggle/tests/resources/train.csv"
    with open(targetFile) as targetData:
        data = tabularData(targetData.readlines())
        summary1 = summaryStatistics(data, 9, percentile=19)
        print(summary1)


def plotQuartile(data, columnIndex):
    colData = []
    for row in data:
        colData.append(float(row[columnIndex]))
    stats.probplot(colData, dist="norm", plot=pylab)
    pylab.show()


def parallelAttributeGraph(data, categories, categoryColumn = 1):
    for i in range(len(data)):
        if (data[i][categoryColumn] == "0")


def main():
    n = int(input("Enter the column index: "))
    with open("/run/media/aditya/EXTRA/repos/kaggle/sample/resources/projects/titanic/train.csv") as targetData:
        tabData = tabularData(targetData.readlines())
    summary1 = summaryStatistics(tabData, 9, percentile=19)
    print(tabData)
    plotQuartile(tabData, n)

if __name__ == '__main__':
    main()