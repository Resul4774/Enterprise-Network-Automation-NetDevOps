# Enterprise Multi-Site Network Design & Python Backup Automation (NetDevOps)

This repository showcases a production-grade, multi-site enterprise network infrastructure design integrated with a robust Python automation script for secure configuration audits and dynamic backups via SSH.

## 🌐 Network Architecture & Topology Details
- **Core Design:** Interconnecting autonomous corporate networks between Istanbul (HQ) and Ankara (Branch).
- **Interior Routing (IGP):** Implemented **OSPF (Area 0)** to establish dynamic path selection and high availability within internal local networks. Successfully verified `FULL/DR` neighbor adjacency.
- **Exterior Routing (EGP):** Configured **eBGP (External Border Gateway Protocol)** between Istanbul (AS 65000) and Ankara (AS 65001) to simulate scalable internet routing and cross-site prefix propagation.
- **Validation:** Confirmed end-to-end connectivity across discrete subnets using ICMP ping benchmarks with 0% packet loss.

## 🛠️ Automation Layer (Python + Netmiko)
To eliminate manual intervention and mitigate human errors during compliance tasks, a standalone automation script was engineered:
- Establishes encrypted **SSH v2 (RSA 1024-bit)** channels to infrastructure nodes.
- Programmatically executes security and configuration audits (`show running-config`).
- Captures active configurations and dynamically exports them with localized precision timestamps (`router_config_YYYY-MM-DD-HH-MM-SS.txt`).
- Features modular `try-except` blocks to handle network timeouts or authentication faults cleanly.

## 📁 Repository Structure
- `backup.py`: The production Python automation script.
- `Topology/`: Contains the network infrastructure visual diagrams and connection mappings.

## 🚀 Getting Started
1. Clone this repository to your local system.
2. Install the production dependencies:
   ```bash
   pip install netmiko
   ```
3. Run the automation agent:
   ```bash
   python backup.py
   ```
