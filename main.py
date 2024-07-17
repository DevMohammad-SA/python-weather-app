import requests
# ANSI escape sequences for text colors
COLOR_RESET = '\033[0m'
COLOR_BLACK = '\033[30m'
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_WHITE = '\033[37m'

# ANSI escape sequences for background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

def get_weather (api_key,location):
	url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
	response = requests.get(url)
	data = response.json()
	return data
def main():
	api_key = "f5f8b72108934cc083e53430242406"
	location = input("Enter your city name or zipcode:\n")
	try:
		weather_data = get_weather(api_key,location)
		print(f"{COLOR_MAGENTA}Weather in {weather_data['location']['name']} {weather_data['location']['country']}:\n"
			  f"Temp: {weather_data['current']["temp_c"]} °C\n"
			  f"Condition: {weather_data['current']['condition']['text']}\n"
			  f"Humidity: {weather_data['current']['humidity']}%\n"
			  f"Wind Speed: {weather_data['current']['wind_kph']} m/s\n"
			  f"Wind Direction: {weather_data['current']['wind_dir']}")
	except Exception as e:
		print("Error fetching weather data: ",e)
if __name__ == "__main__":
	main()