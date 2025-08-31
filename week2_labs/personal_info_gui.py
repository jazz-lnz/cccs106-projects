# personal_info_gui.py
# CCCS 106 - Week 2 Lab Exercise
# Enhanced Personal Information with GUI

import flet as ft
from datetime import datetime
import re # for input validation

def main(page: ft.Page):
    # Page configuration
    page.title = "Personal Information Manager"
    page.window.width = 600
    page.window.height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Title
    title = ft.Text(
        "Personal Information Manager",
        size=28,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.INDIGO_700
    )
    
    # Input fields
    first_name = ft.TextField(label="First Name", width=280)
    last_name = ft.TextField(label="Last Name", width=280)
    age = ft.TextField(label="Age", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    student_id = ft.TextField(label="Student ID", width=200)
    
    # Dropdown for program
    program_dropdown = ft.Dropdown(
        label="Academic Program",
        width=300,
        options=[
            ft.dropdown.Option("BSCS", "Bachelor of Science in Computer Science"),
            ft.dropdown.Option("BSIT", "Bachelor of Science in Information Technology"),
            ft.dropdown.Option("BSCpE", "Bachelor of Science in Computer Engineering"),
            ft.dropdown.Option("BSIS", "Bachelor of Science in Information Systems"),
        ]
    )
    
    # Radio buttons for year level
    year_level = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="1st", label="1st Year"),
            ft.Radio(value="2nd", label="2nd Year"),
            ft.Radio(value="3rd", label="3rd Year"),
            ft.Radio(value="4th", label="4th Year"),
        ])
    )
    
    # Color picker (simulated with dropdown)
    favorite_color = ft.Dropdown(
        label="Favorite Color",
        width=200,
        options=[
            ft.dropdown.Option("Red"), ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"), ft.dropdown.Option("Yellow"),
            ft.dropdown.Option("Purple"), ft.dropdown.Option("Orange"),
            ft.dropdown.Option("Pink"), ft.dropdown.Option("Black"),
            ft.dropdown.Option("White"), ft.dropdown.Option("Gray"),
        ]
    )
    
    hobbies = ft.TextField(label="Hobbies/Interests", width=400, multiline=True)
    
    # Output container
    output_container = ft.Container(
        content=ft.Text("Fill out the form and click 'Generate Profile' to see your information."),
        bgcolor=ft.Colors.GREY_100,
        padding=15,
        border_radius=10,
        width=550
    )
    
    # Functions
    def generate_profile(e):
        try:
            # Check required inputs
            if not all([first_name.value, last_name.value, age.value]):
                show_error("Please fill in all required fields (Name and Age)!")
                return
            
            # Validate name input
            name_pattern = re.compile(r"^[A-Za-z\s'-]+$")
            if not name_pattern.match(first_name.value) or not name_pattern.match(last_name.value):
                show_error("Names must contain only letters, spaces, hyphens, or apostrophes.")
                return
            
            # Validate age/student ID input
            if not age.value.isdigit():
                show_error("Age must be a whole number (no letters or symbols).")
                return
            if student_id.value and not student_id.value.isdigit():
                show_error("Student ID must be a whole number (no letters or symbols).")
                return
            if student_id.value and int(student_id.value) <= 0:
                show_error("Student ID must be greater than zero.")
                return

            age_int = int(age.value)
            if age_int <= 0:
                show_error("Age must be greater than zero.")
                return
            if age_int > 120:
                show_error("Please enter a realistic age (less than 120).")
                return
            
            # Validate hobbies input
            if hobbies.value and not name_pattern.match(hobbies.value):
                show_error("Hobbies must contain only letters, spaces, hyphens, or apostrophes.")
                return

            # Calculate birth year
            current_year = datetime.now().year
            birth_year = current_year - int(age.value)
            graduation_year = current_year + (4 - int(year_level.value[0]) if year_level.value else 4)
            
            # Generate profile
            profile_content = ft.Column([
                ft.Text("🎓 STUDENT PROFILE", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                ft.Divider(),
                ft.Text(f"👤 Full Name: {first_name.value} {last_name.value}", size=16),
                ft.Text(f"🆔 Student ID: {student_id.value or 'Not provided'}", size=16),
                ft.Text(f"🎂 Age: {age.value} years old", size=16),
                ft.Text(f"📅 Birth Year: {birth_year}", size=16),
                ft.Text(f"📚 Program: {program_dropdown.value or 'Not selected'}", size=16),
                ft.Text(f"📊 Year Level: {year_level.value or 'Not selected'}", size=16),
                ft.Text(f"🎨 Favorite Color: {favorite_color.value or 'Not selected'}", size=16),
                ft.Text(f"🎯 Hobbies: {hobbies.value or 'Not provided'}", size=16),
                ft.Divider(),
                ft.Text(f"🎓 Expected Graduation: {graduation_year}", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(f"📝 Profile generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", 
                       size=12, color=ft.Colors.GREY_600),
            ])
            
            output_container.content = profile_content
            page.update()
            
        except ValueError:
            show_error("Please enter a valid age (number only)!")
        except Exception as ex:
            show_error(f"An error occurred: {str(ex)}")
    
    def clear_form(e):
        first_name.value = ""
        last_name.value = ""
        age.value = ""
        student_id.value = ""
        program_dropdown.value = None
        year_level.value = None
        favorite_color.value = None
        hobbies.value = ""
        output_container.content = ft.Text("Form cleared. Fill out the information again.")
        page.update()
    
    def show_error(message):
        error_dialog = ft.AlertDialog(
            title=ft.Text("Input Error"),
            content=ft.Text(message),
            actions=[ft.TextButton("OK", on_click=lambda e: close_error_dialog(error_dialog))]
        )
        page.open(error_dialog) # Flet's newer dialog API'; recommended method 
        page.update()
    
    def close_error_dialog(dialog):
        page.close(dialog) # Flet's newer dialog API'; recommended method 
        page.update()
    
    # Buttons
    generate_btn = ft.ElevatedButton(
        "Generate Profile",
        on_click=generate_profile,
        bgcolor=ft.Colors.INDIGO_600,
        color=ft.Colors.WHITE,
        width=150
    )
    
    clear_btn = ft.ElevatedButton(
        "Clear Form",
        on_click=clear_form,
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        width=150
    )
    
    # Layout
    page.add(
        ft.Column([
            title,
            ft.Divider(),
            ft.Text("Personal Information", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([first_name, last_name], spacing=20),
            ft.Row([age, student_id], spacing=20),
            program_dropdown,
            ft.Text("Year Level:", size=16, weight=ft.FontWeight.BOLD),
            year_level,
            favorite_color,
            hobbies,
            ft.Divider(),
            ft.Row([generate_btn, clear_btn], spacing=20),
            ft.Divider(),
            ft.Text("Generated Profile:", size=18, weight=ft.FontWeight.BOLD),
            output_container,
        ], spacing=10)
    )

if __name__ == "__main__":
    ft.app(target=main)