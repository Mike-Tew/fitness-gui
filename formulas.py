def male_bmr(weight, height, age):
    # Calculate male bmr
    return (6.24 * weight) + (12.7 * height) - (6.755 * age) + 66.47


def female_bmr(weight, height, age):
    # Calculate female BMR
    return (4.35 * weight) + (4.7 * height) - (4.7 * age) + 665.1


def male_calories(heartrate, weight, age, duration):
    # Calculate male calories burned based on heart rate and duration
    return (
        (-55.0969 + (0.6309 * heartrate) + (0.1988 * (weight / 2.205)) + (0.2017 * age))
        / 4.184
    ) * duration


def female_calories(heartrate, weight, age, duration):
    # Calculate female calories burned based on heart rate and duration
    return (
        (-20.4022 + (0.4472 * heartrate) - (0.1263 * (weight / 2.205)) + (0.074 * age))
        / 4.184
    ) * duration


def male_body_fat(age, chest, ab, thigh):
    # Calculate male body fat percentage
    fatTotal = chest + ab + thigh
    fatSquared = fatTotal * fatTotal
    density = (
        1.10938 - (0.0008267 * fatTotal) + (0.0000016 * fatSquared) - (0.0002574 * age)
    )

    return (4.57 / density - 4.142) * 100


def female_body_fat(age, chest, ab, thigh):
    # Calculate female body fat percentage
    fatTotal = chest + ab + thigh
    fatSquared = fatTotal * fatTotal
    density = (
        1.0994921
        - (0.0009929 * fatTotal)
        + (0.0000023 * fatSquared)
        - (0.0001392 * age)
    )

    return (4.57 / density - 4.142) * 100


def bmi_formula(height, weight):
    # Calculate BMI from height and weight
    return (weight * 703) / (height * height)
