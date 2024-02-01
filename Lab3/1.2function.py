"""
Read in a Fahrenheit temperature.
Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""
def CelsiustToFahrenheit(y):
    return y * 9 / 5 + 32
def FahrenheitToCelsius(y):
    return (y - 32) * 5 / 9
print("To convert from Celsius to Fahrenheit, input command 1 and click enter")
print("To convert from Fahrenheit to Celsius, input command 2 and click enter")

x = int(input())

if x != 1 and x != 2:
    print("Wrong command, use command 1 or 2 and nothing else!")
    exit()
elif x == 1:
    y = float(input())
    print(f"Celsius to Fahrenheit: {y} -> {CelsiustToFahrenheit(y)}") 
elif x == 2: 
    y = float(input())
    print(f"Fahrenheit to Celsius: {y} -> {FahrenheitToCelsius(y)}")
 