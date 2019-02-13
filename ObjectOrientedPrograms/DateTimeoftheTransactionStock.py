"""
******************************************************************************
* Purpose:  Program To maintain The Transaction date and time.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   28-01-2019
*
******************************************************************************
"""
import json
from OOPS_Utility.Test_Oops_Utility import DateTimeLinkedListQueue


class DateTimeOfTransaction:
    try:
        with open("DateTime.json", "r") as file:  # open Json file
            json_file = file.read()  # read json file
            file.close()  # close file
            data = json.loads(json_file)  # convert json object to python object
            l1 = DateTimeLinkedListQueue(data)  # creating object DateTimeLinkedListQueue class and passing parameters
            l1.enQueueTransaction()  # on l1 object invoking enQueueTransaction() function
    except FileNotFoundError:
        print("File Not Found....!")
