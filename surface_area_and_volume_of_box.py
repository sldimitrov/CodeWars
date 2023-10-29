def get_size(w,h,d):
    output_list = []

    surface_area = 2 * d * w + 2 * d * h + 2 * w * h
    output_list.append(surface_area)
    
    volume = w * h * d
    output_list.append(volume)
    
    return output_list
