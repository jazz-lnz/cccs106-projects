# CCCS 106 Projects
Application Development and Emerging Technologies
Academic Year 2025-2026

## Student Information
- **Name:** Jessica Mae T. Lanuzo
- **Student ID:** 231001081
- **Program:** Bachelor of Science in Computer Science
- **Section:** 3A

---

## Project Overview
This repository serves as an individual learning portfolio for **CCCS 106 (Application Development and Emerging Technologies)**. It documents the progressive development of cross-platform Graphical User Interface (GUI) applications in Python using the Flet framework—moving from basic console scripts to full-featured desktop applications integrated with relational databases and live third-party REST APIs.

## Methodology
The projects in this portfolio were developed using an iterative, modular software engineering approach:
1. **UI & Logic Separation:** Applications are structured to separate front-end Flet UI components (`main.py`) from back-end business logic (`app_logic.py`, `weather_service.py`) and configuration settings (`config.py`).
2. **Database Integration:** Implemented persistent data storage and authentication workflows using both client-server relational databases (**MySQL** in Week 3) and embedded local databases (**SQLite** in Week 4).
3. **API Consumption & Security:** Connected to the **OpenWeatherMap REST API** (Module 6) to fetch real-time meteorological and 5-day forecast data, utilizing environment variables (`.env`) to secure API keys.
4. **Documentation & Version Control:** Tracked iterative enhancements using Git and documented technical implementations, testing, and reflections in dedicated Markdown lab reports (`LAB1_REPORT.md` through `LAB4_REPORT.md`).

## Results & Key Outcomes
- **Functional GUI Suite:** Successfully built and tested 5 progressive modules featuring responsive layouts, custom frameless windows, and dynamic light/dark theme toggling.
- **Secure Authentication & CRUD Operations:** Achieved working database authentication in the User Login App and full Create, Read, Update, and Delete (CRUD) search functionality in the Contact Book App.
- **Real-Time Data Fetching:** Delivered a complete Weather Application capable of querying live global weather conditions, maintaining user search history, and parsing multi-day forecasts.

---

## Repository Structure

### Week 1 Labs – Environment Setup and Python Basics
- `week1_labs/hello_world.py` – Basic Python introduction
- `week1_labs/basic_calculator.py` – Simple console calculator
- `week1_labs/LAB1_REPORT.md` – Lab 1 documentation

### Week 2 Labs – Git and Flet GUI Development
- `week2_labs/hello_flet.py` – First Flet GUI application
- `week2_labs/personal_info_gui.py` – Enhanced personal information manager
- `week2_labs/enhanced_calculator.py` – GUI calculator (work in progress)
- `week2_labs/LAB2_REPORT.md` – Lab 2 documentation

### Week 3 Labs – User Login App with MySQL
- `week3_labs/` (`userlogin`) – Frameless login GUI with database authentication
- `week3_labs/db_connection.py` – Modular MySQL connector
- `week3_labs/LAB3_REPORT.md` – Lab 3 documentation

### Week 4 Labs – Contact Book App Enhancement
- `week4_labs/contact_book_app/` – Enhanced contact manager with theme toggle and search
- `week4_labs/database.py` – SQLite backend
- `week4_labs/app_logic.py` – Modular logic handling
- `week4_labs/LAB4_REPORT.md` – Lab 4 documentation

### Module 6 Labs – Weather Application Enhancement
- `mod6_labs/main.py` – Main Flet application with city search, current weather display, search history, 5-day forecast, and theme toggle
- `mod6_labs/weather_service.py` – Service layer handling OpenWeatherMap API calls (current weather + forecast)
- `mod6_labs/config.py` – Configuration management (API key, app dimensions, base URL)
- `mod6_labs/README.md` – Documentation with feature descriptions, usage instructions, and screenshots
- `.env.example` – Example environment file for API key setup

### Module 1 Final Project
- `module1_final/` – Final integrated project (TBD)

---

## Technologies & Development Environment
- **Language:** Python 3.8+
- **GUI Framework:** Flet 0.28.3 (`flet==0.28.3`)
- **Databases & APIs:** MySQL, SQLite, OpenWeatherMap API
- **Tools & Platform:** Git, GitHub, VS Code, Windows 10/11 (Virtual Environment: `cccs106_env`)

---

## How to Run Applications

### Prerequisites
1. Python 3.8+ installed
2. Virtual environment activated: `cccs106_env\Scripts\activate`
3. Flet installed: `pip install flet==0.28.3`

### Running GUI Applications
```cmd
# Navigate to project directory
cd week2_labs

# Run applications
python hello_flet.py
python personal_info_gui.py

# Run applications (with hot reload)
flet run hello_flet.py
flet run personal_info_gui.py

# for week 3 and 4 labs
cd week3_labs # or cd week4_labs
flet run
