import unittest

from tests.context import sample

import sample.src.utils.visualizeData as visualizeData;
class MyTest(unittest.TestCase):
    def test_load_data_in_tabular_form(self):
        targetFile = ("../resources/train.csv")
        with open(targetFile) as targetData:
            tabData = visualizeData.tabularData(targetData.readlines())
            assert len(tabData) == 891
            assert len(tabData[0]) == 12

    def test_summary_stats(self):
        targetFile = ("../resources/train.csv")
        with open(targetFile) as targetData:
            data = visualizeData.tabularData(targetData.readlines())
            summary1= visualizeData.summaryStatistics(data, 9, percentile=2)
            print (summary1)