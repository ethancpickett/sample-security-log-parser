import subprocess
import logging

# Configure logging for encryption operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt_file_pgp(file_path, recipient_email):
    """
    Automates PGP file encryption using system GnuPG commands 
    to secure sensitive exports before transmission or storage.
    """
    output_path = f"{file_path}.gpg"

    # Construct the GPG encryption command
    cmd = [
        "gpg",
        "--batch",
        "--yes",
        "--encrypt",
        "--recipient", recipient_email,
        "--output", output_path,
        file_path
    ]

    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(f"File successfully encrypted: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        logging.error(f"PGP encryption failed: {e.stderr}")
        raise
