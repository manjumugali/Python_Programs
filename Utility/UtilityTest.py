"""
******************************************************************************
* Purpose: It Contains All The Static Methods To Perform Operation On User Input
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   12-01-2019
*
******************************************************************************
"""
import math
import random
import decimal
import time


class TestFunctional:

    """--Perform Replacement Operation On Given Sentence <<UserName>>This Word Replace with The User Provided Input-"""

    @staticmethod
    def replaceUsername(name):  # It's Static Function That Accepts String as Parameter
        temp = "Hello <<UserName>>, How are you?"
        res = temp.replace("<<UserName>>", name)  # <<UserName>> its Replace with user input by using replace() function
        print(res)  # Prints Result To Console

    '''*************************************************************************************************************'''
    '''------------------------------Function To Find Percentage Of Heads And Tails---------------------------------'''
    @staticmethod
    def percentageOfHead_Vs_Tails(n):   # Its takes integer as argument
        count = 0
        heads = 0
        tails = 0
        while count < n:  # While loop executes Until count should be less than N
            randvalue = decimal.Decimal(random.randint(0, 10) / 10)     # Generating Random numbers
            count += 1

            if randvalue < 0.5:  # if the random number is less than 0.5 it will increments tails else increments heads
                tails += 1
            else:
                heads += 1

        print("No of Heads:", heads)
        print("No of Tails:", tails)
        head = heads / n * 100  # To Calculate Percentage of Heads
        tail = 100 - head  # To Calculate Percentage of Tails
        print("PercentageOfHeads:", head)
        print("PercentageOfTails:", tail)

    '''*************************************************************************************************************'''

    '''------------------------Function To Check Whether The Year Is Leap Year OR normal year-----------------------'''
    @staticmethod
    def TestLeapYear_OR_NotLeapYear(year):  # it accepts Integer as parameter
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  # if Year is completely Divisible by 4 or 100 or 400
            print("Entered Year Is Leap Year")
            return True
        else:
            print("Entered Year Is Not Leap Year")
            return False
    '''****************************************************1*********************************************************'''

    '''------------------------------------Function To print powers Of 2--------------------------------------------'''

    @staticmethod
    def printPowerOf2(n):   # it accepts Integer As parameter
        for i in range(1, n):   # It loop until to reach n value
            print("2^", i, "=", pow(2, i))  # finding 2 power (1 - n-1) using math class pow() function

    '''*************************************************************************************************************'''

    '''------------------------------------Function To Print harmonic Numbers---------------------------------------'''

    @staticmethod
    def harmonicNumbers(n):     # it accepts Integer As parameter
        sum1 = 0.0
        for x in range(1, n+1):     # It loop until to reach n+1 value
            sum1 = sum1 + 1.0 / x   # logic is like this 1/1 + 1/2 + 1/3 + ... + 1/N
        print("Harmonic Number :", sum1)

    '''*************************************************************************************************************'''

    '''----------------------------------Function To Print Prime Factors Numbers------------------------------------'''

    @staticmethod
    def findPrimeFactors(n):    # it accepts Integer As parameter
        p = 2
        print("Number of Prime factors of '", n, "' are")
        while n > p * p:    # While loop executes Until N should be less than p*p
            if n % p == 0:      # if N is completely Divisible By P then only control Entire  into if loop
                print(p)
                n = n // p
            else:
                p += 1       # if N is not Divisible By p then Increment P value with 1
        print(n)

    '''*************************************************************************************************************'''
    '''-----------------------------Function To play gambler game and prints Win Or lose ---------------------------'''

    @staticmethod
    def getReadyToPlayGame(stake, goal, no):   # It Takes 3 Parameters as Integer
        win = 0
        loss = 0
        nt = no
        while no > 0:   # While loop executes Until N should be > 0
            randvalue = random.random()  # Generating Random numbers
            if randvalue > 0.5:     # if generated random number is > 0.5 increment win by 1
                win += 1
            else:
                loss += 1   # else generated random number is > 0.5 increment win by
            no -= 1     # decrement N by 1

        print("Number of Time Wins", win)
        print("Number of  Time Loses", loss)
        wins = win / nt * 100   # To Calculate Percentage of win
        lose = 100 - wins   # To Calculate Percentage of lose

        if wins > lose:     # if win > lose entire into loop
            print("Percentage of wins", wins)
        else:
            print("Percentage of loses", lose)

    '''*************************************************************************************************************'''
    '''--------------Function To Count how many Time Random method is Invoked to get distinct coupon----------------'''

    @staticmethod
    def generateCouponNumbers(n):   # it takes one parameter as integer
        count = 0
        my_list = []  # Empty Array list to store Distinct coupon
        while len(my_list) < n:     # while loop executes until len(arr) should be < N
            randvalue = random.randint(0, n)    # Generating Random numbers
            count += 1      # Increment count by 1
            if randvalue not in my_list:    # if generated number is not in array list control enters into loop
                my_list.append(randvalue)       # generated number added lo array at the end

        print("Number of Generated random numbers", count)
        print(my_list)

    '''*************************************************************************************************************'''
    '''-----------------------------------------Function to Print Matrix Format-------------------------------------'''

    @staticmethod
    def printMatrixArray(matrix, m, n):     # it accepts three parameters as list,Integers
        for i in range(m):  # it executes until i reach to row value
            for j in range(n):  # it executes until j reach to col value
                print(matrix[i][j], end=" ")    # to print matrix format
            print()

    '''*************************************************************************************************************'''
    '''-----------------------------Function To Find DistinctTriplets ----------------------------------------------'''
    @staticmethod
    def distinctTriplets(arr):  # it Accepts Array list As parameter
        my_triplets = []
        for i in range(len(arr)):   # it executes until i reach to len(arr) value
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == 0:   # if a[i]+a[j]+a[k]=0 these are triplet numbers
                        if arr[i] not in my_triplets or arr[j] not in my_triplets or arr[k] not in my_triplets:
                            my_triplets.append(arr[i])  # if triplets numbers not in array add it to array list
                            my_triplets.append(arr[j])
                            my_triplets.append(arr[k])

        count = len(my_triplets) / 3    # to get number of distinct numbers
        print("Number Of Distinct Triplets :", int(count))
        print("All The Distinct Triplets :", my_triplets)

    '''*************************************************************************************************************'''
    '''---------------------------------Function To find Euclidean Distance-----------------------------------------'''

    @staticmethod
    def findEuclideanDistance(x, y):       # it Accepts Number As parameter
        px = pow(x, 2)
        py = pow(y, 2)
        res = px + py
        result = math.sqrt(res)     # logic is (x*x + y*y)
        print(result)

    '''*************************************************************************************************************'''
    '''--------------------Function To Start CountDown of time------------------------------------------------------'''

    @staticmethod
    def startWatch(choice):     # it Accepts Number As parameter
        if choice == 1:
            start_time = time.time()    # time() returns time as a floating point number expressed in seconds
            return start_time

    '''*************************************************************************************************************'''
    '''----------------------------------Function To Print Elapsed Time---------------------------------------------'''
    @staticmethod
    def stopWatch(choice, start):   # it takes 2 parameters As Integer And Float
        if choice == 2:
            end_time = time.time() - start  # to calculate Elapsed time
            print("Elapsed time  :", end_time, "Secs")

    '''*************************************************************************************************************'''
    '''-----------------------------Function To ind the roots of the equation a*x*x + b*x + c.-----------------------'''

    @staticmethod
    def findRoots(a, b, c):     # it takes 3 parameters as integer
        delta = pow(b, 2) - 4 * a * c   # calculating delta value
        res = 2 * a
        r1 = (-b + math.sqrt(delta)) / res  # formula Root 1 of x = (-b + sqrt(delta))/(2*a)
        r2 = (-b - math.sqrt(delta)) / res  # formula Root 2 of x = (-b - sqrt(delta))/(2*a)
        print(r1, r2)

    '''*************************************************************************************************************'''
    '''-----------------------------Function To Print WindChill Using Math Formula----------------------------------'''

    @staticmethod
    def resultOfWindChill(temp, ws):  # It Takes Two parameters as Integers
        pws = math.pow(ws, 0.16)       # Find Power of speed
        res = 35.74 + 0.6215 * temp
        res2 = 0.4275 * temp - 35.75 * pws
        result = res + res2     # its Based On Formula
        print("Wind Chill :", result)

    '''*************************************************************************************************************'''
    '''-------------------------------Function To Anagram Detection ------------------------------------------------'''

    @staticmethod
    def checkTwoStringsAnagram(s1, s2):  # it Accepts Two parameters As Strings
        result = False
        str1 = sorted(s1)
        str2 = sorted(s2)

        if len(str1) == len(str2):  # if both String length Is Same then control enters into loop else Not anagram

            for i in range(len(str1)):  # loop over the string element
                if str1[i] == str2[i]:  # if both the String elements are equal then result set to true
                    result = True
                else:
                    result = False

            if result:  # if its true the String Elements Are Anagram
                print("Two Strings Are Anagram")
        else:
            print("Two Strings Are Not Anagram")

    '''*************************************************************************************************************'''
    '''------------------------------Function To find Prime Numbers between(0-1000)---------------------------------'''

    @staticmethod
    def PrimeNumbers(n):  # it accepts 1 parameter as Integer
        my_list = []
        pm_list = []
        for i in range(0, n):  # it loops until i reach to N
            if i > 1:
                result = True
                for j in range(2, i):   # it loops until J reach to i
                    if i % j == 0:  # if i completely divisible by j then its not prime number
                        result = False
                        break

                if result:  # if result == to True then its prime number
                    pm_list.append(i)
                    my_list.append(str(i))
        # print(".............List Of Prime Numbers From Given Range 0-", n, ":.........")
        # print(pm_list)
        return my_list

    '''*************************************************************************************************************'''
    '''--------------------Function to Check in prime number list how many are anagram Numbers----------------------'''
    @staticmethod
    def anagramPrime(my_list):  # it takes list as parameter
        my_list1 = []
        # print("...............List of Anagram Prime Numbers...........")
        for i in range(len(my_list)):  # i=0 to length of list
            for j in range(i + 1, len(my_list)):    # j=i+1 to length of list
                temp = my_list[j]
                if sorted(my_list[i]) == sorted(my_list[j]):  # if a[i] & a[j] are equal then anagram Number
                    if my_list[i] not in my_list1:
                        # print(my_list[i], temp)
                        my_list1.append(my_list[i])

        return my_list1

    '''*************************************************************************************************************'''
    '''--------------------Function to Check in prime number list how many are anagram Numbers----------------------'''
    @staticmethod
    def notAnagramPrime(my_list):  # it takes list as parameter
        my_list1 = []
        for i in range(len(my_list)):  # i=0 to length of lis
            temp1 = my_list[i]
            for j in range(i + 1, len(my_list)):  # j=i+1 to length of list
                temp = my_list[j]
                if sorted(my_list[i]) != sorted(my_list[j]):  # if a[i] & a[j] are equal then anagram Number
                    if my_list[i] not in my_list1:
                        my_list1.append(my_list[i])

        return my_list1

    '''*************************************************************************************************************'''
    '''-----------------Function To Check in prime number list how many are Palindrome Numbers----------------------'''

    @staticmethod
    def palindrome(n):  # it accepts 1 parameter as Integer
        rev = 0
        temp = n
        while n > 0:  # loop executes until N > 0
            rem = n % 10    # hold remainder
            rev = rev * 10 + rem    # to get reverse of Number
            n = n // 10

        if rev == temp:  # if booth are == then Number is Palindrome
            return temp

    '''*************************************************************************************************************'''
    '''-------------------------Function To Search Element in Array list--------------------------------------------'''

    @staticmethod
    def searchElement(arr1, ele):  # It accepts 2 parameters as list,Integer Or String
        arr = sorted(arr1)      # sort the Array
        low = 0
        h = len(arr) - 1
        flag = True
        while low <= h:  # loop executes until low <= high
            m = (low + h) // 2  # get middle element position

            if arr[m] == ele:  # if element == a[m] then element found
                print("Element '", arr[m], "' Found At position of", m)
                flag = False

            if arr[m] < ele:  # if a[m] < element the set low = m + 1 else high = m - 1
                low = m + 1
            else:
                h = m - 1
        if flag:    # if flag == True then Element Not Found
            print("Element Is Not Found")

    '''*************************************************************************************************************'''
    '''-----------------Function To sort List of Elements Using Insertion sort---------------------------------------'''

    @staticmethod
    def insertionSort(arr):  # it takes list As parameter
        start = u.startWatch(1)
        j = 0
        for i in range(1, len(arr)):    # i=1 to length of list
            temp = arr[i]
            j = i - 1
            while j >= 0 and temp < arr[j]:  # To check a[i] < a[j] and assign value to a[j+1] = a[j]
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp   # final value is  assign to a[j+1]=a[i]
        # u.stopWatch(2, start)
        return arr

    '''*************************************************************************************************************'''
    '''-------------------Function To sort List of Elements Using Bubble Sort---------------------------------------'''
    @staticmethod
    def bubbleSort(arr):  # it takes list as parameter
        start = u.startWatch(1)
        for i in range(len(arr)):  # it loops i=0 to length of list
            for j in range(i + 1, len(arr)):    # it loops j=i+1 to length of list
                if arr[i] > arr[j]:     # if a[i] > a[j] then it swap the value
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        u.stopWatch(2, start)
        return arr

    '''*************************************************************************************************************'''
    '''-----------------------------------Function To Binary Representation-----------------------------------------'''

    @staticmethod
    def covertDecimalToBinary(num):  # it takes number as parameter
        my_list = []
        while num > 0:      # loop until reach to N > 0
            rem = num % 2
            my_list.append(rem)
            num = num // 2
        my_list.reverse()
        for i in range(len(my_list), 8):  # Adding 0 to empty position
            my_list.append(0)
        str1 = ""
        for j in my_list:   # to marge all numbers into single number
            str1 = str1 + str(j)

        return str1

    '''**************************************************************************************************************'''
    '''-------------------------Function to Print Question to find your number'''

    @staticmethod
    def guessNumber(my_list, low, high):  # it takes 3 parameters as list,number
        num = 0
        num1 = 0
        res = True
        mid = low + high  # middle position
        mid = mid // 2      # to get middle position

        if low == high:     # if low == high than this is your number
            print("Your Guess Number is ::", my_list[mid])
        else:
            print("Your Guess Number is ::", my_list[mid])
            print("YES = 0 :: NO = 1")
            num = int(input())   # reading input as number

        if num == 1:    # if num = 1 this not guess number else this is guess Number
            print("Your Number is Grater than", my_list[mid], " Press = 0 :: Smaller than", my_list[mid], " press = 1")
            num1 = int(input())  # reading input
            res = True
        else:
            print("Your Guess Number is ::", my_list[mid])
            res = False

        if res:     # if res is True then guess number is > middle number else < middle number
            if num1 == 0:
                low = mid + 1
                u.guessNumber(my_list, low, high)   # recursively Calling method
            else:
                high = mid - 1
                u.guessNumber(my_list, low, high)   # recursively Calling method

    '''**************************************************************************************************************'''
    '''---------------------Function to Check the resultant number is the number is a power of 2---------------------'''

    @staticmethod
    def binaryToDecimal(number):    # It takes Binary as parameter
        dec_value = 0
        base = 1    # base value
        temp = number
        while temp:   # it Executes until temp == 0
            last_digit = temp % 10
            temp = int(temp / 10)

            dec_value += last_digit * base
            base = base * 2
        return dec_value

    '''**************************************************************************************************************'''
    '''---------------------Function to Check the resultant number is the number is a power of 2---------------------'''
    @staticmethod
    def isPowerOf2(res1):   # it takes decimal Number as parameter
        log2 = (math.log10(res1) // math.log10(2))  # math class Methods to Check power of 2
        return math.ceil(log2) == math.floor(log2)

    '''**************************************************************************************************************'''
    '''------------------------------Function To Find Day Of the Week------------------------------------------------'''
    @staticmethod
    def dayOfTheWeek(month, day, year):
        months = {1: 'jan', 2: 'Feb', 3: 'March', 4: 'April', 5: 'May', 6: 'Jun', 7: 'July', 8: 'Aug', 9: 'Sept',
                  10: 'Oct', 11: 'Nov', 12:  'Dec'}
        weeks = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        y = year-(14-month)//12
        x = y + y//4-y//100+y//400
        m = month+12*((14-month)//12)-2
        d = (day + x + 31 * m//12) % 7
        print("Day Of The Week : ", weeks[d], "-", months[month], "-", year)
        return d

    '''**************************************************************************************************************'''
    '''---------------------------Function To  Temperature Conversion------------------------------------------------'''
    @staticmethod
    def temperatureConversion(choice):     # it takes 3 arguments as Integer
        if choice == 1:  # if choice == 1 Fahrenheit to Celsius else Celsius to Fahrenheit
            print("Enter Value for Fahrenheit:")
            f = int(input())  # reading input
            c = (f-32)*5//9   # formula to convert Celsius
            print("Temperature Conversion Fahrenheit to Celsius:", c)
        else:
            print("Enter The Value For Celsius :")
            c = int(input())    # Reading input
            f = (c*9//5)+32     # formula to convert Fahrenheit
            print("Temperature Conversion Celsius to Fahrenheit:", f)

    '''**************************************************************************************************************'''
    '''--------------------------------Function to Calculate ​ monthly Payment --------------------------------------'''

    @staticmethod
    def monthlyPayment(ploan, year, pi):    # it takes 3 parameters as Integer
        n = 12 * year
        r = pi // (12*100)
        p1 = ploan*r//1-(1+r)
        payment = pow(p1, -n)       # calculation using formula
        print("Monthly Payment Is :", payment)

    '''**************************************************************************************************************'''
    '''------------------------------Function to Compute Square Root of Number---------------------------------------'''
    @staticmethod
    def findSquareRoot(number):
        epsilon = 1e-15  # initialise Newton's method
        t = number

        while math.fabs(t-number/t) > epsilon*t:   # it Executes until abs(t-number/t) >epsilon
            t = (number/t+t)/2.0    # calculating average of c/t and t
        print("Square Root of '", number, "'is :", t)

    '''**************************************************************************************************************'''
    '''---------------------------------Function To Sort Elements using Marge Sort-----------------------------------'''
    @staticmethod
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            low = arr[:mid]  # Dividing the array elements
            high = arr[mid:]  # into 2 halves

            u.mergeSort(low)  # Sorting the first half We Are Calling Recursively Calling method
            u.mergeSort(high)  # Sorting the second half Recursively Calling method
            i = j = k = 0

            # Copy data to temp arrays low[] and high[]
            while i < len(low) and j < len(high):
                if low[i] < high[j]:
                    arr[k] = low[i]
                    i += 1
                else:
                    arr[k] = high[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(low):
                arr[k] = low[i]
                i += 1
                k += 1
            # Checking if any element was right
            while j < len(high):
                arr[k] = high[j]
                j += 1
                k += 1
            return arr


u = TestFunctional()