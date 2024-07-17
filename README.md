This Python script uses the WeatherAPI to fetch and display current weather data. It supports input of city names or zip codes and retrieves temperature, weather conditions, humidity, wind speed, and wind direction.

The script imports requests for HTTP requests and defines ANSI escape sequences for text and background colors. The get_weather function constructs a URL with an API key and location query, sends a GET request to WeatherAPI, and parses the JSON response.

In main:

- Prompts user for a city name or zip code.
- Retrieves weather data with get_weather.
- Prints formatted weather information using ANSI colors, including temperature (°C), weather condition, humidity (%), wind speed (m/s), and wind direction.
Errors during data retrieval are caught and displayed.
