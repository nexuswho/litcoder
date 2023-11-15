def egyptian_fraction(numerator, denominator):
    fractions = []

    while numerator != 0:
        unit_fraction = (denominator + numerator - 1) // numerator
        fractions.append(unit_fraction)

        numerator = unit_fraction * numerator - denominator
        denominator = denominator * unit_fraction

    return fractions


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
