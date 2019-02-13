"""
******************************************************************************
* Purpose:  Program To arrange company share in Linked list
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   29-01-2019
*
******************************************************************************
"""
import json
from OOPS_Utility.Test_Oops_Utility import LinkedListQueue


class LinkedListCompanyShare:
    try:
        with open("stock.json", "r") as file:  # open Json file
            json_file = file.read()  # read json file
            file.close()  # close file
            stock = json.loads(json_file)  # convert json object to python object
            l1 = LinkedListQueue(stock)  # creating object LinkedListQueue class and passing parameters
            l1.enqueueCompanyShares()  # on l1 object invoking enqueueCompanyShares function
    except RuntimeError:
        print("...........oops Something Went Wrong.........")
