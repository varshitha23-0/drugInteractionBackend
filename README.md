# Drug & Food Interaction Checker — Backend

A Python Flask backend that powers a drug and food interaction checker using a structured medicine knowledge base. It processes requests, matches medicine names, and returns potential interaction information with severity classifications.

## Features

- **Drug–Drug Interaction Checks:** Looks up potential interactions between medicines.
- **Brand-to-Generic Matching:** Supports medicine name matching where mappings are available.
- **Severity Information:** Returns severity classifications based on the available knowledge-base data.
- **Food Interaction Checks:** Supports food-related warnings where the relevant data is available.
- **Structured Knowledge Base:** Uses JSON data for medicine and interaction lookups.
- **REST API:** Exposes backend functionality for the React frontend.

## Tech Stack

- Python
- Flask
- REST APIs
- JSON

## Project Structure

```text
Drug-Interaction-Backend/
├── data/
│   ├── extractdata.py
│   └── top_kb.json
├── app.py
├── Procfile
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or a version supported by the dependencies
- pip

### 1. Clone the repository

```bash
git clone https://github.com/varshitha23-0/drugInteractionBackend
cd drugInteractionBackend
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

### 4. Start the backend

```bash
python app.py
```

Use the local address displayed in the terminal to access the backend. If the application exposes API endpoints, you can test them using a browser or an API client where appropriate.

## Knowledge Base

The `data/top_kb.json` file contains structured information used by the backend for medicine matching and interaction lookups. The `data/extractdata.py` script supports data extraction or preparation.

## Deployment

The `Procfile` specifies a startup command for compatible hosting platforms. Deployment also requires the appropriate Python runtime, installed dependencies, and any required environment configuration.

## Related Project

This backend is designed to work with the React frontend for the Drug & Food Interaction Checker.

Add the frontend repository link here once it is published.

## Disclaimer

This project is intended for educational and informational purposes. Its results depend on the coverage and quality of the underlying data and should not replace advice from a qualified doctor or pharmacist. Do not change medication or dietary instructions based solely on this application.
