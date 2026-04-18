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
        return{"status": "healthy", "data": cpu_data}
    except ServiceUnavailableError:
        return{"status": "error", "data": "Service Unavailable"}
    
def check_memory():
    try:
        memory_data = memory_monitor.get_memory_metrics()
        if memory_data['usage_percent'] > MEMORY_THRESHOLD:
            raise ThresholdExceededError("Memory Threshold Exceeded")
        return{"status": "healthy", "data": memory_data}
    except DataCorruptionError:
        return{"status": "error", "data": "Data Corrupted"}
    
def check_network():
    try:
        network_data = network_monitor.get_network_metrics()
        if network_data['usage_percent'] > NETWORK_THRESHOLD:
            raise ThresholdExceededError("Network Threshold Exceeded")
        return {"status": "healthy", "data": network_data}
    except ConnectionTimeoutError:
        return{"status": "error", "data": "Connection Timeout"}


def run_checks():
    cpu_result = check_cpu()
    memory_result = check_memory()
    network_result = check_network()
    check_results = {"cpu": cpu_result, "memory": memory_result, "network": network_result}
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
        status = results[check_type]["status"]
        report += (f"{check_type}: {status}\n")
    return report

def main():
    try:    
        check_results = run_checks()
        report_string = generate_report(check_results)
        print (report_string)
        log_results(check_results, "monitor.log")
    except ThresholdExceededError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
