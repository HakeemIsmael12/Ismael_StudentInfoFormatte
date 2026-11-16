# Student Info Formatter - Version 1.0 (Initial version - basic input and output)
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    section = input("Enter your section: ")
    favorite_color = input("Enter your favorite color: ")

    print("\nStudent Information:")
    print(f"Name: {first_name} {last_name}")
    print(f"Section: {section}")
    print(f"Favorite Color: {favorite_color}")

if __name__ == "__main__":
    main()


