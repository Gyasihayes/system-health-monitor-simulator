# Gyasi Hayes
# 04/17/2026
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
            raise ThresholdExceededError("Network Threshold Exceeded")
        return {"Status": "Healthy", "Data": network_data}
    except ConnectionTimeoutError:
        return{"Status": "Error", "Data": "Connection Timeout"}
    except ThresholdExceededError as error:
        return{"Status": "Error", "Data": str(error)}

def run_checks():
    cpu_result = check_cpu()
    memory_result = check_memory()
    network_result = check_network()
    check_results = {"CPU Check": cpu_result, "Memory Check": memory_result, "Network Check": network_result}
    return check_results

def log_results(results, filepath):
    try:
        with open(filepath, "a") as file:
            file.write(f"Results {results}\n")
            file.write("Results Logged\n")
    except Exception as error:
        print(f"Could not write to file: {error}")

def generate_report(results):
    report = "SYSTEM REPORT\n"
    for check_type in results:
        status = results[check_type]["Status"]
        report += (f"{check_type}: {status}\n")
    return report

def main():
    check_results = run_checks()
    report_string = generate_report(check_results)
    print (report_string)
    log_results(check_results, "monitor.log")

if __name__ == "__main__":
    main()
