# AutoSecure: AI-Powered IT Compliance Assistant 🛡️💻

AutoSecure is a lightweight, simulated IT compliance assistant built in Python. Inspired by real-world internal IT and security workflows, this tool is designed to emulate core functionalities of an AI assistant used for managing compliance, device security, and access control across a modern hybrid organization.

> ⚙️ Built for demo purposes — ideal as a portfolio project for IT, security, and DevOps professionals.

---

## 🔍 Features

- **Slack-Style Bot Responses**
  - Returns compliance status of user devices (encryption, firewall, updates).
- **Access Review Agent**
  - Checks user roles and flags potential privilege risks.
- **Audit Summary Generator**
  - Outputs a consolidated SOC 2-style audit report.

---

## 📂 Project Structure

```plaintext
autosecure_agent.py   # Main Python script with simulated logic
```

---

## 🚀 How to Run

### 1. Install Python (if not already installed)

Check if Python is available:

```bash
python3 --version
```

If not installed:

```bash
brew install python
```

### 2. Clone or Download the Script

If downloaded from GitHub:

```bash
git clone https://github.com/your-username/autosecure.git
cd autosecure
```

Or move the file to your working folder if downloaded manually.

### 3. Run the Script

```bash
python3 autosecure_agent.py
```

---

## 🧠 Example Output

```
Slack Bot Response for jane.doe@company.com:
⚠️ Device for jane.doe@company.com is non-compliant on: updates

Access Review for user_1:
{
  "email": "jane.doe@company.com",
  "roles": ["admin", "billing"],
  "compliance_flags": ["excessive_privileges"],
  "status": "⚠️ Review needed"
}

Audit Summary Report:
{
  ...
}
```

---

## 🛠 Technologies Used

- Python 3
- JSON data structures
- Terminal CLI
- Simulated logic (no external API calls)

---

## 📌 Disclaimer

This project is a mock/demo script designed for educational and portfolio purposes. It does **not** integrate with real systems (e.g., Jamf, Okta, Google Workspace) but provides a realistic architecture for how such systems might be modeled.

---

## 📫 Contact

Built by [Your Name](https://www.linkedin.com/in/your-profile/)  
Want help turning this into a web app or Slack bot? Drop me a message!
