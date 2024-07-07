# Global conversion factors
FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(farhenheit):
    """Convert Fahrenheit to Celcius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit using the global conversion factor."""
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def master():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}C is {converted_temp}F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}F is {converted_temp}C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__master__":
    master()
