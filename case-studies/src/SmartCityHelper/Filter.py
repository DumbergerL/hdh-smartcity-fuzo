import datetime

def filterDateRange(dataPoint, fromDateString, toDateString):
    fromDate = datetime.datetime.strptime(fromDateString, '%Y-%m-%d %H:%M:%S')
    lastDate = datetime.datetime.strptime(toDateString, '%Y-%m-%d %H:%M:%S')

    datetimeValue = datetime.datetime.strptime(dataPoint['datetime'], '%Y-%m-%d %H:%M:%S')

    return datetimeValue > fromDate and datetimeValue < lastDate