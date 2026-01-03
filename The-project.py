# Temperature Conversion Program
temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit?(C/F): ")
if unit == "C" or unit == "c":
    temp = temp * 9/5 + 32
    print(f"The temperature in Fahrenheit is {temp} Fahrenheit")
elif unit == "F" or unit == "f":
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {temp} Celsius")
else:
    print(f"The temperature unit is invalid")
