from src.log_parser import parse_auth_logs
from src.pgp_encryptor import encrypt_file_pgp
import os

def run_security_workflow():
    print("--- Starting Security & Encryption Pipeline ---")

    # 1. Parse authentication logs for failed login anomalies
    log_path = "logs/sample_auth.log"
    if os.path.exists(log_path):
        anomalies = parse_auth_logs(log_path)
        print(f"Detected failed login attempts from IPs: {anomalies}")
    else:
        print(f"Log file not found at {log_path}")

    # 2. Example PGP Encryption workflow (uncomment when keys/files are configured)
    # target_file = "logs/sample_auth.log"
    # recipient = "security@domain.com"
    # encrypt_file_pgp(target_file, recipient)

    print("--- Security Pipeline Completed Successfully ---")

if __name__ == "__main__":
    run_security_workflow()
