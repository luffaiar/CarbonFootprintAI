def calculate_carbon(transport, distance, electricity, meat):

    transport_values = {
        "Walking": 0,
        "Bicycle": 0.2,
        "Bus": 1,
        "Train": 0.8,
        "Car": 2
    }

    score = transport_values[transport] * distance
    score += electricity * 0.5

    if meat == "Sometimes":
        score += 5
    elif meat == "Frequently":
        score += 10

    return round(score, 2)