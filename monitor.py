# Gyasi Hayes
# 04/17/2026
# A Program that runs checks on different parts of a computer system, then prints them to a separate file and outputs them.
import cpu_monitor
import memory_monitor
import network_monitor
from exceptions import(ServiceUnavailableError, DataCorruptionError, ConnectionTimeoutError, ThresholdExceededError)

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0

def check_cpu():
    """
    Checks the cpu data usage and compares it to the threshold
    No parameters
    Returns a dictionary containing the status of the system if it's healthy or there's an error
    """
    try:
        cpu_data = cpu_monitor.get_cpu_metrics()
        if cpu_data['usage_percent'] > CPU_THRESHOLD: # Checks to see if the CPU data is above the CPU threshold
            raise ThresholdExceededError("CPU Threshold Exceeded") # Raises a custom exception but doesn't catch it yet
        return{"status": "healthy", "data": cpu_data}
    except ServiceUnavailableError:
        return{"status": "error", "data": "Service Unavailable"} # Raises a custom exception but doesn't catch it yet
    
def check_memory():
    """
    Checks the memeory usage and compares it to the threshold
    No parameters
    Returns a dictionary containing the status of the system if it's healthy or there's an error
    """   
    try:
        memory_data = memory_monitor.get_memory_metrics()
        if memory_data['usage_percent'] > MEMORY_THRESHOLD: # Checks to see if the memory data is above the threshold
            raise ThresholdExceededError("Memory Threshold Exceeded") # Raises a custom exception but doesn't catch it yet
        return{"status": "healthy", "data": memory_data}
    except DataCorruptionError:
        return{"status": "error", "data": "Data Corrupted"} # Raises a custom error and returns an error message
   
    
def check_network():
    """
    Checks the network data usage and compares it to the threshold
    No parameters
    Returns a dictionary containing the status of the system if it's healthy or there's an error
    """    
    try:
        network_data = network_monitor.get_network_metrics()
        if network_data['usage_percent'] > NETWORK_THRESHOLD: # Checks to see if the network usage is above the threshold
            raise ThresholdExceededError("Network Threshold Exceeded") # Raises a custom exception but doesn't catch it yet
        return {"status": "healthy", "data": network_data}
    except ConnectionTimeoutError:
        return{"status": "error", "data": "Connection Timeout"} # Raises a custom exception but doesn't catch it yet


def run_checks():
    """
    Calls the check functions to see if their is one of 3 errors, ServiceUnavailableError, DataCorruptionError, or ConnectionTimeoutError
    No parameters
    Returns a dictionary containing results of the checks
    """    
    cpu_result = check_cpu() #Runs the checks
    memory_result = check_memory()
    network_result = check_network()
    check_results = {"cpu": cpu_result, "memory": memory_result, "network": network_result} 
    # Creates a dictionary with the results of the checks
    return check_results

def log_results(results, filepath):
    """
    Appends the results from the check to a file
    The parameters are: results(the dictionary containing the results from the checks), and filepath(the filepath)
    No returns
    """     
    try:
        with open(filepath, "a") as file: # Opens a new file to append the results of the checks to it
            file.write(f"Results {results}\n")
            file.write("Results Logged\n")
    except Exception as error:
        print(f"Could not write to file: {error}") # Catches all excptions in case something goes wrong

def generate_report(results):
    """
    Parses through the data and creates a report string to be outputted later
    The parameter is results, which is the dictionary containing the results from the checks
    Returns the report string
    """    
    report = "SYSTEM REPORT\n"
    for check_type in results: # Loops through the results to grab the name of the check and the status from the result dictionary
        status = results[check_type]["status"]
        report += (f"{check_type}: {status}\n")
    return report

def main():
    """
    Calls the functions and outputs the formatter report, or an error message.
    No parameters
    No returns
    """      
    try:    
        check_results = run_checks() 
        report_string = generate_report(check_results)
        print (report_string)
        log_results(check_results, "monitor.log") # Outputs the results
    except ThresholdExceededError as error: # Finally catches the ThresholdExceeded errors back from the check functions.
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
