import random, os, csv

def load_words(filepath="CyberStar_words.csv"):
    with open(filepath, newline="") as f:
        return [row["word"] for row in csv.DictReader(f)]

WORD_LIST = load_words()

FLEETS = [
    ("OUTER FLEET", [
        ("Ogun-X Dreadnought",  "████████████"),
        ("Sankofa Void Reaper", "██████████"),
        ("Neon Griot Specter",  "████████"),
        ("Adinkra Wraith",      "██████"),
    ]),
    ("INNER FLEET", [
        ("Kente Glitch Runner", "████████████"),
        ("Juju Wire Shade",     "██████████"),
        ("Nyame Ghost Bit",     "████████"),
        ("Anansi Cipher Blade", "██████"),
    ]),
    ("EARTH DEFENSE FLEET", [
        ("Ashanti Iron Aegis",  "████████████"),
        ("Oduduwa Last Stand",  "██████████"),
        ("Zulu Neon Bastion",   "████████"),
        ("Sankofa Final Ark",   "██████"),
    ]),
]

DESTROYED_MSGS = [
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

HEADER = (
    "╔══════════════════════════════════════════════════╗\n"
    "║   ✦  C Y B E R   S T A R  :  W O R D  W A R S  ✦  ║\n"
    "╚══════════════════════════════════════════════════╝"
)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_word(word, guessed):
    return "  ".join(c.upper() if c in guessed else "_" for c in word)

def get_fleet(base, word_length):
    return list(base[:min(max(word_length - 3, 2), len(base))])

def render(word, guessed, wrong, fleet, fleet_name, lost, reinf, idx, msg=""):
    clear()
    print(HEADER + "\n")
    print(f"  ── {fleet_name} (Line {idx + 1} of 3) ──────────────────────")
    for i, (name, hull) in enumerate(fleet):
        if i < lost:
            print(f"  ✕  {name:<24}  {'~' * len(hull)}  [STARSHIP DESTROYED!]")
        else:
            print(f"  ▶  {name:<24}  {hull}")
    reinf_str = "✔ AVAILABLE  (type '9' to use  |  '0' to quit)" if reinf else "✘ USED  (type '0' to quit)"
    print(f"\n  Ships remaining : {len(fleet) - lost} / {len(fleet)}")
    print(f"  Reinforcement   : {reinf_str}")
    print(f"\n  WORD:    {display_word(word, guessed)}")
    print(f"\n  Wrong letters:  {', '.join(sorted(wrong)).upper() if wrong else '—'}")
    if msg:
        print(f"\n  ▶  {msg}")
    print()

def play_fleet(word, guessed, wrong, idx):
    fleet_name, base = FLEETS[idx]
    fleet = get_fleet(base, len(word))
    lost, reinf = 0, True
    msg = (f"⬡ {fleet_name} deployed. {len(fleet)} vessels ready. Guess a letter."
           if idx == 0 else
           f"⬡ {fleet_name} now active. Enemy has broken through. Guess a letter.")

    while True:
        render(word, guessed, wrong, fleet, fleet_name, lost, reinf, idx, msg)

        if all(c in guessed for c in word):
            return "win"

        if lost >= len(fleet):
            if idx < 2:
                print(f"  ⚠  {fleet_name} gone. Enemy is closing in on Earth.")
                input("  Press Enter to deploy the next fleet...")
                return "next"
            return "lose"

        raw = input("  Your guess (letter), '9' for Reinforcement, or '0' to quit → ").strip().lower()

        if raw == "0":
            print("\n  ⚠  Session ended. Sankofa — go back and fetch it. Until next time.\n")
            exit()
        elif raw == "9":
            if not reinf:
                msg = "⚠ Reinforcement already used. No more backup this fleet."
            elif lost == 0:
                msg = "⚠ No ships lost yet. Hold your reinforcement."
            else:
                reinf = False
                lost -= 1
                msg = f"★ Reinforcement deployed. {fleet[lost][0]} is back in the fight."
        elif len(raw) == 1 and raw.isalpha():
            if raw in guessed or raw in wrong:
                msg = f"Already guessed '{raw.upper()}'. Try a different letter."
            elif raw in word:
                guessed.add(raw)
                count = word.count(raw)
                msg = f"✓ '{raw.upper()}' found. {count} occurrence{'s' if count > 1 else ''} revealed."
            else:
                wrong.add(raw)
                dmsg = DESTROYED_MSGS[min(lost, len(DESTROYED_MSGS) - 1)]
                lost += 1
                if lost <= len(fleet):
                    msg = f"✗ '{raw.upper()}' not found. {fleet[lost-1][0]}: STARSHIP DESTROYED! {dmsg} {len(fleet)-lost} ship(s) remain."
                else:
                    msg = f"✗ '{raw.upper()}' not found. Final ship lost."
        else:
            msg = "Single letter only. '9' for reinforcement. '0' to quit."

def play():
    word = random.choice(WORD_LIST)
    guessed, wrong = set(), set()

    for idx in range(3):
        result = play_fleet(word, guessed, wrong, idx)
        if result in ("win", "lose"):
            clear()
            print(HEADER + "\n")
            if result == "win":
                print(f"  ★ ★ ★  MISSION COMPLETE  ★ ★ ★")
                print(f"  The word was '{word.upper()}'. {random.choice(VICTORY_LINES)}\n")
            else:
                print(f"  ✕ ✕ ✕  EARTH HAS FALLEN  ✕ ✕ ✕")
                print(f"  The word was '{word.upper()}'. {random.choice(DEFEAT_LINES)}\n")
            break

    if input("  Play again? (y/n) → ").strip().lower() == "y":
        play()
    else:
        print("\n  Sankofa — go back and fetch it. Until next time, warrior.\n")

if __name__ == "__main__":
    play()