# ContactBookApp app

### Functions:
- Add, edit, and delete contacts
- View and search contacts by name in real-time
- Toggle between light and dark mode

### Features:
- Collapsible Add Contact' section for wider view of contact list
- Input validation to prevent nameless contacts
- Card-based UI with icons for contact details
- Confirmation dialog before deleting a contact

## How It Works
- Contacts are stored and managed in `contacts.db` using SQLite.
- UI is built with Flet’s `reactive components` (TextField, ListView, Card, etc.).
- Theme toggling is handled via `FloatingActionButton` and `page.theme_mode`.
- Search field filters contacts using SQL `LIKE` clause.


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