# Advanced System Monitoring & Activity Logger

## Overview

Advanced System Monitoring & Activity Logger is a cybersecurity learning project developed during an internship to understand system monitoring, endpoint visibility, event collection, and secure reporting mechanisms.

The application demonstrates how administrative monitoring tools can collect and report system activity while maintaining transparency by notifying users that monitoring is active.

> **Disclaimer:** This project was developed strictly for educational, research, and internship learning purposes. It must only be used on systems where explicit authorization and consent have been obtained. Unauthorized monitoring of users or devices is illegal and unethical.

---

## Features

### Activity Monitoring

* Records keyboard input events for learning and analysis purposes.
* Tracks user activity patterns on authorized systems.

### Real-Time Screenshots

* Captures screenshots at configurable intervals.
* Helps demonstrate endpoint monitoring and activity auditing concepts.

### Network Information Collection

* Retrieves network-related information, including:

  * Connected network details
  * IP address information
  * Network adapter information

### Device Information Gathering

* Collects system information such as:

  * Operating System details
  * Hostname
  * Device specifications
  * User environment information

### Email-Based Reporting

* Generates structured reports.
* Sends collected information to the designated administrator email when required.
* Supports centralized monitoring and analysis.

### User Transparency & Consent

* Displays a notification/pop-up informing the user that monitoring is active.
* Ensures users are aware that collected information may be transmitted to an authorized administrator.
* Designed with ethical monitoring principles in mind.

---

## Technology Stack

* Python
* SMTP Email Services
* System Information APIs
* Screenshot Capture Libraries
* Network Information Utilities

---

## Learning Objectives

This project was built to gain hands-on experience with:

* Endpoint monitoring concepts
* Event logging mechanisms
* System information gathering
* Email automation
* Cybersecurity monitoring techniques
* Responsible security tool development

---

## Ethical Considerations

This project follows the principles of:

* User awareness
* Administrative authorization
* Transparency
* Responsible disclosure
* Educational use only

The application includes user notification mechanisms to inform individuals that monitoring is being performed and that collected information may be shared with an authorized administrator.

---

## Installation

```bash
git clone https://github.com/yourusername/advanced-system-monitor.git

cd advanced-system-monitor

pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

Upon execution:

1. The user receives a monitoring notification.
2. System and network information are collected.
3. Activity logs and screenshots are generated.
4. Reports can be sent to the authorized administrator via email.

---

## Security Notice

This software is intended solely for:

* Cybersecurity education
* Research environments
* Authorized administrative monitoring
* Internship and academic projects

Do not deploy this software on devices without explicit permission from the owner or user.

---

## Author

**Mayank Shekhar**

Cybersecurity Enthusiast | Network Security | Ethical Hacking | Security Research

---

## License

This project is provided for educational and research purposes only. Users are responsible for ensuring compliance with all applicable laws, regulations, and organizational policies before deployment or use.
