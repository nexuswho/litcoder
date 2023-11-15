def check_passwords(passwords):
    passwords.sort()  # Sort the passwords lexicographically

    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return f"BAD PASSWORD\n{passwords[i]} {passwords[i+1]}"

    return "GOOD PASSWORD"


# Exercise-1
input_passwords_1 = ["abc", "zxy", "pqr"]
output_1 = check_passwords(input_passwords_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_passwords_2 = ["abc", "abczxy", "abcpqr"]
output_2 = check_passwords(input_passwords_2)
print(f"Exercise-2 Output: {output_2}")
