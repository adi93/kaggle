import unittest

from tests.context import sample

import sample.src.utils.visualizeData as visualizeData;
class MyTest(unittest.TestCase):
    def __init__(self):
        self.targetFile = ("../resources/train.csv")


    def test_load_data_in_tabular_form(self):
        with open(self.targetFile) as targetData:
            tabData = visualizeData.tabularData(targetData.readlines())
            assert len(tabData) == 891
            assert len(tabData[0]) == 12

    def test_summary_stats(self):
        with open(self.targetFile) as targetData:
            data = visualizeData.tabularData(targetData.readlines())
            summary1= visualizeData.summaryStatistics(data, 9, percentile=2)
            assert len(summary1) == 3
            assert len(summary1.get("percentile")) == 3

    def test_plot_data