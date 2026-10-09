# Drug & Food Interaction Checker

An application that checks potential drug–drug and drug–food interactions using a structured knowledge base. It maps brand names to generic medicines and provides interaction severity information to help users identify potential risks.

## Features

- **Drug Interaction Checking:** Checks medicines for potential interactions.
- **Brand-to-Generic Mapping:** Helps match brand names with generic medicine names.
- **Severity Classification:** Displays interaction severity categories such as low, medium, and severe, according to the available data.
- **Food Interaction Checking:** Provides food-related warnings when supported by the knowledge base.
- **Structured Knowledge Base:** Uses JSON data to support medicine matching and interaction lookups.
- **REST API:** Provides a Flask backend for application requests.

## Tech Stack

- Python
- Flask
- REST API
- JSON-based knowledge base

## Project Structure

```text
Drug-Food-Interaction-Checker/
├── data/
│   ├── extractdata.py
│   └── top_kb.json
├── app.py
├── Procfile
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend

```bash
python app.py
```

Use the local URL shown in the terminal to access the backend, or test its API endpoints using a suitable API client.

## Purpose

This project explores how structured medicine information and backend APIs can help users identify potential drug and food interactions.

## Disclaimer

This tool is for informational and educational purposes only. It does not replace advice from a qualified healthcare professional. Always consult a doctor or pharmacist before changing medication or dietary instructions.
