"""
Write a Python program to calculate two date difference in seconds.
"""
import datetime
dateinput1 = input("Enter a date separated by space\n(day, month, year, hour, minute, second)(example: 18 2 2014 19 03 45):\n")
datelist1 = dateinput1.split()
date1 = [int(num) for num in datelist1]
x = datetime.datetime(year = date1[2],
                      month = date1[1],
                      day = date1[0],
                      hour = date1[3],
                      minute = date1[4],
                      second = date1[5])

dateinput2 = input("Enter a second date\n(day, month, year, hour, minute, second):\n")
datelist2 = dateinput2.split()
date2 = [int(num) for num in datelist2]
y = datetime.datetime(year = date2[2],
                      month = date2[1],
                      day = date2[0],
                      hour = date2[3],
                      minute = date2[4],
                      second = date2[5])

print ("Date 1:", x)
print ("Date 2:", y)

print("Absolute difference between dates:", abs(x - y))
print("Absolute difference between dates in seconds:", abs(x - y).total_seconds())
