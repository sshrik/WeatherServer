import requests

if __name__ == "__main__":
    apiFile = open("apikey", "r")
    apiKey = apiFile.readline()
    apiFile.close()

    URL = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(URL, {"q":"Seoul", "appid":apiKey})
    
    weatherFile = open("weather", "w")
    weatherFile.write(response.text)
    weatherFile.close()