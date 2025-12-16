def km_to_m(distance_km):
    return distance_km * 1000

def m_to_cm(distance_m):
    return distance_m * 100

def cm_to_mm(distance_cm):
    return distance_cm * 10

def feet_to_inches(distance_ft):
    return distance_ft * 12

def inches_to_cm(distance_in):
    return distance_in * 2.54

def distance_converter(distance, conversion_type_str, conversion_func):
    result = conversion_func(distance)
    print(f"{distance} {conversion_type_str} = {result}")

def conversion():
    
        user_distance_input = input("Enter a distance value: ")
        distance_value = float(user_distance_input)
        
        print("\nAll Conversions\n")

        distance_converter(distance_value, "km to m", km_to_m)
        distance_converter(distance_value, "m to cm", m_to_cm)
        distance_converter(distance_value, "cm to mm", cm_to_mm)
        distance_converter(distance_value, "feet to inches", feet_to_inches)
        distance_converter(distance_value, "inches to cm", inches_to_cm)

conversion()