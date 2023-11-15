import sys


def analyze_string(email_address):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0

    # Iterate through each character in the email address
    for char in email_address:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    # Calculate percentages
    total_length = len(email_address)
    uppercase_percentage = (uppercase_count / total_length) * 100
    lowercase_percentage = (lowercase_count / total_length) * 100
    digit_percentage = (digit_count / total_length) * 100
    other_percentage = (other_count / total_length) * 100

    return (
        uppercase_percentage,
        lowercase_percentage,
        digit_percentage,
        other_percentage,
    )


# Exercise-1
input_val_1 = "Support1@litwork.in"
output_val_1 = analyze_string(input_val_1)

# Print the result for Exercise-1
print(f"Exercise-1 Output:")
print(f"{output_val_1[0]:.3f}%")
print(f"{output_val_1[1]:.3f}%")
print(f"{output_val_1[2]:.3f}%")
print(f"{output_val_1[3]:.3f}%")
print()

# Exercise-2
input_val_2 = "Client.1234@litwork.in"
output_val_2 = analyze_string(input_val_2)

# Print the result for Exercise-2
print(f"Exercise-2 Output:")
print(f"{output_val_2[0]:.3f}%")
print(f"{output_val_2[1]:.3f}%")
print(f"{output_val_2[2]:.3f}%")
print(f"{output_val_2[3]:.3f}%")
