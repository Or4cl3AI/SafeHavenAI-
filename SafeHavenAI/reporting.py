```python
import json
import datetime

from SafeHavenAI.vulnerability_scanner import VULNERABILITY_DATA
from SafeHavenAI.malware_detection import MALWARE_DATA
from SafeHavenAI.data_encryption import ENCRYPTED_DATA
from SafeHavenAI.user_training import USER_TRAINING_DATA
from SafeHavenAI.threat_intelligence import THREAT_INTELLIGENCE_DATA
from SafeHavenAI.real_time_detection import REAL_TIME_DETECTION_DATA
from SafeHavenAI.automated_response import AUTOMATED_RESPONSE_DATA
from SafeHavenAI.scalability import SYSTEM_SCALABILITY_DATA
from SafeHavenAI.cost_effectiveness import COST_DATA
from SafeHavenAI.reliability import RELIABILITY_DATA
from SafeHavenAI.security import SECURITY_DATA
from SafeHavenAI.customization import CUSTOMIZATION_DATA
from SafeHavenAI.support import SUPPORT_DATA

def generate_report():
    report_data = {
        "vulnerability_data": VULNERABILITY_DATA,
        "malware_data": MALWARE_DATA,
        "encrypted_data": ENCRYPTED_DATA,
        "user_training_data": USER_TRAINING_DATA,
        "threat_intelligence_data": THREAT_INTELLIGENCE_DATA,
        "real_time_detection_data": REAL_TIME_DETECTION_DATA,
        "automated_response_data": AUTOMATED_RESPONSE_DATA,
        "system_scalability_data": SYSTEM_SCALABILITY_DATA,
        "cost_data": COST_DATA,
        "reliability_data": RELIABILITY_DATA,
        "security_data": SECURITY_DATA,
        "customization_data": CUSTOMIZATION_DATA,
        "support_data": SUPPORT_DATA,
        "report_generated_at": datetime.datetime.now().isoformat()
    }

    with open('report.json', 'w') as f:
        json.dump(report_data, f, indent=4)

    print("Report generated successfully at report.json")

if __name__ == "__main__":
    generate_report()
```