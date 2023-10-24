import itertools

def load_words(filename="wordlist.txt"):
    with open(filename, "r") as f:
        return set(word.strip().lower() for word in f)

def get_score(word):
    if len(word) == 4:
        return 1
    return len(word)

def is_valid(word, letters, center_letter):
    # Words must include the center letter.
    if center_letter not in word:
        return False

    # Words must contain at least four letters.
    if len(word) < 4:
        return False

    # All letters in the word should be part of the provided letters.
    for w in word:
        if w not in letters:
            return False

    return True

def spelling_bee_solver(letters, center_letter, words):
    valid_words = set()
    for i in range(4, len(letters) + 1):
        for combo in itertools.product(letters, repeat=i):
            word = "".join(combo)
            if word in words and is_valid(word, letters, center_letter):
                valid_words.add(word)

    pangrams = [word for word in valid_words if all(l in word for l in letters)]
    return valid_words, pangrams

def main():
    words = load_words()
    
    print("Welcome to the Spelling Bee Solver!")
    letters = input("Enter the letters (with no spaces): ").strip().lower()
    center_letter = input("Specify the center letter: ").strip().lower()

    valid_words, pangrams = spelling_bee_solver(letters, center_letter, words)

    print("\nValid Words:")
    for word in sorted(valid_words, key=lambda x: (-len(x), x)):
        score = get_score(word)
        if word in pangrams:
            score += 7
        print(f"{word} ({score} points)")

    total_score = sum([get_score(word) for word in valid_words]) + 7 * len(pangrams)
    print(f"\nTotal possible points: {total_score}")

if __name__ == "__main__":
    main()
