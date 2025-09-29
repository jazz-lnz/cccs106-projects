import flet as ft 
from database import update_contact_db, delete_contact_db, add_contact_db, get_all_contacts_db 

def display_contacts(page, contacts_list_view, db_conn, search_input=None): 
    """Fetches and displays all contacts in the ListView.""" 
    contacts_list_view.controls.clear() 
    contacts = get_all_contacts_db(db_conn, search_input) 
    for contact in contacts:
        contact_id, name, phone, email = contact 
        contacts_list_view.controls.append( 
            ft.Card(
                content = ft.ListTile( 
                    # Contact Icon (non-customizable)
                    leading=ft.Container( # wrap for adding round border
                        content=ft.Icon(ft.Icons.PERSON, size=30),
                        width=40, # area size
                        height=40,
                        alignment=ft.alignment.center,
                        border=ft.border.all(1, ft.Colors.GREY), # border specification
                        border_radius=20,
                    ),
                    # Contact Name
                    title=ft.Text(name), 
                    # Contact Phone No. and Email (icon and text)
                        # Provides alt text if details were not specified
                        # Adjusts layout to window width
                    subtitle=ft.Row(
                        controls = [
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        ft.Icon(ft.Icons.PHONE, size = 17),
                                        ft.Container( # wrap to specify size of space occupied
                                            content = ft.Text(
                                                phone if phone else "(Not Specified)", 
                                                opacity=0.4 if not phone else 1.0,
                                                overflow = "ellipsis"
                                            ),
                                            width = 120, # text occupies this much space, even when blank
                                        ),
                                    ]
                                ),
                                width=150
                            ),
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        ft.Icon(ft.Icons.EMAIL, size = 18),
                                        ft.Text(
                                            email if email else "(Not Specified)", 
                                            opacity=0.4 if not email else 1.0
                                        )
                                    ]
                                ),
                                width=150
                            )
                        ],
                        wrap = True, # for dynamic wrapping
                        width = page.window.width, # wraps according to window/screen width
                        spacing=5,
                    ),
                    # Three-Dot Menu
                    trailing=ft.PopupMenuButton( 
                        icon=ft.Icons.MORE_VERT, 
                        items=[ 
                            ft.PopupMenuItem( 
                                text="Edit", 
                                icon=ft.Icons.EDIT, 
                                on_click=lambda _, c=contact: open_edit_dialog(page, c, db_conn, contacts_list_view) 
                            ), 
                            ft.PopupMenuItem(), 
                            ft.PopupMenuItem( 
                                text="Delete", 
                                icon=ft.Icons.DELETE, 
                                on_click=lambda _, cid=contact_id: delete_contact(page, cid, db_conn, contacts_list_view) 
                            ), 
                        ], 
                    ), 
                ), 
            ) 
        ) 
    page.update() 
 
def add_contact(page, inputs, contacts_list_view, db_conn): 
    """Adds a new contact and refreshes the list.""" 
    name_input, phone_input, email_input = inputs 

    # I N P U T  V A L I D A T I O N
    # Check for empty name
    if name_input.value.strip() == "":
        name_input.error_text =  "Name cannot be empty"
        page.update()
        return
    
    # F O R  V A L I D  I N P U T S
    add_contact_db(db_conn, name_input.value, phone_input.value, email_input.value) 
    # clear error text & input fields
    name_input.error_text = ""
    for field in inputs: 
        field.value = "" 
 
    display_contacts(page, contacts_list_view, db_conn) 
    page.update() 
 
def delete_contact(page, contact_id, db_conn, contacts_list_view): 
    """Deletes a contact and refreshes the list.""" 
    # C O N F I R M A T I O N  L O G I C
    confirm_delete = ft.AlertDialog(
        modal = True,
        title = ft.Text("Delete contact", text_align = ft.TextAlign.CENTER),
        content = ft.Text("Are you sure you want to delete this contact?", text_align = ft.TextAlign.CENTER),
        actions = [
            ft.TextButton("NO", on_click=lambda e: page.close(confirm_delete)),
            ft.TextButton("YES", on_click=lambda e: [
                delete_contact_db(db_conn, contact_id,),
                display_contacts(page, contacts_list_view, db_conn),
                page.close(confirm_delete)
                ])])

    page.open(confirm_delete)
    page.update()
 
def open_edit_dialog(page, contact, db_conn, contacts_list_view): 
    """Opens a dialog to edit a contact's details.""" 
    contact_id, name, phone, email = contact 
 
    edit_name = ft.TextField(label="Name", value=name) 
    edit_phone = ft.TextField(label="Phone", value=phone) 
    edit_email = ft.TextField(label="Email", value=email) 

    def save_and_close(e): 
        update_contact_db(db_conn, contact_id, edit_name.value, edit_phone.value, edit_email.value) 
        dialog.open = False 
        page.update() 
        display_contacts(page, contacts_list_view, db_conn) 
    
    dialog = ft.AlertDialog( 
        modal=True, 
        title=ft.Text("Edit Contact"), 
        content=ft.Container( # wrap to specify the space occupied by the column
            content=ft.Column(
                controls = [edit_name, edit_phone, edit_email], 
                tight = True # keeps the dialog box small/no vertical stretching
            )
        ),
        actions=[ 
            ft.TextButton("Cancel", on_click=lambda e: setattr(dialog, 'open', False) or page.update()), 
            ft.TextButton("Save", on_click=save_and_close), 
        ], 
    ) 
    
    page.open(dialog)