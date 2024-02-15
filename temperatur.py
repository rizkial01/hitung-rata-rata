def konversi_celsius_ke_fahrenheit(suhu_celsius):
    suhu_fahrenheit = (suhu_celsius * 9/5) + 32
    return suhu_fahrenheit

def main():
    suhu_celsius = float(input("Masukkan suhu dalam derajat Celsius: "))
    suhu_fahrenheit = konversi_celsius_ke_fahrenheit(suhu_celsius)
    print("Suhu dalam derajat Fahrenheit:", suhu_fahrenheit)

if '_ _name_ _' == "_main_":
    main()