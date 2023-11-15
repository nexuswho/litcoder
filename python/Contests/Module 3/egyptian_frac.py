def egyptian_fraction(numerator, denominator):
    result = []
    while numerator != 0:
        x = -(-denominator // numerator)
        result.append(x)
        numerator = numerator * x - denominator
        denominator = denominator * x
    return result


# Exercise-1
input_numerator_1 = 6
input_denominator_1 = 14
output_1 = egyptian_fraction(input_numerator_1, input_denominator_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_numerator_2 = 3
input_denominator_2 = 4
output_2 = egyptian_fraction(input_numerator_2, input_denominator_2)
print(f"Exercise-2 Output: {output_2}")
