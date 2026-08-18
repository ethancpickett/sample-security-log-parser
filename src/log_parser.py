import re
import logging

# Configure logging for security audit trails
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_auth_logs(file_path):
    """
    Parses system authentication logs using regular expressions 
    to detect failed login attempts and potential brute-force anomalies.
    """
    failed_attempts = 0
    ip_addresses = {}

    # Regex pattern to match failed SSH/system login attempts
    pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    failed_attempts += 1
                    ip = match.group(1)
                    ip_addresses[ip] = ip_addresses.get(ip, 0) + 1

        logging.info(f"Log parsing complete. Total failed logins detected: {failed_attempts}")
        return ip_addresses

    except FileNotFoundError:
        logging.error(f"Log file not found at {file_path}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while parsing logs: {e}")
        raise
