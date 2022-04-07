"""Generate Pig Latin version of words from English words"""
def main():
    """Check the word if it starts from constant or vowel. If constant, move it to end and add
    'ay', else add 'way' at end."""
    vowels = ('a', 'e', 'i', 'o', 'u')

    while True:

        word = input("\nEnter the word : ")

        if word[0] not in vowels:
            word = word[1:] + word[0] + 'ay'
        else:
            word = word + 'way'
        print("\n\nPig Latin : " + word)

        try_again = input("\nTry Again?(Press Enter else n)")
        if try_again == 'n':
            break
    input("\nPress Enter to exit")
if __name__ == "__main__":
    main()
    