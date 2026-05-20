import random
import os

WORD_LIST = [
    "python", "cipher", "hangman", "terminal", "keyboard",
    "dungeon", "phantom", "mystery", "eclipse", "crystal",
    "voltage", "quantum", "gravity", "fractal", "labyrinth",
    "whisper", "ancient", "diamond", "vampire", "phoenix",
]

SHIPS = [
    ("Dreadnought-X",  "████████████"),
    ("Void Reaper",    "██████████"),
    ("Neon Specter",   "████████"),
    ("Chrome Wraith",  "██████"),
    ("Glitch Runner",  "████"),
    ("Wire Shade",     "██"),
    ("Ghost Bit",      "▪"),
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display_word(word, guessed):
    return "  ".join(c.upper() if c in guessed else "_" for c in word)


def assign_fleet(word_length):
    fleet_sizes = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    num_ships = min(max(word_length - 3, 2), len(SHIPS))
    return list(SHIPS[:num_ships])


def render(word, guessed, wrong_letters, fleet, ships_lost, message=""):
    clear()
    print("╔══════════════════════════════════════════╗")
    print("║    Cyber Star Word Wars!!!!!!     ║")
    print("╚══════════════════════════════════════════╝\n")

    print("  ── FLEET STATUS ─────────────────────────")
    for i, (name, hull) in enumerate(fleet):
        if i < ships_lost:
            print(f"  ✕  {name:<12}  {'~' * len(hull)}  [SUNK]")
        else:
            print(f"  ▶  {name:<12}  {hull}")

    remaining = len(fleet) - ships_lost
    print(f"\n  Ships remaining: {remaining} / {len(fleet)}")
    print()
    print("  WORD:   ", display_word(word, guessed))

    if wrong_letters:
        print(f"\n  Wrong letters:  {', '.join(sorted(wrong_letters)).upper()}")
    else:
        print("\n  Wrong letters:  —")

    if message:
        print(f"\n  ▶  {message}")
    print()


def play():
    word = random.choice(WORD_LIST)
    guessed = set()
    wrong_letters = set()
    fleet = assign_fleet(len(word))
    ships_lost = 0
    message = f"Your fleet of {len(fleet)} ships is deployed. Guess a letter!"

    while True:
        word_done = all(c in guessed for c in word)
        render(word, guessed, wrong_letters, fleet, ships_lost, message)

        if word_done:
            print(f"  ★ ★ ★  MISSION COMPLETE!  ★ ★ ★")
            print(f"  The word was '{word.upper()}'. Fleet survived with {len(fleet) - ships_lost} ship(s) intact.\n")
            break

        if ships_lost >= len(fleet):
            print(f"  ✕ ✕ ✕  FLEET DESTROYED  ✕ ✕ ✕")
            print(f"  The word was '{word.upper()}'.\n")
            break

        raw = input("  Your guess → ").strip().lower()

        if len(raw) == 1 and raw.isalpha():
            if raw in guessed or raw in wrong_letters:
                message = f"You already guessed '{raw.upper()}'. Try another."
            elif raw in word:
                guessed.add(raw)
                revealed = sum(1 for c in word if c == raw)
                message = f"✓ '{raw.upper()}' is in the word! ({revealed} occurrence{'s' if revealed > 1 else ''})"
            else:
                wrong_letters.add(raw)
                ships_lost += 1
                if ships_lost <= len(fleet):
                    sunk = fleet[ships_lost - 1][0]
                    remaining = len(fleet) - ships_lost
                    message = f"✗ '{raw.upper()}' not found — {sunk} has been sunk! {remaining} ship(s) remaining."
                else:
                    message = f"✗ '{raw.upper()}' is not in the word."
        else:
            message = "Please enter a single letter."

    again = input("  Play again? (y/n) → ").strip().lower()
    if again == "y":
        play()
    else:
        print("\n  Fair winds and following seas.\n")


if __name__ == "__main__":
    play()