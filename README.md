# Security Log Parser & Automated PGP Encryption Tool

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Cybersecurity](https://img.shields.io/badge/Security-Log%20Analysis%20%26%20PGP-success)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

A robust Python-based security utility engineered to parse system and authentication logs for anomalous access patterns, paired with an automated PGP encryption framework for secure file and data governance.

---

##  Project Motivation & Business Impact
In modern IT and financial environments, protecting sensitive data at rest and in transit is a paramount compliance requirement. Simultaneously, monitoring system logs for unauthorized login attempts or failed authentication events is crucial for proactive threat detection. 

This project showcases core cybersecurity competencies—combining regex-based log parsing with cryptographic key management (OpenPGP/Kleopatra workflows) to ensure enterprise-grade data protection and automated threat auditing.

---

##  Tech Stack & Security Tools
* **Language:** Python (Standard library, Regular Expressions, Subprocess/GnuPG integration)
* **Encryption Standards:** OpenPGP / Gpg4win / Kleopatra keypair management
* **Log Analysis:** Regex pattern matching, structured anomaly detection, automated alerting

---

##  Project Architecture
```text
security-log-parser/
│
├── logs/
│   └── sample_auth.log            # Sample system authentication log for testing
│
├── src/
│   ├── log_parser.py              # Regex parser for detecting failed logins & anomalies
│   └── pgp_encryptor.py           # Automated file encryption utility using PGP keys
│
├── main.py                        # Orchestrator script
└── README.md
