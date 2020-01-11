import re
def validate_number(number):
    result = re.findall(r'(\d{3})[\W\s]{0,1}(\d{3})[\W\s]{0,1}(\d{4})', number)
    if result:
        x,y,z = result[0]
        return x + y + z
    return False

def validate_email(email:str)->bool:
    if len(email) < 3: 
        return False
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    return True if re.search(regex,email) else False
    
def validate_name(name:str) ->bool:
    """
    :param name: name of the user
    return true if find a digit, otherwise return false
    """
    # print(len(name))
    if len(name) > 3:
        result = any(char.isdigit() for char in name)
        return name if not result else False
    return False
if __name__ == "__main__":

    numbers = ["787*377*6957", "787.376.6957", "787 387 6957", "787-555-6957", "787-377-6957", "787377q6957", "7874-5646-454"]
    for n in numbers:
        print(validate_number(n))

    emails = ["Rasdasdasd@gmai.com", "1raul0221@gmail.com", "raul0221@gmailcom", "raul0221@gmail.com"]
    for e in emails:
        print(validate_email(e))

    name = ["Raul Pichardo", "Pedor", "Ramo2n", "Raul 2do", "1Maria"]

    for n in name:
        print(validate_name(n))