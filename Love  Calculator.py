import random

def calculate_love_score(name1, name2):
    # Combine the names
    combined_names = name1 + name2
    # Convert to lowercase and remove spaces
    combined_names = combined_names.lower().replace(" ", "")
    # Use a basic algorithm to determine the score
    love_score = 0
    for char in combined_names:
        love_score += ord(char)
    # Make sure the score is within a percentage range
    love_percentage = love_score % 101
    return love_percentage

def main():
    print("Welcome to the Love Calculator!")
    
    # Get names from user
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    # Calculate love percentage
    love_percentage = calculate_love_score(name1, name2)
    
    # Print the result
    print(f"The love score between {name1} and {name2} is {love_percentage}%")

if __name__ == "__main__":
    main()
