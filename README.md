# CCCS 106 Projects
Application Development and Emerging Technologies  
Academic Year 2025-2026

## Student Information
- **Name:** Jessica Mae T. Lanuzo
- **Student ID:** 231001081
- **Program:** Bachelor of Science in Computer Science
- **Section:** 3A

## Repository Structure

### Week 1 Labs - Environment Setup and Python Basics
- `week1_labs/hello_world.py` - Basic Python introduction
- `week1_labs/basic_calculator.py` - Simple console calculator
- `week1_labs/LAB1_REPORT.md` - Lab 1 documentation

### Week 2 Labs - Git and Flet GUI Development
- `week2_labs/hello_flet.py` - First Flet GUI application
- `week2_labs/personal_info_gui.py` - Enhanced personal information manager
- `week2_labs/enhanced_calculator.py` - GUI calculator (work in progress)
- `week2_labs/LAB2_REPORT.md` - Lab 2 documentation

### Week 3 Labs - User Login App with MySQL
- `week3_labs/` (userlogin) - Frameless login GUI with database authentication
- `week3_labs/db_connection.py` - Modular MySQL connector
- `week3_labs/LAB3_REPORT.md` - Lab 3 documentation

### Week 4 Labs - Contact Book App Enhancement
- `week4_labs/contact_book_app/` - Enhanced contact manager with theme toggle and search
- `week4_labs/database.py` - SQLite backend
- `week4_labs/app_logic.py` - Modular logic handling
- `week4_labs/LAB4_REPORT.md` - Lab 4 documentation

### Module 6 Labs - Weather Application Enhancement
- `mod6_labs/main.py` – Main Flet application with city search, current weather display, search history, 5‑day forecast, and theme toggle
- `mod6_labs/weather_service.py` – Service layer handling OpenWeatherMap API calls (current weather + forecast)
- `mod6_labs/config.py` – Configuration management (API key, app dimensions, base URL)
- `mod6_labs/README.md` – Documentation with feature descriptions, usage instructions, and screenshots
- `.env.example` – Example environment file for API key setup

### Module 1 Final Project
- `module1_final/` - Final integrated project (TBD)

## Technologies Used
- **Python 3.8+** - Main programming language
- **Flet 0.28.3** - GUI framework for cross-platform applications
- **Git & GitHub** - Version control and collaboration
- **VS Code** - Integrated development environment

## Development Environment
- **Virtual Environment:** cccs106_env
- **Python Packages:** flet==0.28.3
- **Platform:** Windows 10/11

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