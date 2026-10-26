def integer_validation(user_input):
    try:
        num = int(user_input.strip())
        if num <= 0 :
            return None
        else:
            return num
    except ValueError:
        return None
    
def age_validation(user_input):
    try:
        validated_age = int(user_input.strip())
        if validated_age >= 3 and validated_age <= 120:
            return validated_age
        else:
            return None
    except ValueError:
        return None

def string_validation(user_input):    
    if user_input.strip() == "":
        return None
    else:
        return user_input.strip()
