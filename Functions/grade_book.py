def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) // 3
    if 0 <= average < 60:
        return "F"
    elif 60 <= average < 70:
        return "D"
    elif 70 <= average < 80:
        return "C"
    elif 80<= average < 90:
        return "B"
    elif 90 <= average <= 100:
        return "A"
