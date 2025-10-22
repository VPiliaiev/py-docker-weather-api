import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    URL = "http://api.weatherapi.com/v1/current.json"
    API_KEY = os.getenv("API_KEY")
    FILTERING = os.getenv("FILTERING")

    result = requests.get(f"{URL}?key={API_KEY}&q={FILTERING}&lang=en")
    data = result.json()

    if "error" in data:
        print("Error:", data["error"]["message"])
        return

    loc = data["location"]
    cur = data["current"]

    city = loc["name"]
    country = loc["country"]
    time = loc["localtime"]
    temp = cur["temp_c"]
    condition = cur["condition"]["text"]

    print(f"{city}/{country} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
