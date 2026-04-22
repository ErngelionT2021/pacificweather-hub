# 🌊 PacificWeather Hub

Real-time weather dashboard for Pacific Island nations, deployed on AWS EC2 with automated CI/CD.

**Live Demo:** http://15.134.95.161

---

## 🇸🇧 About This Project

I'm an international student from the Solomon Islands studying Data Science at UNSW Sydney. I built this project to learn AWS cloud engineering while solving something meaningful — giving Pacific Island communities easy access to real-time weather data.

Climate and weather directly affect daily life across the Pacific. This dashboard displays live conditions for Honiara, Apia, Suva, Port Vila and Nuku'alofa, with historical tracking.

---

## ☁️ AWS Architecture
OpenWeather API → AWS EC2 (Flask App) → AWS RDS PostgreSQL
GitHub → GitHub Actions CI/CD → AWS EC2 (Auto Deploy)

| Service | Purpose |
|---|---|
| AWS EC2 t3.micro | Ubuntu Linux server running the app |
| AWS RDS PostgreSQL | Managed database for weather history |
| Elastic IP | Permanent public IP address |
| Security Groups | Firewall — HTTP, HTTPS, SSH rules |
| IAM | Least-privilege user access |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **Database:** PostgreSQL (psycopg2)
- **Container:** Docker, Docker Compose
- **CI/CD:** GitHub Actions → AWS EC2
- **API:** OpenWeatherMap
- **Server:** Ubuntu 24.04 on AWS EC2

---

## 🚀 CI/CD Pipeline

Every `git push` to main automatically:
1. GitHub Actions triggers the workflow
2. SSHes into the EC2 server
3. Pulls latest code
4. Rebuilds Docker containers
5. Restarts the app

Zero manual deployment needed.

---

## 📁 Project Structure
---
pacificweather-hub/
├── .github/workflows/deploy.yml  # CI/CD pipeline
├── app/
│   ├── main.py                   # Flask routes
│   ├── weather.py                # OpenWeather API
│   ├── database.py               # PostgreSQL connection
│   └── templates/                # Dashboard UI
├── Dockerfile                    # Container definition
├── docker-compose.yml            # Multi-container setup
└── requirements.txt              # Python dependencies

## 🌏 Cities Tracked

| City | Country |
|---|---|
| Honiara | 🇸🇧 Solomon Islands |
| Apia | 🇼🇸 Samoa |
| Suva | 🇫🇯 Fiji |
| Port Vila | 🇻🇺 Vanuatu |
| Nuku'alofa | 🇹🇴 Tonga |

---

## 💡 What I Learned

- Launching and managing AWS EC2 instances
- Configuring security groups and VPC networking
- Containerising applications with Docker
- Building automated CI/CD pipelines with GitHub Actions
- Managing PostgreSQL on AWS RDS
- Debugging live production deployments
- Linux server administration via SSH

---

*Built by Erngelion Tora - Solomon Islands student at UNSW Sydney* 🇸🇧