from datetime import datetime

CATEGORIES = {"D":"Developer" ,"T":"Tester" ,"M":"Manager"}
DATE_FORMAT = "%d-%m-%Y"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)
    
    try:
        # Attempt to parse the provided date string into a datetime object
        date_obj = datetime.strptime(date_str, DATE_FORMAT)
        return date_obj.strftime(DATE_FORMAT)
    except ValueError:
        print(f"Invalid format. Please enter the date in the correct format ({DATE_FORMAT}).")
        return get_date(prompt, allow_default)


def get_role():
    role=input("Enter the role ('D' for Developer or 'T' for Tester 'M' for Manager)").upper()
    if role in CATEGORIES:
        return CATEGORIES[role]
    
    print("Invalid Role.Please enter ('D' for Developer or 'T' for Tester 'M' for Manager)")
    return get_role()
    

def get_empname():
    name = input("Enter the name:")
    return name

def get_empno():
    try:
        no = int(input("Enter The Employee NO: "))
        if no < 1000 or no >= 10000:
            raise ValueError("Enter The No between thousand and ten thousand.")
        return no
    except ValueError as e:
        print(e)
        return get_empno()

def get_salary():
    try:
        amount = int(input("Enter The Salary:"))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative & non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_empno()
