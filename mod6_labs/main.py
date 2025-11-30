"""Weather Application using Flet v0.28.3"""

import flet as ft
from weather_service import WeatherService
from config import Config
import json
from pathlib import Path

class WeatherApp:
    """Main Weather Application class."""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.weather_service = WeatherService()
        self.setup_page()

        # === SEARCH HISTORY ENCHANCEMENT ===
        self.history_file = Path("search_history.json")     # JSON file for history items
        self.search_history = self.load_history()           # initialization of history list (from existing file if exists)

        self.build_ui()

    # File persistence functions
    def load_history(self):
        """Load search history from file."""
        if self.history_file.exists():
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_history(self):
        """Save search history to file."""
        with open(self.history_file, 'w') as f:
            json.dump(self.search_history, f)
    
    # History management function
    # ensures: no duplicate city in history, most recent search is in front,
    # and only last 10 searched city are stored and showed
    def add_to_history(self, city: str):
        """Add city to history."""
        # Remove if already exists (so it can be re-inserted at front)
        if city in self.search_history:
            self.search_history.remove(city)

        # Insert at front
        self.search_history.insert(0, city)

        # Trim to last 10
        self.search_history = self.search_history[:10]
        self.save_history()

        # Refresh chips
        if hasattr(self, "history_chips"):
            self.history_chips.controls = [
                self.create_history_chip(c) for c in self.search_history
            ]
            self.page.update()

    # Function for search history chip creation and format
    def create_history_chip(self, city):
        return ft.Container(
            bgcolor=ft.Colors.BLUE_100,
            padding=ft.padding.symmetric(vertical=2, horizontal=6),
            border_radius=10,
            on_click=lambda e: self.select_from_history(city),
            content=ft.Text(city, size=11, color=ft.Colors.BLUE_900),
        )
    
    # Chip interactivity function (makes them clickable)
    def select_from_history(self, city):
        # Move the clicked city to the front
        if city in self.search_history:
            self.search_history.remove(city)
            self.search_history.insert(0, city)
            self.save_history()

        # Refresh chips visually
        if hasattr(self, "history_chips"):
            self.history_chips.controls = [
                self.create_history_chip(c) for c in self.search_history
            ]
        
        # Makes clicked chip the search input and triggers search
        self.city_input.value = city
        self.page.update()
        self.on_search(None)

    # === 5-DAY FORECAST ENHANCEMENT ===
    def summarize_forecast(self, data: dict) -> dict:
        """Summarize 5-day forecast into daily high/low + condition."""
        days = {}

        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]  # "YYYY-MM-DD"
            temp_min = entry["main"]["temp_min"]
            temp_max = entry["main"]["temp_max"]
            desc = entry["weather"][0]["description"]

            if date not in days:
                days[date] = {"min": temp_min, "max": temp_max, "desc": desc}
            else:
                days[date]["min"] = min(days[date]["min"], temp_min)
                days[date]["max"] = max(days[date]["max"], temp_max)

        return days

    def display_forecast(self, forecast_data: dict):
        """Render 5-day forecast in the UI."""
        days = self.summarize_forecast(forecast_data)

        # Convert date to more readable format
        from datetime import datetime
        
        forecast_rows = []
        for date, info in list(days.items())[:5]:  # Limit to 5 days
            # Convert date to readable format
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            day_name = date_obj.strftime("%a %m/%d")  # e.g., "Mon 11/28" - shorter format
            
            # Create a compact row for each day (horizontal layout)
            row = ft.Container(
                content=ft.Row(
                    [
                        # Day name - fixed width
                        ft.Container(
                            content=ft.Text(
                                day_name,
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_700,
                            ),
                            width=75,
                        ),
                        # High temp
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.ARROW_UPWARD, size=14, color=ft.Colors.RED_400),
                                ft.Text(f"{info['max']:.0f}°", size=13, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=2,
                        ),
                        # Low temp
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.ARROW_DOWNWARD, size=14, color=ft.Colors.BLUE_400),
                                ft.Text(f"{info['min']:.0f}°", size=13),
                            ],
                            spacing=2,
                        ),
                        # Weather description - takes remaining space
                        ft.Container(
                            content=ft.Text(
                                info["desc"].title(),
                                size=12,
                                color=ft.Colors.GREY_700,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            expand=True,
                        ),
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor=ft.Colors.ON_SECONDARY, # for theme adaptaability
                border_radius=8,
                padding=10,
            )
            forecast_rows.append(row)

        # Update forecast container with vertical list of rows
        self.forecast_container.content = ft.Column(
            [
                ft.Text(
                    "5-Day Forecast",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_700,
                ),
                ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
                ft.Column(
                    forecast_rows,
                    spacing=6,
                ),
            ],
            spacing=8,
        )
        self.forecast_container.visible = True
        self.page.update()
    # ===   ===

    def setup_page(self):
        """Configure page settings."""
        self.page.title = Config.APP_TITLE

        # Add theme switcher
        self.page.theme_mode = ft.ThemeMode.SYSTEM  # Use system theme
        
        # Custom theme Colors
        self.page.theme = ft.Theme(
            color_scheme_seed=ft.Colors.BLUE,
        )

        self.page.padding = 20

        # Make vertical scrolling possible
        self.page.scroll = ft.ScrollMode.AUTO

        # Window properties are accessed via page.window object in Flet 0.28.3
        self.page.window.width = Config.APP_WIDTH
        self.page.window.height = Config.APP_HEIGHT
        self.page.window.resizable = False
        self.page.window.center()
    
    def build_ui(self):
        """Build the user interface."""
        # Title
        self.title = ft.Text(
            "Weather App",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_700,
        )
        
        # Theme toggle button
        self.theme_button = ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            tooltip="Toggle theme",
            on_click=self.toggle_theme,
        )

        title_row = ft.Row(
            [
                self.title,
                self.theme_button,
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # City input field
        self.city_input = ft.TextField(
            label="Enter city name",
            hint_text="e.g., London, Tokyo, New York",
            border_color=ft.Colors.BLUE_400,
            prefix_icon=ft.Icons.LOCATION_CITY,
            autofocus=True,
            on_submit=self.on_search,
        )

        # Store search history as a list (row) of chips
        self.history_chips = ft.Row(
            wrap=True,
            spacing=5,
            controls=[
                self.create_history_chip(city) for city in self.search_history
            ]
        )

        # Search button
        self.search_button = ft.ElevatedButton(
            "Get Weather",
            icon=ft.Icons.SEARCH,
            on_click=self.on_search,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_700,
            ),
        )
        
        # Weather display container (initially hidden)
        self.weather_container = ft.Container(
            visible=False,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=10,
            padding=20,
        )

        # Forecast display container (initially hidden)
        self.forecast_container = ft.Container(
            visible=False,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=10,
            padding=20,
        )

        # Error message
        self.error_message = ft.Text(
            "",
            color=ft.Colors.RED_700,
            visible=False,
        )
        
        # Loading indicator
        self.loading = ft.ProgressRing(visible=False)
        
        # Add all components to page
        self.page.add(
            ft.Column(
                [
                    title_row,
                    ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                    self.city_input,
                    self.history_chips, # show search history feature on page
                    self.search_button,
                    ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                    self.loading,
                    self.error_message,
                    self.weather_container,
                    self.forecast_container, # show 5 day forecast feature on page
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )

    def toggle_theme(self, e):
        """Toggle between light and dark theme."""
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_button.icon = ft.Icons.LIGHT_MODE
            # theme compatibility enhancement
            self.weather_container.bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_50)
            self.forecast_container.bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_50)
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_button.icon = ft.Icons.DARK_MODE
            # theme compatibility enhancement
            self.weather_container.bgcolor=ft.Colors.BLUE_50
            self.forecast_container.bgcolor=ft.Colors.BLUE_50 

        self.page.update()

    def on_search(self, e):
        """Handle search button click or enter key press."""
        self.page.run_task(self.get_weather)
    
    async def get_weather(self):
        """Fetch and display weather data."""
        city = self.city_input.value.strip()
        
        # Validate input
        if not city:
            self.show_error("Please enter a city name")
            return
        
        # Show loading, hide previous results
        self.loading.visible = True
        self.error_message.visible = False
        self.weather_container.visible = False
        self.forecast_container.visible = False # added feature
        self.page.update()
        
        try:
            # Fetch and display weather data--current weather
            weather_data = await self.weather_service.get_weather(city)
            await self.display_weather(weather_data)

            # Fetch and display 5-day forecast info
            forecast_data = await self.weather_service.get_forecast(city)
            self.display_forecast(forecast_data)
            
            self.add_to_history(city)   # add searched city to search history

        except Exception as e:
            self.show_error(str(e))
        
        finally:
            self.loading.visible = False
            self.page.update()
    
    async def display_weather(self, data: dict):
        """Display weather information."""
        # Extract data
        city_name = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        temp = data.get("main", {}).get("temp", 0)
        feels_like = data.get("main", {}).get("feels_like", 0)
        humidity = data.get("main", {}).get("humidity", 0)
        description = data.get("weather", [{}])[0].get("description", "").title()
        icon_code = data.get("weather", [{}])[0].get("icon", "01d")
        wind_speed = data.get("wind", {}).get("speed", 0)
        
        # Build weather display
        self.weather_container.content = ft.Column(
            [
                # Location
                ft.Text(
                    f"{city_name}, {country}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                
                # Weather icon and description
                ft.Row(
                    [
                        ft.Image(
                            src=f"https://openweathermap.org/img/wn/{icon_code}@2x.png",
                            width=100,
                            height=100,
                        ),
                        ft.Text(
                            description,
                            size=20,
                            italic=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                # Temperature
                ft.Text(
                    f"{temp:.1f}°C",
                    size=48,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                ),
                
                ft.Text(
                    f"Feels like {feels_like:.1f}°C",
                    size=16,
                    color=ft.Colors.GREY_700,
                ),
                
                ft.Divider(),
                
                # Additional info
                ft.Row(
                    [
                        self.create_info_card(
                            ft.Icons.WATER_DROP,
                            "Humidity",
                            f"{humidity}%"
                        ),
                        self.create_info_card(
                            ft.Icons.AIR,
                            "Wind Speed",
                            f"{wind_speed} m/s"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
        
        self.weather_container.animate_opacity = 300
        self.weather_container.opacity = 0
        self.weather_container.visible = True
        self.error_message.visible = False
        self.page.update()

        # Fade in
        import asyncio
        await asyncio.sleep(0.1)
        self.weather_container.opacity = 1
        self.page.update()

    def create_info_card(self, icon, label, value):
        """Create an info card for weather details."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=30, color=ft.Colors.BLUE_700),
                    ft.Text(label, size=12, color=ft.Colors.GREY_600),
                    ft.Text(
                        value,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            bgcolor=ft.Colors.ON_SECONDARY, # for theme adaptability
            border_radius=10,
            padding=15,
            width=150,
        )
    
    def show_error(self, message: str):
        """Display error message."""
        self.error_message.value = f"❌ {message}"
        self.error_message.visible = True
        self.weather_container.visible = False
        self.forecast_container.visible = False # added feature
        self.page.update()


def main(page: ft.Page):
    """Main entry point."""
    WeatherApp(page)


if __name__ == "__main__":
    ft.app(target=main)