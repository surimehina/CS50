def main():
    userInput = input("Input: ")
    print("Output: ", remove_vowels(userInput))

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels])

main()