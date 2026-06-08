#! /usr/bin/python
#
# This script is written and tested on Archlinux

import secrets
import string
import math


def get_valid_length():
    try:
        length = int(input("Enter password length: "))

        if length < 15:
            print(
                f"Warning: NIST 2024 recommends minimum 15 characters (you entered {length})"
            )
            confirm = input("Proceed anyway? (y/n): ")

            if confirm.lower() != "y":
                return get_valid_length()

        if length > 64:
            print("Maximum recommended length is 64 characters")
            return 64
        return length
    except ValueError:
        print("Error: Please enter a valid integer")
        return get_valid_length()


def include_punctuation():
    while True:
        response = input("Include punctuation? (y/n): ").lower()
        if response in ("y", "n"):
            return response == "y"
        print("Please enter 'y' or 'n'")


def generate_password(length, use_punctuation):
    character_pool = string.ascii_letters + string.digits
    if use_punctuation:
        character_pool += string.punctuation
    password_chars = [secrets.choice(character_pool) for _ in range(length)]
    return "".join(password_chars)


def format_time(seconds):
    intervals = [
        ("century", 60 * 60 * 24 * 365.25 * 100, "centuries"),
        ("year", 60 * 60 * 24 * 365.25, "years"),
        ("day", 60 * 60 * 24, "days"),
        ("hour", 60 * 60, "hours"),
        ("minute", 60, "minutes"),
        ("second", 1, "seconds"),
    ]
    for name, duration, plural in intervals:
        if seconds >= duration:
            value = seconds / duration
            label = name if value < 2 else plural
            return f"{value:.1f} {label}"
    return "instantly"


def calculate_entropy(length, use_punctuation):
    pool_size = 62  # 52 letters + 10 digits
    if use_punctuation:
        pool_size = 94  # + 32 punctuation
    entropy = length * math.log2(pool_size)
    possibilities = pool_size**length
    guesses_per_sec = 10**9  # SHA-256 offline attack estimate
    crack_time = possibilities / guesses_per_sec
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Possibilities: {pool_size}^{length} = {possibilities:.2e}")
    print(f"Crack time: {format_time(crack_time)}")
    return entropy


def main():
    print("Random password generator\n")
    length = get_valid_length()
    use_punctuation = include_punctuation()
    password = generate_password(length, use_punctuation)
    print(f"\nPassword: {password}")
    print(f"Length: {len(password)} characters")
    calculate_entropy(length, use_punctuation)


if __name__ == "__main__":
    main()
