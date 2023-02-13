#### Intro 
Here is some example data pulled from NASA in JSON format 

#### Near Earth Object (NEO) data: 
```
            {
                "links": {
                    "self": "http://api.nasa.gov/neo/rest/v1/neo/54341459?api_key=xfgp244Iz1GK1Bbk1eG32doMCb9NgafoW0efmNqt"
                },
                "id": "54341459",
                "neo_reference_id": "54341459",
                "name": "(2023 CY)",
                "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54341459",
                "absolute_magnitude_h": 26.367,
                "estimated_diameter": {
                    "kilometers": {
                        "estimated_diameter_min": 0.0141629909,
                        "estimated_diameter_max": 0.0316694105
                    },
                    "meters": {
                        "estimated_diameter_min": 14.1629909163,
                        "estimated_diameter_max": 31.6694104535
                    },
                    "miles": {
                        "estimated_diameter_min": 0.0088004718,
                        "estimated_diameter_max": 0.0196784532
                    },
                    "feet": {
                        "estimated_diameter_min": 46.4665071177,
                        "estimated_diameter_max": 103.9022685921
                    }
                },
                "is_potentially_hazardous_asteroid": false,
                "close_approach_data": [
                    {
                        "close_approach_date": "2023-02-11",
                        "close_approach_date_full": "2023-Feb-11 20:22",
                        "epoch_date_close_approach": 1676146920000,
                        "relative_velocity": {
                            "kilometers_per_second": "11.0244915499",
                            "kilometers_per_hour": "39688.1695796591",
                            "miles_per_hour": "24660.6851479832"
                        },
                        "miss_distance": {
                            "astronomical": "0.0205286127",
                            "lunar": "7.9856303403",
                            "kilometers": "3071036.733974949",
                            "miles": "1908253.7395903362"
                        },
                        "orbiting_body": "Earth"
                    }
                ],
                "is_sentry_object": false
            }
        ]
    }
}
```
#### Example Solar Flare Data 
```
   {
        "activityID": "2023-02-12T17:12:00-CME-001",
        "catalog": "M2M_CATALOG",
        "startTime": "2023-02-12T17:12Z",
        "sourceLocation": "",
        "activeRegionNum": null,
        "link": "https://webtools.ccmc.gsfc.nasa.gov/DONKI/view/CME/23740/-1",
        "note": "This CME is visible to the SE in SOHO LASCO C2/C3 and STEREO A COR2 coronagraph imagery. The source is likely an opening of field lines visible beyond the SW limb in SDO AIA 171 imagery starting around 2023-02-12T17:00Z.",
        "instruments": [
            {
                "displayName": "SOHO: LASCO/C2"
            },
            {
                "displayName": "SOHO: LASCO/C3"
            },
            {
                "displayName": "STEREO A: SECCHI/COR2"
            }
        ],
        "cmeAnalyses": [
            {
                "time21_5": "2023-02-12T22:21Z",
                "latitude": -32.0,
                "longitude": 144.0,
                "halfAngle": 16.0,
                "speed": 697.0,
                "type": "C",
                "isMostAccurate": true,
                "note": "Measurement based on the best fit between SOHO LASCO C2/C3 and STEREO A COR2 following the bulk portion of the CME. Longitude may vary +/-10 degrees.",
                "levelOfData": 0,
                "link": "https://webtools.ccmc.gsfc.nasa.gov/DONKI/view/CMEAnalysis/23741/-1",
                "enlilList": null
            }
        ],
        "linkedEvents": null
    }
]
```

#### Example Solar Flare Data
```
    {
        "flrID": "2023-02-12T15:33:00-FLR-001",
        "instruments": [
            {
                "displayName": "GOES-P: EXIS 1.0-8.0"
            }
        ],
        "beginTime": "2023-02-12T15:33Z",
        "peakTime": "2023-02-12T15:38Z",
        "endTime": "2023-02-12T16:01Z",
        "classType": "M1.0",
        "sourceLocation": "S10E26",
        "activeRegionNum": 13217,
        "linkedEvents": null,
        "link": "https://webtools.ccmc.gsfc.nasa.gov/DONKI/view/FLR/23733/-1"
    }
]

```
