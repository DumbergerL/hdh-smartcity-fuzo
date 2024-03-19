import json
import os

SENSOR_NAMES = ['Brenzstr', 'FuZo_Eugen-Jaekle-Platz', 'FuZo_Olgastr', 'Arkaden', 'Knoepfle_Nord', 'Knoepfle_Ost']

def getAllSensors():

    sensorData = {}
    for sensorName in SENSOR_NAMES:    
        
        filePath = os.path.join("..", "..", "data", sensorName + ".json")
        
        with open(filePath) as jsonFile:
            data = json.load(jsonFile)
            sensorData[sensorName] = data     

    
    return sensorData