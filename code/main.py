from itertools import permutations
from typing import List


def create_vocabulary() -> List[str]:
    """This function creates the german dictionary
    from a txt file

    Returns:
        List[str]: A list of all german words found in the txt file
    """
    german_words = []
    with open("wordlist-german.txt", "r") as file:
        german_words = [line.lower().rstrip("\n") for line in file]
    return german_words


def german_anagram(word: str, starts_with: str) -> List[str]:
    """This function takes as an argument a scrabbled word
        and returns the word if found in german dictionary
    Args:
        word (str): the scrabbled word
        starts_with (str): the first letter of the word

    Returns:
        List[str]: A list of all possible words found
    """
    german_words = create_vocabulary()
    german_words_found = []
    letters = list(word)
    if starts_with and starts_with in word:
        perms = [p for p in permutations(letters) if p[0] == starts_with]
    else:
        perms = list(permutations(letters))
    for perm in perms:
        candidate = "".join(perm)
        if candidate in german_words:
            german_words_found.append(candidate)
    return german_words_found


if __name__ == "__main__":
    german_words_found = german_anagram("funlae", "l")
    print(german_words_found)

