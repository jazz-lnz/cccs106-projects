# Userlogin app

### Functions:
- Authenticate users against a MySQL database
- Validate input fields before login attempt
- Display feedback dialogs for success, failure, or input errors

### Features:
- Frameless and centered login window following specified styling
- Input fields for username and password with icons and helper text
- Password field supporting hiding and revealing input
- Alert dialogs for login success, failure, input errors, and database issues

## How It Works
- User credentials are stored in a `MySQL database` (fletapp) under the users table.
- UI is built using `Flet’s reactive components` (TextField, ElevatedButton, Dialog, etc.).
- Login logic is handled via an asynchronous `login_click` function. 
*(asynchronous: UI stays responsive while waiting for login results)*
- `Input validation` checks for empty fields before querying the database.
- Authentication uses `parameterized SQL queries` to prevent injection.
- Feedback is provided through styled `AlertDialog` components based on login outcome.


## Run the app

Requirements:
- Python 3.10+
- Flet (pip install flet)

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).