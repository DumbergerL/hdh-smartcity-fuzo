# HDH FuZo Data

This repository hosts traffic data from the pedestrian zone in Heidenheim, sourced from the smart city API. For further information, refer to the [unofficial documentation](https://github.com/DumbergerL/hdh-smartcity-api). The repository aims not only to retrieve and archive this data but also to refine and convert it into a more practical format.

The dataset begins from November 10th, 2022.

## Extract Data:

The collected data comes from these six traffic sensors provided by the smart city:

| Name | labelIdentifier |
| ---  | --- |
| Arkaden | 3bc2a1ae-8a6f-4cc6-aab0-0e7ac50f3077 |
| FuZo_Eugen-Jaekle-Platz | 8752218d-1afc-468f-9f89-79576547798c |
| FuZo_Olgastr | f3060e0b-ad7c-4987-afe6-471ca7178b34 |
| Brenzstr | 841db5c7-fd00-470c-8854-e65e52b3c010 |
| Knoepfle_Nord | 95a79150-a49c-4580-8397-aa380cc596e3 |
| Knoepfle_Ost | 71e09626-6b0d-42c4-91e1-1ddc59e03c0e |

The unprocessed data is organized into chunks within the [raw-data](raw-data) directory. Each file corresponds to a specific quarter for each sensor. Below is a JSON example response from the data endpoint.

```json
{
    "data": 
        [
            {
                "id": "25c0b636-8038-409d-8d6b-b5e721670288", "singleDataPoints": [
                    {
                        "datetime": "2023-01-01T23:30:00+00:00", 
                        "value": "1", 
                        "valueKey": "bicycle.in"
                    }, 
                    {
                        "datetime": "2023-01-01T23:30:00+00:00",
                        "value": "0", 
                        "valueKey": "van.out"
                    }, 
                ],
                "name": "Verkehr Brenzstr", 
                "labelIdentifier": "841db5c7-fd00-470c-8854-e65e52b3c010", "labelName": "Verkehr Brenzstr", 
                "latitude": 48.67826862158109, 
                "longitude": 10.151976682033705, 
                "groupIdentifier": "d18db740-d364-43ff-86c7-9655d009a529",
            }
        ]
}
```

Below is an illustrative request to retrieve data for the Eugen-Jaekle-Platz Sensor during Q4 of 2023:
- https://staging.dashboard.heidenheim.de/api/historical/?labelIdentifier=8752218d-1afc-468f-9f89-79576547798c&datetime__gte=2023-10-01T00:00:00.000Z&datetime__lte=2024-01-01T23:55:55.500Z


## Transform Data:

The raw collected data has been converted into a more practical format. In its original state, sensor values are spread across different objects instead of being consolidated within one object for each timestamp. This issue is resolved through the transformation process executed by the Jupyter notebook [data/ProcessRawData.ipynb](data/ProcessRawData.ipynb). Additionally, the notebook includes comments to aid in understanding the transformation procedure.

As a result of this transformation process, each sensor has a single JSON file encompassing all data for the entire time period ([data-Folder](data)):

- [Arkaden.json](data/Arkaden.json)
- [Brenzstr.json](data/Brenzstr.json)
- [FuZo_Eugen-Jaekle-Platz.json](data/FuZo_Eugen-Jaekle-Platz.json)
- [FuZo_Olgastr.json](data/FuZo_Olgastr.json)
- [Knoepfle_Nord.json](data/Knoepfle_Nord.json)
- [Knoepfle_Ost.json](data/Knoepfle_Ost.json)

Each sensor value is now grouped by the corresponding timestamp. Here an example of the JSON format:

```json
{
  "id": "0438a9cc-95cb-4111-bd3c-34dec97c720a",
  "name": "Zugang Arkaden Olgastr",
  "latitude": 48.67927135526141,
  "longitude": 10.152471894699366,
  "labelIdentifier": "3bc2a1ae-8a6f-4cc6-aab0-0e7ac50f3077",
  "groupIdentifier": "d18db740-d364-43ff-86c7-9655d009a529",
  "singleDataPoints": {
    "2022-12-31 23:30:00": {
      "datetime": "2022-12-31 23:30:00",
      "timestamp": 1672525800.0,
      "bicycle.in": "0",
      "bicycle.out": "0",
      "person.in": "2",
      "person.out": "3"
    },
    "2022-12-31 23:00:00": {
      "datetime": "2022-12-31 23:00:00",
      "timestamp": 1672524000.0,
      "bicycle.in": "0",
      "bicycle.out": "0",
      "person.in": "1",
      "person.out": "3"
    }
  }
}
```

> [!IMPORTANT]  
> Some of the sensor data show large time gaps. For example, the "Schloss Arkaden" sensor provides no data from 01.02.23 12:00 to 06.02.23 07:00. [More information on the missing sensor values here](data/MissingSensorValues.md). 

## Case Studies

The [case-studies](case-studies) folder contains sample scenarios for the data provided. Example case studies:

* [Warten auf's Christkind (Waiting for Santa Claus) Heidenheim 2022 vs 2023](/case-studies/warten-aufs-christkind/README.md)
* [Demonstration: "Nie wieder ist jetzt! (10.02.2024)"](/case-studies/demonstration-nie-wieder-ist-jetzt/README.md)
* [Does Weather Affect Visitor Numbers in Heidenheim Downtown?](/case-studies/correlation-weather/README.md)