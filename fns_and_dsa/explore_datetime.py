# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date: {formatted_future_date}")

def main():
    while True:
        print("\nDatetime Operations")
        print("1. Display Current Date and Time")
        print("2. Calculate Future Date")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_current_datetime()
        elif choice == '2':
            calculate_future_date()
        elif choice == '3':
            print("Exiting the Datetime Operations script. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
