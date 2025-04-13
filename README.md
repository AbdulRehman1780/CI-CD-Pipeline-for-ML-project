# CI/CD Pipeline for ML Project using Jenkins & Docker

This project demonstrates a complete CI/CD pipeline for a Machine Learning project using **Jenkins**, **Docker**, and **GitHub**. The pipeline automates testing, building Docker images, and deployment processes.

---

## Project Overview

This repository simulates an end-to-end CI/CD workflow for an ML application. Whenever changes are pushed to the main branch, Jenkins automatically:

1. **Clones the repository**
2. **Builds a Docker image**
3. **Runs tests using pytest**
4. **Pushes the Docker image to Docker Hub**
5. **Deploys the application**
6. **Sends an email notification to the admin upon success**

---

## Technologies Used

- Jenkins (inside Docker)
- Docker & Docker Hub
- GitHub (SCM)
- Ngrok (for webhook tunneling)
- Python, Pytest
- Email Notification Plugin

---

## Project Setup

### 1. Clone this Repository

```bash
git clone https://github.com/AbdulRehman1780/CI-CD-Pipeline-for-ML-project.git
cd CI-CD-Pipeline-for-ML-project
```

### 2. Start Jenkins using Docker

```bash
docker run -d --name jenkins \
-p 8080:8080 -p 50000:50000 \
-v jenkins_home:/var/jenkins_home \
jenkins/jenkins:lts
```

* Access Jenkins at http://localhost:8080

### Jenkins Setup

1. **Install Plugins**:
   * Git
   * Docker Pipeline
   * Email Extension
   * Pipeline
   
2. **Create a Pipeline Job**:
   * Select "Pipeline script from SCM"
   * SCM: Git
      * Repo: `https://github.com/AbdulRehman1780/CI-CD-Pipeline-for-ML-project.git`
      * Branch: `main`
   * Script Path: `Jenkinsfile`
   
3. **Add Credentials**:
   * Docker Hub (for push)
   * GitHub (if private repo)

### Setup GitHub Webhook via Ngrok

1. Start Ngrok:

```bash
ngrok http 8080
```

2. Copy the public URL (e.g., `https://abc123.ngrok.io`)
3. Go to GitHub → Settings → Webhooks → Add:
   * Payload URL: `https://your-ngrok-url/github-webhook/`
   * Content Type: `application/json`
   * Event: **Just the push event**

### ⚙️ Run the Pipeline

Push any change to `main` branch:

```bash
git add .
git commit -m "Trigger CI/CD"
git push origin main
```

Jenkins will automatically run the following:
* Checkout code
* Build Docker image
* Run unit tests (via `pytest`)
* Push image to Docker Hub
* Echo "Deploying..." message
* Send email notification to admin

### Project Structure

```
CI-CD-Pipeline-for-ML-project/
├── app/                # ML Application Code
├── tests/              # Unit Tests
├── Dockerfile          # Docker image definition
├── requirements.txt    # Python dependencies
├── Jenkinsfile         # CI/CD Pipeline Definition
└── README.md           # Project Info & Setup
```

### Email Notification

Make sure to configure email in Jenkins (SMTP) and use the Email Extension plugin to notify admin after successful deployment.

### Note

This project is intended for educational and demonstration purposes. You can expand it to include:
* Model training
* Full deployment to a cloud provider (AWS/GCP/Azure)
* Database connectivity
* Monitoring dashboards

### Author

**Abdul Rehman**
[GitHub](https://github.com/AbdulRehman1780)
