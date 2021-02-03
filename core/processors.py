"""Main processors module"""

# Ones place dictionary
ones = {
0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

# Tens place dictionary
tens = {
2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
7: 'seventy', 8: 'eighty', 9: 'ninety'}

# -illions place dictionary
illions = {
1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
10: 'nonillion', 11: 'decillion', 12: 'undecillion', 13: 'duodecillion',
14: 'tredecillion', 15: 'quattuordecillion', 16: 'quindecillion',
17: 'hexdecillion', 18: 'septendecillion', 19: 'octodecillion',
20: 'novemdecillion', 21: 'vigintillion', 22: 'unvigintillion',
23: 'duovigintillion', 24: 'trevigintillion', 25: 'quattourvigintillion',
26: 'quinvigintillion', 27: 'hexvigintillion', 28: 'septenvigintillion',
29: 'octovigintillion', 30: 'novemvigintillion', 31: 'trigintillion',
32: 'untrigintillion', 33: 'duotrigintillion', 34: 'googol',
35: 'googolplex'}

def validate_number(number):
    """Function checks for valid postive/negative numbers and not strings"""
    number = number.replace(',', '') # Remove any commas
    is_valid = number.lstrip("-").isdigit()
    return is_valid

def transform_number_to_words(number):
    """Function converts number string into English words string"""
    try:
        # Remove any commas then convert number string to integer
        number = int(number.replace(',', '')) 
    except ValueError:
        return 'Error: Unable to convert number string into integers!'

    if number < 0:
        return _join('negative', _number_position(-number))
    if number == 0:
        return 'zero'
    return _number_position(number)

def _number_position(number):
    """Function to determine numbers place"""
    if number < 20:
        return ones[number]
    if number < 100:
        return _join(tens[number // 10], ones[number % 10])
    if number < 1000:
        return _divider(number, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if number < 1000**(illions_number + 1):
            break
    return _divider(number, 1000**illions_number, illions_name)

def _divider(dividend, divisor, magnitude):
    """Function to handle large division"""
    return _join(
        _number_position(dividend // divisor),
        magnitude,
        _number_position(dividend % divisor),
    )

def _join(*args):
    """Function to handle joins and adds spaces"""
    return ' '.join(filter(bool, args))