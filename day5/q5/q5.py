import arithmetic
import string_ops

def main():
    num1 = 4
    num2 = 7

    print("Addition:", arithmetic.add(num1, num2))
    print("Multiplication:", arithmetic.multiply(num1, num2))

    text = "Darshana"
    print("Reversed String:", string_ops.reverse_string(text))
    print("Vowel Count:", string_ops.count_vowels(text))

main()

