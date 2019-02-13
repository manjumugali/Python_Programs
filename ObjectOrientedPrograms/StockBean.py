"""
******************************************************************************
* Purpose:  Program To data holder bean class.
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   27-01-2019
*
******************************************************************************
"""


class Stock:
    def __init__(self, name, no_share, price):
        self.__stock_name = name
        self.__no_share = no_share
        self.__share_price = price

    def setName(self, name):
        self.__stock_name = name

    def setNoShare(self, no_share):
        self.__no_share = no_share

    def setPrice(self, price):
        self.__share_price = price

    def getName(self):
        return self.__stock_name

    def getNoShare(self):
        return self.__no_share

    def getPrice(self):
        return self.__share_price