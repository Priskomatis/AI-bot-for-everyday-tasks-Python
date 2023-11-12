from pyowm import OWM
from geopy import Nominatim
from datetime import datetime


class Weather():

    #Location of where you want the forecast for

    __location = "Athens, Greece"

    #API Key from the weather browser

    api_key = "c028bb17c85b84dd7f7da13c97b2b7bf"

    def __init__(self):
        self.ow = OWM(self.api_key)         #Open weather manager, creates a new open weather map object and it passes that api key into that object
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="myGeoCoder")
        city = "Athens"
        country = "GR"
        self.__location = city + ", " + country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude


    def uv_index(self, uvi:float):
        """ Returns a message depending on the IV Index provided """
        message = ""
        if uvi <= 2.0:
            message = "The Ultraviolet level is low, no protection is required."
        if uvi >= 3.0 and uvi < 6:
            message = "The ultraviolet level is medium, skin protection is required"
        if uvi >= 6 and uvi < 8:
            message = "The ultraviolet level is high, skin protection is required"
        if uvi >= 8 and uvi < 11:
            message ="The ultraviolet level is very high, extra skin protection is required"
        if uvi >= 11:
            message = "The ultraviolet is extremely high, caution is advised and extra skin protection is required"
        return message


    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast

    @property
    def forecast(self):
        """ Returns the forecast at this location """
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        detail_status = forecast.forecast_daily[0].detailed_status
        pressure = str(forecast.forecast_daily[0].pressure.get('press'))
        humidity = str(forecast.forecast_daily[0].humidity)
        sunrise = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime("%H:%M:%S")
        sunset = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime("%H:%M:%S")
        temperature = str(forecast.forecast_daily[0].temperature('celsius').get('day'))
        uvi = forecast.forecast_daily[0].uvi


        message = "Here is the Weather: Today will be mostly " + detail_status \
                    + ", humidity of " + humidity + " percent" \
                    + " and a pressure of " + pressure + " millibars " \
                    + ". The temperature is " +temperature + " degrees" \
                    + ". Sunrise was at "+ sunset \
                    + " and sunset is at " + sunset \
                    + "." + self.uv_index(uvi)

        return message





# Demo

myWeather = Weather()

print(myWeather.forecast)


