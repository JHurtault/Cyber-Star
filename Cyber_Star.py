import random
import os
import csv

def load_words(filepath="CyberStar_words.csv"):
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return [row["word"] for row in reader]

WORD_LIST = load_words()

OUTER_FLEET = [
    ("Ogun-X Dreadnought",  "████████████"),
    ("Sankofa Void Reaper", "██████████"),
    ("Neon Griot Specter",  "████████"),
    ("Adinkra Wraith",      "██████"),
]

INNER_FLEET = [
    ("Kente Glitch Runner", "████████████"),
    ("Juju Wire Shade",     "██████████"),
    ("Nyame Ghost Bit",     "████████"),
    ("Anansi Cipher Blade", "██████"),
]

EARTH_DEFENSE_FLEET = [
    ("Ashanti Iron Aegis",  "████████████"),
    ("Oduduwa Last Stand",  "██████████"),
    ("Zulu Neon Bastion",   "████████"),
    ("Sankofa Final Ark",   "██████"),
]

FLEETS = [
    ("OUTER FLEET",         OUTER_FLEET),
    ("INNER FLEET",         INNER_FLEET),
    ("EARTH DEFENSE FLEET", EARTH_DEFENSE_FLEET),
]

DESTROYED_MESSAGES = [
    "The ancestors mourn its loss.",
    "Its neon adinkra symbols fade to dark.",
    "The griot will sing no more of this vessel.",
    "Ogun could not shield it from destruction.",
    "Its kente-wired hull dissolves into the void.",
    "The juju circuits have gone silent.",
    "Even Nyame could not save it.",
]

VICTORY_LINES = [
    "The griots will tell of this victory for generations.",
    "Ogun smiles upon your fleet, warrior.",
    "Your ancestors guided every guess.",
    "The adinkra of wisdom served you well.",
]

DEFEAT_LINES = [
    "The void swallows all three fleets. The griots weep.",
    "Ogun turns his back. Earth burns in neon fire.",
    "The ancestors watch in silence as the last ship fades.",
    "Your kente-hull burns in the cold dark between stars.",
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display_word(word, guessed):
    return "  ".join(c.upper() if c in guessed else "_" for c in word)


def assign_fleet(base_fleet, word_length):
    num_ships = min(max(word_length - 3, 2), len(base_fleet))
    return list(base_fleet[:num_ships])


def render(word, guessed, wrong_letters, fleet, fleet_name, ships_lost, reinforcement_available, fleet_index, message=""):
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║   ✦  C Y B E R   S T A R  :  W O R D  W A R S  ✦  ║")
    print("╚══════════════════════════════════════════════════╝\n")

    print(f"  ── {fleet_name} (Line {fleet_index + 1} of 3) ──────────────────────")
    for i, (name, hull) in enumerate(fleet):
        if i < ships_lost:
            print(f"  ✕  {name:<24}  {'~' * len(hull)}  [STARSHIP DESTROYED!]")
        else:
            print(f"  ▶  {name:<24}  {hull}")

    remaining = len(fleet) - ships_lost
    reinf_status = "✔ AVAILABLE  (type '9' to use  |  '0' to quit)" if reinforcement_available else "✘ USED  (type '0' to quit)"
    print(f"\n  Ships remaining : {remaining} / {len(fleet)}")
    print(f"  Reinforcement   : {reinf_status}")
    print()
    print("  WORD:   ", display_word(word, guessed))

    if wrong_letters:
        print(f"\n  Wrong letters:  {', '.join(sorted(wrong_letters)).upper()}")
    else:
        print("\n  Wrong letters:  —")

    if message:
        print(f"\n  ▶  {message}")
    print()


def play_fleet(word, guessed, wrong_letters, fleet_index):
    fleet_name, base_fleet = FLEETS[fleet_index]
    fleet = assign_fleet(base_fleet, len(word))
    ships_lost = 0
    reinforcement_available = True

    if fleet_index == 0:
        message = f"⬡ {fleet_name} deployed — {len(fleet)} vessels stand ready. Guess a letter!"
    else:
        message = f"⬡ Enemy breaches the line! {fleet_name} now engages. Guess a letter!"

    while True:
        word_done = all(c in guessed for c in word)
        render(word, guessed, wrong_letters, fleet, fleet_name, ships_lost, reinforcement_available, fleet_index, message)

        if word_done:
            return "win"

        if ships_lost >= len(fleet):
            if fleet_index < 2:
                print(f"  ⚠  {fleet_name} has fallen! The enemy pushes closer to Earth...")
                input("  Press Enter to deploy the next fleet...")
                return "next"
            else:
                return "lose"

        raw = input("  Your guess (letter), '9' for Reinforcement, or '0' to quit → ").strip().lower()

        if raw == "0":
            print("\n  ⚠  Retreating from battle... Sankofa — go back and fetch it. Until next time, warrior.\n")
            exit()

        elif raw == "9":
            if not reinforcement_available:
                message = "⚠ Reinforcement already used this fleet. Fight on, warrior!"
            elif ships_lost == 0:
                message = "⚠ No ships lost yet — save your reinforcement for when you need it."
            else:
                reinforcement_available = False
                ships_lost -= 1
                restored = fleet[ships_lost][0]
                message = f"★ Reinforcement called! {restored} has been restored to the line!"

        elif len(raw) == 1 and raw.isalpha():
            if raw in guessed or raw in wrong_letters:
                message = f"You already called '{raw.upper()}' into the void. Try another."
            elif raw in word:
                guessed.add(raw)
                revealed = sum(1 for c in word if c == raw)
                message = f"✓ '{raw.upper()}' resonates through the kente-grid! ({revealed} occurrence{'s' if revealed > 1 else ''})"
            else:
                wrong_letters.add(raw)
                destroy_msg = DESTROYED_MESSAGES[min(ships_lost, len(DESTROYED_MESSAGES) - 1)]
                ships_lost += 1
                if ships_lost <= len(fleet):
                    destroyed = fleet[ships_lost - 1][0]
                    remaining = len(fleet) - ships_lost
                    message = f"✗ '{raw.upper()}' not found — {destroyed}: STARSHIP DESTROYED! {destroy_msg} {remaining} ship(s) remain."
                else:
                    message = f"✗ '{raw.upper()}' not found — final ship lost!"
        else:
            message = "Speak a single letter, type '9' for reinforcements, or '0' to quit."


def play():
    word = random.choice(WORD_LIST)
    guessed = set()
    wrong_letters = set()

    for fleet_index in range(3):
        result = play_fleet(word, guessed, wrong_letters, fleet_index)

        if result == "win":
            clear()
            print("╔══════════════════════════════════════════════════╗")
            print("║   ✦  C Y B E R   S T A R  :  W O R D  W A R S  ✦  ║")
            print("╚══════════════════════════════════════════════════╝\n")
            print(f"  ★ ★ ★  MISSION COMPLETE  ★ ★ ★")
            print(f"  The word was '{word.upper()}'.")
            print(f"  {random.choice(VICTORY_LINES)}\n")
            break

        if result == "lose":
            clear()
            print("╔══════════════════════════════════════════════════╗")
            print("║   ✦  C Y B E R   S T A R  :  W O R D  W A R S  ✦  ║")
            print("╚══════════════════════════════════════════════════╝\n")
            print(f"  ✕ ✕ ✕  EARTH HAS FALLEN  ✕ ✕ ✕")
            print(f"  The word was '{word.upper()}'.")
            print(f"  {random.choice(DEFEAT_LINES)}\n")
            break

    again = input("  Play again? (y/n) → ").strip().lower()
    if again == "y":
        play()
    else:
        print("\n  Sankofa — go back and fetch it. Until next time, warrior.\n")


if __name__ == "__main__":
    play()