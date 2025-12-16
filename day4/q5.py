
tonns_to_kg = lambda tonns: tonns * 1000
kg_to_gm = lambda kg: kg * 1000
gm_to_mg = lambda gm: gm * 1000
gm_to_pounds = lambda gm: gm / 453.59237


def display_weight(value, conversion_type_str, conversion_func):
    result = conversion_func(value)
    print(f"{value} {conversion_type_str} = {result}")


def conversion():
    value = float(input("Enter a weight value: "))

    print("\nAll Conversions\n")

    display_weight(value, "tonns_to_kg", tonns_to_kg)
    display_weight(value, "kg_to_gm", kg_to_gm)
    display_weight(value, "gm_to_mg", gm_to_mg)
    display_weight(value, "gm_to_pounds", gm_to_pounds)


conversion()
