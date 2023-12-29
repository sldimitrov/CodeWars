def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = fuel_left * mpg 
    if distance_to_pump <= max_distance:
        return True
    else:
        return False
