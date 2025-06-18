class SmartLight:
    def __init__(self, device_name):
        self.device_name = device_name

    def turn_on(self):
        print(f"{self.device_name} is now ON")

    def set_brightness(self, level):
        print(f"{self.device_name} brightness set to {level}")


class SmartThermostat:
    def __init__(self, device_name):
        self.device_name = device_name

    def turn_on(self):
        print(f"{self.device_name} is now ON")

    def set_temperature(self, temp):
        print(f"{self.device_name} temperature set to {temp}°C")


class SmartSpeaker:
    def __init__(self, device_name):
        self.device_name = device_name
        self.volume = 5

    def play_music(self, song):
        print(f"{self.device_name} is playing '{song}' at volume {self.volume}")


# Example usage
light = SmartLight("Living Room Light")
thermostat = SmartThermostat("Hall Thermostat")
speaker = SmartSpeaker("Bedroom Speaker")

light.turn_on()
light.set_brightness(75)

thermostat.turn_on()
thermostat.set_temperature(24)

speaker.play_music("Your Favorite Song")