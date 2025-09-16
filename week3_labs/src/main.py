import flet as ft
import mysql.connector
from db_connection import connect_db

def main(page: ft.Page):

    # W I N D O W   L A Y O U T
    page.title = "User Login"
    page.window.height = 350
    page.window.width = 400
    page.window.alignment = ft.Alignment(0.0, 0.0)
    page.bgcolor = ft.Colors.AMBER_ACCENT
    page.window.frameless = True
    page.window.title_bar_hidden = True

    # Align everything to center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.symmetric(vertical=50) # compress page contents to vertical center

    # C O N T E N T S
    # Title
    title = ft.Text("User Login", 
                                size=20, 
                                weight=ft.FontWeight.BOLD,
                                font_family = "Arial",
                                text_align=ft.TextAlign.CENTER)

    # Text fields
    username_input = ft.TextField(
        icon = ft.Icons.PERSON,
        label = "User name", 
        hint_text = "Enter your user name",
        helper_text = "This is your unique identifier",
        autofocus = True,
        bgcolor = ft.Colors.LIGHT_BLUE_ACCENT,
        width = 300
        )
    
    password_input = ft.TextField(
        icon = ft.Icons.PASSWORD,
        label = "Password", 
        hint_text = "Enter your password",
        helper_text = "This is your secret key",
        password = True,
        can_reveal_password = True,
        bgcolor = ft.Colors.LIGHT_BLUE_ACCENT,
        width = 300
        )
    
    # Login function & button
    def login_click(e):
        success_dialog = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(
                        name=ft.Icons.CHECK_CIRCLE, 
                        color=ft.Colors.GREEN, 
                        size=25
                    ), 
            title=ft.Text("Login Successful", text_align = ft.TextAlign.CENTER),
            content=ft.Text(f"Welcome, {username_input.value}!", text_align = ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(success_dialog))],
            )
        
        failure_dialog = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(
                        name=ft.Icons.ERROR, 
                        color=ft.Colors.RED, 
                        size=25
                    ), 
            title=ft.Text("Login Failed", text_align = ft.TextAlign.CENTER),
            content=ft.Text("Invalid username or password", text_align = ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(failure_dialog))]
            )
        
        invalid_input_dialog = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(
                        name=ft.Icons.ERROR, 
                        color=ft.Colors.BLUE, 
                        size=25
                    ), 
            title=ft.Text("Input Error", text_align = ft.TextAlign.CENTER),
            content=ft.Text("Please enter username and password", text_align = ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(invalid_input_dialog))]
            )
        
        database_error_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Database Error"),
            content=ft.Text("An error occurred while connecting to the database"),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(database_error_dialog))]
            )
        
        # I N P U T  V A L I D A T I O N
        # Check for empty inputs
        if username_input.value.strip() == "" or password_input.value.strip() == "":
            page.open(invalid_input_dialog)
            return

        # Database validation 
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s", 
                (username_input.value, password_input.value)
            ) # parameterized query
            data = cursor.fetchone()
            conn.close()

            if data:
                page.open(success_dialog)
            else:
                page.open(failure_dialog)
            page.update()

        except:
            page.open(database_error_dialog)
            page.update()

    login_button = ft.ElevatedButton("Login", 
                                     on_click = login_click,
                                     width = 100,
                                     icon = ft.Icons.LOGIN)

    # C O N T R O L S  A R R A N G E M E N T
    page.add(
        title,
        ft.Container(
            content = ft.Column(
                controls=[username_input, password_input],
                spacing = 20,
            ),
            expand=True
        ),
        ft.Container(
            content = login_button,
            alignment = ft.alignment.top_right,
            margin=ft.Margin(0, 20, 40, 0),
            padding=ft.padding.only(right=10) # align button with input field edges
        )
)

ft.app(target = main)