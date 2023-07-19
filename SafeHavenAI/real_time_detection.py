```python
import os
import sys
import json
import datetime
from threat_intelligence import THREAT_INTELLIGENCE_DATA

REAL_TIME_DETECTION_DATA = []

def detect_real_time_threat():
    print("Real-time threat detection initiated...")
    for threat in THREAT_INTELLIGENCE_DATA:
        if datetime.datetime.now() - threat['time'] < datetime.timedelta(minutes=5):
            REAL_TIME_DETECTION_DATA.append(threat)
            print(f"Real-time threat detected: {threat['name']}")
    return REAL_TIME_DETECTION_DATA

if __name__ == "__main__":
    detect_real_time_threat()
```