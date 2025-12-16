
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.54


def distance_converter(distance, conversion_type_str, conversion_func):
    result = conversion_func(distance)
    print(f"{distance} {conversion_type_str} = {result}")


def conversion():
    distance_value = float(input("Enter a distance value: "))

    print("\nAll Conversions\n")

    distance_converter(distance_value, "km to m", km_to_m)
    distance_converter(distance_value, "m to cm", m_to_cm)
    distance_converter(distance_value, "cm to mm", cm_to_mm)
    distance_converter(distance_value, "feet to inches", feet_to_inches)
    distance_converter(distance_value, "inches to cm", inches_to_cm)


conversion()
