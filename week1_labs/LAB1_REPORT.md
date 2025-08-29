# Lab 1 Report: Environment Setup and Python Basics

**Student Name:** Jessica Mae T. Lanuzo
**Student ID:** 231001081
**Section:** A
**Date:** August 27, 2025

## Environment Setup

### Python Installation
- **Python Version:** 3.13.5
- **Installation Issues:** System path needed to be modified to use a newer version of python.
- **Virtual Environment Created:** ✅ cccs106_env_lanuzo

### VS Code Configuration
- **VS Code Version:** 1.103.2
- **Python Extension:** ✅ Installed and configured
- **Interpreter:** ✅ Set to cccs106_env_lanuzo/Scripts/python.exe

### Package Installation
- **Flet Version:** 0.28.3
- **Other Packages:** 
anyio,
certifi,
flet,
h11,
httpcore,
httpx,
idna,
oauthlib,
pip,
repath,
six,
sniffio

## Programs Created

### 1. hello_world.py
- **Status:** ✅ Completed
- **Features:** Student info display, age calculation, system info
- **Notes:** Age calculation feature only considers the birth and current year, so it shows the student's age after their birthday in the current year.

### 2. basic_calculator.py
- **Status:** ✅ Completed
- **Features:** Basic arithmetic, remainder (modulo), power, and square root calculation, error handling, min/max calculation
- **Notes:** Operations are calculated in only one way: <1st num> \<operation> <2nd num>. The calculator can take negative numbers and floats.

## Challenges and Solutions

I had to redo a lot of the steps because I had not organized my directory in advance. These steps include setting up the interpreter and taking the documentation screenshots. To avoid repeating this (as I have encountered the problem while trying tha activity at home), I made the whole directory structure first, and then proceeded to create the simple programs.

Not really a challenge but when I had to screenshot VS Code showing the Python version and interpreter, I could not figure out how to make those two details appear in the status bar. Turns out that just I needed to open a python file first.

For the calculator, I also needed to add error handling to the source code. This was done by simply enclosing the input lines and calculations in a while statement (almost forgot the break statement!). Making the calculator display the division remainder only when the first number is greater than the second also required some specifications, which is just adding an if statement.

## Learning Outcomes

- Modifying system path
    - We have been taught how to modify (reorder) the system path in case you have multiple versions of Python installed but want to use a specific one, but I have never done it myself. For this activity, I encountered this problem and was able to perform this. 
- Creating a virtual environment
    - I used to ignore and click whatever for the python intepreter in VS Code when I run into problems executing programs. In this activity, I learned how to create and use in VS Code a custom environment. Having a set environment for your work ensures and makes it easy to run your code using the same version of the same packages, this applies to the Python version as well. 
- Programming and Documentation
    - Modifying the source codes for the simple programs served as a small review of my knowlege using the Python language, especially in implementing error handling.
    - We have made documentations using jupyter notebooks but never using markdowns alone. Inserting images, aligning text, and previewing the markdown in VS Code were new experiences.

## Screenshots
<div style="text-align: center;">

![Alt text](lab1_screenshots\environment_setup.png "Exercise 1.1: Python Installation and Virtual Environment Setup")

Activated environment and list of packages
<br /><br />

![Alt text](lab1_screenshots\vscode_setup.png "Exercise 1.2: Visual Studio Code Setup")

Installed Python extension and active interpreter (from created environment)
<br /><br />


![Alt text](lab1_screenshots\hello_world_output.png "Exercise 1.3: First Python Programs (Hello World!)")

Output of Hello World! program
<br /><br />

![Alt text](lab1_screenshots\basic_calculator_output.png "Exercise 1.3: First Python Programs (Basic Calculator)")

Output of calculator program

</div>