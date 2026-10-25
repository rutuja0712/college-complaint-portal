# College Complaint Portal — DevOps Project

A web-based College Complaint Portal built with Flask and deployed using Docker, Jenkins, Kubernetes, AWS EC2, and Terraform. This project demonstrates automated testing, containerization, CI/CD, and cloud deployment.

## Project Overview

The College Complaint Portal allows users to submit complaints and view submitted complaints through a simple web interface and API.

### Features

- Submit and view college complaints
- Health-check endpoint for deployment monitoring
- Automated tests using pytest
- Docker-based application packaging
- Jenkins CI/CD pipeline
- Kubernetes deployment with two replicas in the Minikube environment
- AWS EC2 deployment using Docker
- Terraform configuration to track the existing AWS EC2 instance

## Technologies Used

| Technology | Purpose |
|---|---|
| Python and Flask | Web application and API |
| pytest | Automated testing |
| Git and GitHub | Version control and source code hosting |
| Docker | Containerization |
| Docker Hub | Container image registry |
| Jenkins | CI/CD automation |
| Kubernetes and Minikube | Container orchestration and deployment practice |
| AWS EC2 | Cloud hosting |
| Terraform | Infrastructure as code |

## Architecture

Developer → GitHub → Jenkins → Automated Tests → Docker Build → Docker Hub → Kubernetes Deployment

The application is also deployed directly on AWS EC2 using Docker.

Terraform imports and tracks the existing EC2 instance, allowing its configuration to be checked against the actual AWS infrastructure.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | College Complaint Portal homepage |
| `/health` | Application health check |
| `/api/complaints` | Complaint API |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rutuja0712/college-complaint-portal.git
cd college-complaint-portal
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run automated tests

```bash
pytest -v
```

### 5. Start the application

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## Run with Docker

Pull the published image:

```bash
docker pull rutujaw0712/college-complaint-portal:latest
```

Run the container:

```bash
docker run -d --name college-complaint-portal -p 5000:5000 rutujaw0712/college-complaint-portal:latest
```

Open `http://localhost:5000`.

## AWS Deployment

The application is deployed on an AWS EC2 instance using Docker. The container maps host port 80 to application port 5000.

The `/health` endpoint can be used to verify that the application is responding.

## Terraform

The `terraform/` directory contains:

- `main.tf` — AWS provider and EC2 instance configuration
- `.terraform.lock.hcl` — selected provider version lock file
- `.gitignore` — excludes local Terraform state and provider files

The existing EC2 instance was imported into Terraform, and `terraform plan` confirmed that the configuration matched the deployed infrastructure at the time of verification.

**Important:** Terraform state is kept locally and is not committed to this repository.

## Kubernetes

The project includes Kubernetes deployment and service manifests. The development environment uses Minikube, with two application replicas and a NodePort service.

## Important Notes

- Complaints are stored in application memory, not in a persistent database. They may be lost when the application restarts, and separate replicas do not share complaint data.
- This project is intended for learning and demonstration. Production use would require persistent storage, authentication, HTTPS, and additional security controls.
- Do not commit passwords, access tokens, AWS credentials, or Terraform state files.

## Author

**Rutuja**

GitHub: [rutuja0712](https://github.com/rutuja0712)
