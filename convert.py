"""
Converting Arabic number into a Roman numeral in its minimal form 
using the "standard" subtractive notation.

Example:
The numerals for 4 (IV) and 9 (IX) are written using "subtractive notation",
where the first symbol (I) is subtracted from the larger one (V, or X),
thus avoiding the clumsier (IIII, and VIIII).

The largest number that can be displayed in this notation is 3999 (MMMCMXCIX).

Returns:        Roman numeral
Return type:    string
"""


def convert_to_roman(arabic_number):
    arabic_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numeral = ''
    for arabic, roman in arabic_roman_map:
        while arabic_number >= arabic:
            roman_numeral += roman
            arabic_number -= arabic
    return roman_numeral


print(" Arabic number to Roman numeral Conversion.\n")
while True:
    try:
        arabic_number = int(
            input(" Enter a positive integer less than or equal to 3999: ")
            )
    except ValueError:
        print("\n Provide an integer value")
        continue
    if 0 < arabic_number < 4000:
        break
    else:
        print("\n Please enter a valid input ...")

roman_numeral = convert_to_roman(arabic_number)
print(f"\n Arabic Number= {arabic_number}, Roman Numeral= {roman_numeral}\n")
