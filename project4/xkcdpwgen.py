import random
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a secure, memorable password using the XKCD method")
    parser.add_argument('-w', '--words', default=4, type=int,
                        help="include WORDS words in the password (default=4)")
    parser.add_argument('-c', '--caps', default=0, type=int,
                        help="capitalize the first letter of CAPS random words (default=0)")
    parser.add_argument('-n', '--numbers', default=0, type=int,
                        help="insert NUMBERS random numbers in the password (default=0)")
    parser.add_argument('-s', '--symbols', default=0, type=int,
                        help="insert SYMBOLS random symbols in the password (default=0)")
    return parser.parse_args()


def main(args):
    print("num words:", args.words)
    print("num caps:", args.caps)
    print("num numbers:", args.numbers)
    print("num symbols:", args.symbols)

    words = open("words.txt", "r").read().split("\n")[:-1]
    chosen_words = random.choices(words, k=args.words)

    caps_words = []
    possible_indices = [i for i in range(0, args.words)]
    indices_found = 0
    while indices_found < args.caps and len(possible_indices) > 0:
        index = random.choice(possible_indices)
        possible_indices.remove(index)
        indices_found += 1
        caps_words.append(index)

    for index in caps_words:
        chosen_words[index] = chosen_words[index][0].upper() + chosen_words[index][1:]

    print(chosen_words)

    password = []
    for word in chosen_words:
        password.extend(["", word])
    password.append("")

    numbers = [str(num) for num in range(10)]
    possible_indices = [i for i in range(0, 2 * args.words + 1, 2)]
    symbols_slots = random.choices(possible_indices, k=args.numbers)
    for slot in symbols_slots:
        if random.random() < 0.5:
            password[slot] = password[slot] + random.choice(numbers)
        else:
            password[slot] = random.choice(numbers) + password[slot]

    symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]
    possible_indices = [i for i in range(0, 2 * args.words + 1, 2)]
    symbols_slots = random.choices(possible_indices, k=args.symbols)
    for slot in symbols_slots:
        if random.random() < 0.5:
            password[slot] = password[slot] + random.choice(symbols)
        else:
            password[slot] = random.choice(symbols) + password[slot]

    password = "".join(password)
    print(password)



if __name__ == "__main__":
    args = parse_arguments()
    main(args)
