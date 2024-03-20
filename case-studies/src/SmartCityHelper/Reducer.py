def avgReducer(dataPoints, dictValueKey, pointsToReduce = 3):
    maxIndex = len(dataPoints) - pointsToReduce

    values = []

    indexRange = range(0, maxIndex, pointsToReduce)
    
    for index in indexRange:
        sumVal = 0
        for nThValue in range(pointsToReduce):
            sumVal += int(dataPoints[index + nThValue][dictValueKey])
        
        dictCopy = dataPoints[index].copy()
        dictCopy[dictValueKey] = sumVal / pointsToReduce
        values.append(dictCopy)

    # Values that could not reduced
    #numberUnprocessedItems = indexRange[-1]
    lastProcessedItem = indexRange[-1] + (pointsToReduce - 1)
    indexesUnprocessedItems = range(lastProcessedItem + 1, len(dataPoints))
    
    for indexUnprocessedItem in indexesUnprocessedItems:
        values.append(dataPoints[indexUnprocessedItem]) 
    
    return values

def sumReducer(dataPoints, dictValueKey):
    return sumReducerWithReset(dataPoints, dictValueKey, [])

def sumReducerWithReset(dataPoints, dictValueKey, resetOnDateTimes):
    currentValue = 0
    values = []
    
    for dataPoint in dataPoints:
        dictCopy = dataPoint.copy()
        dictCopy[dictValueKey] = currentValue
        currentValue += int(dataPoint[dictValueKey])
        values.append(dictCopy)

        if 'datetime' in dataPoint and dataPoint['datetime'] in resetOnDateTimes:
            currentValue = 0

    return values