# enhanced_calculator.py 
# CCCS 106 - Week 2 Lab Exercises (Optional)
# Enhanced calculator GUI

# hello_flet.py
# CCCS 106 - Week 2 Lab Exercise
# First Flet GUI Application
# Student: [Your Name]

import flet as ft

def main(page: ft.Page):
    # Page configuration
    page.title = "Enhanced Calculator"
    page.window.width = 400
    page.window.height = 600
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Input fields
    a = ft.TextField(
        label="First Number",
        width=100,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    b = ft.TextField(
        label="Second Number",
        width=100,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    # Output container
    output = ft.Text(
        value="", 
        size=14, 
        selectable=True)
    
    # Calculation function
    def calculate(e):
        try:
            num1 = float(a.value)
            num2 = float(b.value)
            
            # Basic calculations
            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            
            # Handle division by zero
            modulo = ''

            if num2 != 0:
                division = num1 / num2
                if num1 > num2:
                    modulo = f"(r. {num1 % num2})"
            else:
                division = "Cannot divide by zero"
            
            # Additional operations
            exponent = num1**num2
            sqroot1 = num1**0.5
            sqroot2 = num2**0.5
            larger = max(num1, num2)
            smaller = min(num1, num2)

            # Results
            result = (
            f"RESULTS:\n"
            f"\n{num1} + {num2} = {addition}\n"
            f"{num1} - {num2} = {subtraction}\n"
            f"{num1} * {num2} = {multiplication}\n"
            f"{num1} / {num2} = {division} {modulo}\n"
            f"\n{num1} ^ {num2} = {exponent}\n"
            f"√{num1} = {sqroot1}\n"
            f"√{num2} = {sqroot2}\n"
            f"\nLarger number: {larger}\n"
            f"Smaller number: {smaller}"
            )

            output.value = result

        except ValueError:
            output.value = "***Error: Please enter valid numbers only!"
        except Exception as ex:
            output.value = f"***An error occurred: {ex}"

        page.update()

    # Calculate Button
    calc_button = ft.ElevatedButton(
        "Calculate",
        on_click = calculate
    )

    # Layout
    page.add(
        ft.Column([
            ft.Text("Enhanced Calculator", size=24, weight=ft.FontWeight.BOLD),
            a,
            b,
            calc_button,
            ft.Divider(),
            output
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

# Run the application
if __name__ == "__main__":
    ft.app(target=main)