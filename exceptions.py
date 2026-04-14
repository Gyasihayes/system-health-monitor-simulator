# Gyasi Hayes
# 04/13/2026
# Creates the 4 exceptions that will be raised in the monitor.py file
class ServiceUnavailableError(Exception):
    # Raises when a service cannot be reached
    pass
class DataCorruptionError(Exception):
    # Raises when data returned by a service is corrupted
    pass
class ConnectionTimeoutError(Exception):
    # Raises when a service connection times out
    pass
class ThresholdExceededError(Exception):
    # Raises when a metric exceeds it's defined threshold
    pass