def integer_validation(user_input):
    try:
        num = int(user_input)
        if num <= 0 :
            return None
        else:
            return num
    except ValueError:
        return None
    
