# Gyasi Hayes
# 04/**/2026
# 
import cpu_monitor
import network_monitor
import network_monitor
from exceptions import(ServiceUnavailableError, DataCorruptionError, ConnectionTimeoutError, ThresholdExceededError)

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0

def check_cpu():
    try:
        data = cpu_monitor.get_cpu_metrics()
        if data['usage_percent'] > CPU_THRESHOLD:
            raise ThresholdExceededError("CPU Threshold Exceeded")
        return{"Status": "Healthy", "Data": data}
   
    except ServiceUnavailableError:
        return{"Status": "Error", "Data": "Service Unavailable"}

    except ThresholdExceededError as error:
        return{"Status": "Error", "Data": str(error)}
    
