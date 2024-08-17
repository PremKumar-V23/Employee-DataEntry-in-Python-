import pandas as pd
from datetime import datetime
from dataentry import get_date,get_empname,get_empno,get_role,get_salary
import csv

DATE_FORMAT = "%d-%m-%Y"

class CSV:
    CSV_FILE = "EMPLOYEE_DETAILS.CSV"
    columns = ["date", "role", "empno", "empname", "salary"]

    @classmethod
    def initalize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, role, empno, empname, salary):
        new_entry = {
            "date": date,
            "role": role,
            "empno": empno,
            "empname": empname,
            "salary": salary
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Entry Added Successfully")

    @classmethod
    def search_by_empno(cls, empno):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            result = df[df["empno"] == empno]
            if not result.empty:
                return result
            else:
                return f"No entry found with employee number {empno}."
        except FileNotFoundError:
            return "CSV file not found. Please initialize it first."

    @classmethod
    def search_by_empname(cls, empname):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            result = df[df["empname"].str.lower() == empname.lower()]
            if not result.empty:
                return result
            else:
                return f"No entry found with employee name {empname}."
        except FileNotFoundError:
            return "CSV file not found. Please initialize it first."

    @classmethod
    def search_by_date(cls, date):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            result = df[df["date"] == date]
            if not result.empty:
                return result
            else:
                return f"No entries found for the date {date}."
        except FileNotFoundError:
            return "CSV file not found. Please initialize it first."

    @classmethod
    def search_by_date_range(cls, start_date, end_date):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=DATE_FORMAT)
            start_date = datetime.strptime(start_date, DATE_FORMAT)
            end_date = datetime.strptime(end_date, DATE_FORMAT)
            result = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
            if not result.empty:
                return result
            else:
                return f"No entries found between {start_date.strftime(DATE_FORMAT)} and {end_date.strftime(DATE_FORMAT)}."
        except FileNotFoundError:
            return "CSV file not found. Please initialize it first."
        except Exception as e:
            return f"An error occurred: {e}"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)
    
    try:
        date_obj = datetime.strptime(date_str, DATE_FORMAT)
        return date_obj.strftime(DATE_FORMAT)
    except ValueError:
        print(f"Invalid format. Please enter the date in the correct format ({DATE_FORMAT}).")
        return get_date(prompt, allow_default)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add New Entry")
        print("2. Search by Employee Number or Name")
        print("3. Get Details by Date")
        print("4. Get Data by Date Range")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            search()
        elif choice == '3':
            date = get_date("Enter the date (DD-MM-YYYY):", allow_default=False)
            result = CSV.search_by_date(date)
            print(result)
        elif choice == '4':
            start_date = get_date("Enter the start date (DD-MM-YYYY):", allow_default=False)
            end_date = get_date("Enter the end date (DD-MM-YYYY):", allow_default=False)
            result = CSV.search_by_date_range(start_date, end_date)
            print(result)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def add_entry():
    CSV.initalize_csv()
    date = get_date("Enter the date of entry (DD-MM-YYYY):", allow_default=True)
    role = get_role()
    empno = get_empno()
    empname = get_empname()
    salary = get_salary()
    CSV.add_entry(date, role, empno, empname, salary)

def search():
    search_type = input("Search by (1) Employee Number, (2) Employee Name, or (3) Date? Enter 1, 2, or 3: ")
    if search_type == '1':
        empno = get_empno()
        result = CSV.search_by_empno(empno)
    elif search_type == '2':
        empname = get_empname()
        result = CSV.search_by_empname(empname)
    elif search_type == '3':
        date = get_date("Enter the date (DD-MM-YYYY):", allow_default=False)
        result = CSV.search_by_date(date)
    else:
        result = "Invalid option selected."
    
    print(result)

# Call the main menu function to start the program
main_menu()





