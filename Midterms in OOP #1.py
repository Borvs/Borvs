def main():

    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class CelsToFahr(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class FahrToCelc(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5/9

    class KelvToCelc(TemperatureConversion):

        def conversion(self):
            return (self._temp - 273.15)


    class CelsToKelv(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15

    tempInCelsius = float(input("Enter the temperature: "))

    convert = CelsToFahr(tempInCelsius)

    print(str(convert.conversion()) + " Celsius to Fahrenheit")

    convert = CelsToKelv(tempInCelsius)

    print(str(convert.conversion()) + " Celsius to Kelvin")


    convert = FahrToCelc(tempInCelsius)

    print(str(convert.conversion()) + " Fahrenheit To Celsius")

    convert = KelvToCelc(tempInCelsius)

    print(str(convert.conversion()) + " Kelvin To Celsius")

main()