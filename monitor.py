# Gyasi Hayes
# 04/**/2026
# 
import cpu_monitor
import memory_monitor
import network_monitor
from exceptions import(ServiceUnavailableError, DataCorruptionError, ConnectionTimeoutError, ThresholdExceededError)

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0

def check_cpu():
    try:
        cpu_data = cpu_monitor.get_cpu_metrics()
        if cpu_data['usage_percent'] > CPU_THRESHOLD:
            raise ThresholdExceededError("CPU Threshold Exceeded")
        return{"Status": "Healthy", "Data": cpu_data}
   
    except ServiceUnavailableError:
        return{"Status": "Error", "Data": "Service Unavailable"}

    except ThresholdExceededError as error:
        return{"Status": "Error", "Data": str(error)}
    
def check_memory():
    try:
        memory_data = memory_monitor.get_memory_metrics()
        if memory_data['usage_percent'] > MEMORY_THRESHOLD:
            raise ThresholdExceededError("Memory Threshold Exceeded")
        return{"Status": "Healthy", "Data": memory_data}
    except DataCorruptionError:
        return{"Status": "Error", "Data": "Data Corrupted"}
    except ThresholdExceededError as error:
        return{"Status": "Error", "Data": str(error)}
    
def check_network():
    try:
        network_data = network_monitor.get_network_metrics()
        if network_data['usage_percent'] > NETWORK_THRESHOLD:
            raise ConnectionTimeoutError
    