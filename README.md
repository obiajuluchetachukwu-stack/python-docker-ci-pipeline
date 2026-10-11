
# Containerized Data Ingestion Pipeline with Python, Docker, and GitHub Actions

Automating data extraction pipelines requires consistency across development and production environments. Differences in host operating systems or python dependency versions frequently lead to runtime errors when deploying code to cloud servers.

This repository demonstrates how to containerize an automated Python data pipeline using **Docker** and validate image compilation continuously with **GitHub Actions CI/CD**.

---

## Architectural Workflow

1. **Python Ingestion Core:** Connects to an external REST API, parses market records using `pandas`, computes rolling statistics, and handles network degradation gracefully.
2. **Containerization (Docker):** Packages application code, OS dependencies, and execution contexts into an isolated, lightweight container image.
3. **Automated Testing (CI/CD):** Triggers automated builds and execution tests on every `git push` via GitHub Actions workflows.

---

## Prerequisites

Before running this project, verify that your development environment contains:
- **Python 3.10** or higher
- **Docker Engine** / Docker Desktop
- **Git** version control

---

## Local Setup & Execution

### Option 1: Running Directly with Python

1. Clone the repository:
   ```bash
   git clone [https://github.com/obiajuluchetachukwu-stack/python-docker-ci-pipeline.git](https://github.com/obiajuluchetachukwu-stack/python-docker-ci-pipeline.git)
   cd python-docker-ci-pipeline

```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. Install project dependencies:
```bash
pip install -r requirements.txt

```


4. Run the data extraction script:
```bash
python app/main.py

```



---

### Option 2: Running Inside a Docker Container

Containerization guarantees that the application runs identically on local machines, staging environments, and cloud infrastructure.

1. Build the Docker container image:
```bash
docker build -t python-data-pipeline .

```


2. Execute the containerized application:
```bash
docker run --rm -v $(pwd)/output:/app/output python-data-pipeline

```



---

## Automated CI/CD Pipeline

This project uses **GitHub Actions** for automated build testing. The configuration file located at `.github/workflows/ci.yml` performs the following steps on every pull request or main branch update:

- Clones the repository codebase.
- Installs required Python dependencies.
- Verifies script execution and syntax.
- Compiles the production Docker image to confirm container stability.
- 
