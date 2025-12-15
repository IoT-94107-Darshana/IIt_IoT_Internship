# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Function to count consonants
def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count


# Function to calculate ratio of vowels to consonants
def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Undefined (No consonants)"
    return vowels / consonants


# Main program
text = input("Enter a string: ")

vowel_count = count_vowels(text)
consonant_count = count_consonants(text)

ratio = vowel_consonant_ratio(vowel_count, consonant_count)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Ratio of vowels to consonants:", ratio)
