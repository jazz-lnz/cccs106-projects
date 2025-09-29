import flet as ft 
from database import init_db 
from app_logic import display_contacts, add_contact 
 
def main(page: ft.Page): 
    page.title = "Contact Book" 
    page.vertical_alignment = ft.MainAxisAlignment.START 
    page.window_width = 400 
    page.window_height = 600 
 
    # Title/App Bar
    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Contact Book"),
        center_title=True,
        bgcolor=ft.Colors.GREY,
    )
 
    db_conn = init_db() 
 
    name_input = ft.TextField(label="Name", width=350) 
    phone_input = ft.TextField(label="Phone", width=350) 
    email_input = ft.TextField(label="Email", width=350) 
 
    inputs = (name_input, phone_input, email_input) 
 
    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=False) 
 
    add_button = ft.ElevatedButton( 
        text="Add Contact", 
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn) 
    ) 
 
    # FEATURE: Collapsible Add Contact Fields
    expansion_add = ft.ExpansionTile(
        leading = ft.Icon(ft.Icons.ADD),
        title=ft.Text("Add Contact:", size=20, weight=ft.FontWeight.BOLD),
        affinity=ft.TileAffinity.PLATFORM,
        maintain_state=True,
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        name_input,
                        phone_input,
                        email_input,
                        ft.Row(
                            controls=[add_button],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=ft.padding.symmetric(vertical=10)  # Adds space above and below
            )
        ]
    ) 

    # FEATURE: Contact Search
    search_input = ft.TextField(
        width=350,
        label = "Search Contacts",
        helper_text = "Enter the name of the contact you want to find",
        prefix_icon = ft.Icons.SEARCH,
        on_change = lambda e: display_contacts(page, contacts_list_view, db_conn, e.control.value) 
        # ^ triggers search function (get_all_contacts_db) everytime the user types on the search box
        ) 
    
    # FEATURE: Light/Dark Mode Display
    page.theme_mode = ft.ThemeMode.LIGHT
    dark_mode = False
    def switch_mode(e):
        nonlocal dark_mode, page_theme_button # assign changes to already declared variables (outside the function)
        dark_mode = not dark_mode
        page.theme_mode = ft.ThemeMode.DARK if dark_mode else ft.ThemeMode.LIGHT
        page_theme_button.icon = (ft.Icons.LIGHT_MODE if dark_mode else ft.Icons.NIGHTS_STAY_OUTLINED)
        page.update()

    page_theme_button = ft.FloatingActionButton(
        icon = ft.Icons.NIGHTS_STAY_OUTLINED,
        on_click = switch_mode
    )
    page.floating_action_button = page_theme_button
    
 
    page.add( 
        ft.Column(
            [ 
                ft.Container(
                    content = expansion_add,
                    width = 400,
                    alignment = ft.Alignment(0.0, 0.0)
                ),
                ft.Divider(), 
                ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
                search_input,
                contacts_list_view, 
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, # center-align UI
            expand=True
        ) 
    ) 
 
    display_contacts(page, contacts_list_view, db_conn) 
 
if __name__ == "__main__": 
    ft.app(target=main)