class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
        if scale == "C":
            self.value_kelvin = value + 273.15
        elif scale == "F":
            self.value_kelvin = (value - 32) * 5 / 9 + 273.15

    def __eq__(self, other):
        return self.value_kelvin == other.value_kelvin

    def __lt__(self, other):
        return self.value_kelvin < other.value_kelvin


tc = Temperature(25, "C")
tf = Temperature(77, "F")
tf2 = Temperature(100, "F")
print(tc == tf)  # True
print(tc < tf2)  # True
