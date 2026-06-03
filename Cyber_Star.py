import random
import os
import time
import glob

try:
    import pygame
    pygame.mixer.init()
    AUDIO = True
except ImportError:
    AUDIO = False

SOUND_PATHS = [
    "Cyberpunk Sound FX Pack Vol. 1/CyberCity Soundscapes",
    "Cyberpunk Sound FX Pack Vol. 1/Errors and Alerts",
    "Cyberpunk Sound FX Pack Vol. 1/Pulse and Surge",
]

def find_intro_sound():
    for folder in SOUND_PATHS:
        for ext in ("*.wav", "*.ogg", "*.mp3"):
            files = glob.glob(os.path.join(folder, ext))
            if files:
                return files[0]
    return None

def play_intro():
    if not AUDIO:
        return
    path = find_intro_sound()
    if path:
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(0)
        except Exception:
            pass

def stop_audio():
    if AUDIO:
        try:
            pygame.mixer.music.stop()
        except Exception:
            pass

# ── Faction definitions ───────────────────────────────────────────────────────

FACTIONS = {
    "1": {
        "name": "Shango",
        "desc": "Yoruba god of thunder and lightning. High damage, lower shields.",
        "ships": [
            {
                "name":    "Shango Thunder Skiff",
                "art_key": "shango_1",
                "hp": 100, "max_hp": 100, "shield": 25, "energy": 3,
                "specials": [
                    {"name": "Lightning Strike", "dmg": (22, 32), "cost": 1, "desc": "Calls down a thunder bolt"},
                    {"name": "Storm Surge",       "dmg": (32, 44), "cost": 2, "desc": "Rapid electrical volley"},
                    {"name": "Oya's Fury",        "dmg": (44, 58), "cost": 3, "desc": "Channel the storm goddess"},
                ],
            },
            {
                "name":    "Shango Storm Cruiser",
                "art_key": "shango_2",
                "hp": 115, "max_hp": 115, "shield": 30, "energy": 3,
                "specials": [
                    {"name": "Thunder Volley",   "dmg": (24, 36), "cost": 1, "desc": "Chain lightning barrage"},
                    {"name": "Arc Cascade",      "dmg": (36, 48), "cost": 2, "desc": "Arcing electrical field"},
                    {"name": "Oya's Fury",       "dmg": (48, 62), "cost": 3, "desc": "Channel the storm goddess"},
                ],
            },
            {
                "name":    "Shango Tempest Destroyer",
                "art_key": "shango_3",
                "hp": 130, "max_hp": 130, "shield": 35, "energy": 4,
                "specials": [
                    {"name": "Thunderclap Beam", "dmg": (28, 40), "cost": 1, "desc": "Focused thunder cannon"},
                    {"name": "Storm Wall",       "dmg": (40, 54), "cost": 2, "desc": "Wall of crackling energy"},
                    {"name": "Oya's Fury",       "dmg": (54, 70), "cost": 3, "desc": "Channel the storm goddess"},
                ],
            },
        ],
    },
    "2": {
        "name": "Kushites",
        "desc": "Ancient Nile warriors. Balanced stats, iron-forged shields.",
        "ships": [
            {
                "name":    "Kush Iron Skiff",
                "art_key": "kush_1",
                "hp": 110, "max_hp": 110, "shield": 45, "energy": 3,
                "specials": [
                    {"name": "Apedemak's Roar",  "dmg": (18, 28), "cost": 1, "desc": "Lion-god war cry attack"},
                    {"name": "Meroe Iron Rain",  "dmg": (28, 40), "cost": 2, "desc": "Forged iron projectile burst"},
                    {"name": "Kandake's Wrath",  "dmg": (40, 54), "cost": 3, "desc": "Strike of the warrior queen"},
                ],
            },
            {
                "name":    "Kush Nile Warship",
                "art_key": "kush_2",
                "hp": 125, "max_hp": 125, "shield": 52, "energy": 3,
                "specials": [
                    {"name": "Pyramid Pulse",    "dmg": (20, 32), "cost": 1, "desc": "Sacred geometry energy wave"},
                    {"name": "Meroe Iron Rain",  "dmg": (32, 44), "cost": 2, "desc": "Forged iron projectile burst"},
                    {"name": "Kandake's Wrath",  "dmg": (44, 58), "cost": 3, "desc": "Strike of the warrior queen"},
                ],
            },
            {
                "name":    "Kush Apedemak Titan",
                "art_key": "kush_3",
                "hp": 140, "max_hp": 140, "shield": 60, "energy": 4,
                "specials": [
                    {"name": "Lion God Strike",  "dmg": (24, 36), "cost": 1, "desc": "Apedemak's lion-headed fury"},
                    {"name": "Nile Surge",       "dmg": (36, 50), "cost": 2, "desc": "Ancient river force unleashed"},
                    {"name": "Kandake's Wrath",  "dmg": (50, 66), "cost": 3, "desc": "Strike of the warrior queen"},
                ],
            },
        ],
    },
    "3": {
        "name": "Yoruba",
        "desc": "Orisha-blessed fleet. High energy, powerful special moves.",
        "ships": [
            {
                "name":    "Yoruba Orisha Skiff",
                "art_key": "yoruba_1",
                "hp": 95, "max_hp": 95, "shield": 30, "energy": 4,
                "specials": [
                    {"name": "Ogun's Blade",     "dmg": (20, 30), "cost": 1, "desc": "Iron god's cutting strike"},
                    {"name": "Ifa Oracle Beam",  "dmg": (30, 44), "cost": 2, "desc": "Divine knowledge weaponized"},
                    {"name": "Esu's Trickfire",  "dmg": (44, 60), "cost": 3, "desc": "Crossroads god confusion blast"},
                ],
            },
            {
                "name":    "Yoruba Ifa Cruiser",
                "art_key": "yoruba_2",
                "hp": 110, "max_hp": 110, "shield": 35, "energy": 4,
                "specials": [
                    {"name": "Ogun's Blade",     "dmg": (22, 34), "cost": 1, "desc": "Iron god's cutting strike"},
                    {"name": "Ifa Oracle Beam",  "dmg": (34, 48), "cost": 2, "desc": "Divine knowledge weaponized"},
                    {"name": "Esu's Trickfire",  "dmg": (48, 64), "cost": 3, "desc": "Crossroads god confusion blast"},
                ],
            },
            {
                "name":    "Yoruba Sango Battleship",
                "art_key": "yoruba_3",
                "hp": 125, "max_hp": 125, "shield": 40, "energy": 5,
                "specials": [
                    {"name": "Ogun's Blade",     "dmg": (26, 38), "cost": 1, "desc": "Iron god's cutting strike"},
                    {"name": "Ifa Oracle Beam",  "dmg": (38, 54), "cost": 2, "desc": "Divine knowledge weaponized"},
                    {"name": "Esu's Trickfire",  "dmg": (54, 72), "cost": 3, "desc": "Crossroads god confusion blast"},
                ],
            },
        ],
    },
}

# ── Ship ASCII art ────────────────────────────────────────────────────────────

SHIP_ART = {
    # Shango — jagged lightning-inspired hulls
    "shango_1": [
        "     /\\^/\\     ",
        "    /  ~  \\    ",
        "   |~|=|~| |   ",
        "  /~|   |~|\\  ",
        " /__|___|__|__\\ ",
        "    [~~~~~]    ",
    ],
    "shango_2": [
        "    /\\^^^/\\    ",
        "   / ~~~~~  \\  ",
        "  |~|=====|~|  ",
        " /~|       |~\\ ",
        "/~_|_______|_~\\",
        "   [~~~~~~~]   ",
        "  -~~--~~--~~- ",
    ],
    "shango_3": [
        "   /\\^^^^^/\\   ",
        "  /  ~~~~~  \\  ",
        " |~|=======|~| ",
        " |~| SHANGO|~| ",
        "/~_|_______|_~\\",
        "|~~[~~~~~~~]~~|",
        " \\~~~~~~~~~~~~~/ ",
        "  --~~~--~~~-- ",
    ],
    # Kushites — pyramid and iron motifs
    "kush_1": [
        "      /\\      ",
        "     /##\\     ",
        "    /####\\    ",
        "   |__##__|   ",
        "  /|  ||  |\\ ",
        " /_|__|__|_|\\ ",
    ],
    "kush_2": [
        "       /\\       ",
        "      /##\\      ",
        "     /####\\     ",
        "    /######\\    ",
        "   |___##___|   ",
        "  /|   ||   |\\ ",
        " /_|___|___|_|\\ ",
        "   [=======]   ",
    ],
    "kush_3": [
        "        /\\        ",
        "       /##\\       ",
        "      /####\\      ",
        "     /######\\     ",
        "    /########\\    ",
        "   |____##____|   ",
        "  /|    ||    |\\ ",
        " /_|____|____|_|\\ ",
        "   [=========]   ",
        "  -|--|--|--|-- ",
    ],
    # Yoruba — orisha symbol-inspired curved hulls
    "yoruba_1": [
        "    .(~~~).    ",
        "   /  |||  \\  ",
        "  | >( O )< |  ",
        "   \\  |||  /  ",
        "  __|_____|__  ",
        " /  [=====]  \\ ",
    ],
    "yoruba_2": [
        "   ..(~~~~~)..   ",
        "  /   |||||   \\  ",
        " |  >(  O  )<  | ",
        " |   |||||   |  ",
        "  \\___|___|___/  ",
        " /   [=====]   \\ ",
        "/__|_________|__\\",
    ],
    "yoruba_3": [
        "  ...(~~~~~~~)...  ",
        " /    |||||||    \\ ",
        "|  >>( ORISHA )<<  |",
        "|    |||||||    |  ",
        " \\____|_____|____/  ",
        "/    [=========]   \\",
        "|__|_____________|__|",
        "    --|||---|||--    ",
    ],
    # Enemy ships
    "drone": [
        "    .---.    ",
        "   /|o o|\\   ",
        "  | | - | |  ",
        "   \\_____/   ",
        "  -|--+--|-- ",
    ],
    "jackal": [
        "   /\\_/\\_/\\   ",
        "  | >   < |  ",
        "  |  ---  |  ",
        " /|_______|\\ ",
        "/_____________\\",
    ],
    "stalker": [
        "    __/\\__    ",
        "   /  ##  \\   ",
        "  | >[  ]< |  ",
        "  |________|  ",
        " /--/----\\--\\ ",
        "/___\\    /___\\",
    ],
    "sentinel": [
        "   ___|___    ",
        "  /  [#]  \\   ",
        " | >[   ]< |  ",
        " |  [###]  |  ",
        " |_________|  ",
        "/--/-----\\--\\ ",
    ],
    "wraith": [
        "  ~~/\\~~~~    ",
        " ~ /##\\ ~~ ~  ",
        "~ |>--<| ~ ~  ",
        " ~|~##~|~ ~   ",
        "  |_____|     ",
        " /~~~~~~~\\    ",
    ],
    "cruiser": [
        "   __|____|__   ",
        "  /   [##]   \\  ",
        " | >>[    ]<< | ",
        " |   [####]   | ",
        " |____________| ",
        "/--/--------\\--\\",
    ],
    "destroyer": [
        "  ____|______|____  ",
        " /    [######]    \\ ",
        "| >>>[        ]<<< |",
        "|     [######]     |",
        "|___________________|",
        "/----/----------\\----\\",
    ],
    "titan": [
        " ___|___|___|___  ",
        "/   [#########]  \\",
        "|>>>[         ]<<<|",
        "|   [#########]   |",
        "|   [#########]   |",
        "|_________________|",
        "/---/___________\\---\\",
    ],
    "reaper": [
        "_____|_____|_____|_____",
        "\\    [###########]    /",
        " |>>>[           ]<<<| ",
        " |   [###########]   | ",
        " |   [  REAPER   ]   | ",
        " |   [###########]   | ",
        " |___________________|  ",
        "/----/             \\----\\",
        "\\___/_______________\\___/",
    ],
}

WAVES = [
    {
        "name": "OUTER FLEET",
        "enemies": [
            {"name": "Void Drone MK-I",    "art": "drone",     "hp": 30,  "max_hp": 30,  "atk": (6, 12),  "special": "Plasma Sting",    "special_dmg": (14, 20)},
            {"name": "Neon Jackal",         "art": "jackal",    "hp": 40,  "max_hp": 40,  "atk": (8, 14),  "special": "Static Burst",    "special_dmg": (16, 24)},
            {"name": "Griot-Class Stalker", "art": "stalker",   "hp": 50,  "max_hp": 50,  "atk": (10, 16), "special": "Kente Scramble",  "special_dmg": (18, 26)},
        ]
    },
    {
        "name": "INNER FLEET",
        "enemies": [
            {"name": "Adinkra War Sentinel", "art": "sentinel", "hp": 60,  "max_hp": 60,  "atk": (12, 18), "special": "Symbol Strike",   "special_dmg": (22, 30)},
            {"name": "Juju Wraith",           "art": "wraith",   "hp": 70,  "max_hp": 70,  "atk": (14, 20), "special": "Soul Drain",      "special_dmg": (24, 34)},
            {"name": "Anansi Web Cruiser",    "art": "cruiser",  "hp": 80,  "max_hp": 80,  "atk": (16, 22), "special": "Cyber Web Trap",  "special_dmg": (26, 36)},
        ]
    },
    {
        "name": "EARTH DEFENSE — FINAL WAVE",
        "enemies": [
            {"name": "Ogun Iron Destroyer",  "art": "destroyer", "hp": 90,  "max_hp": 90,  "atk": (18, 24), "special": "Iron Surge",       "special_dmg": (28, 38)},
            {"name": "Nyame Void Titan",     "art": "titan",     "hp": 100, "max_hp": 100, "atk": (20, 26), "special": "Sky Collapse",     "special_dmg": (30, 42)},
            {"name": "Sankofa Final Reaper", "art": "reaper",    "hp": 120, "max_hp": 120, "atk": (22, 28), "special": "Ancestor's Wrath", "special_dmg": (34, 46)},
        ]
    },
]

CLEAR = lambda: os.system("cls" if os.name == "nt" else "clear")

HEADER = """\
╔══════════════════════════════════════════════════╗
║   ✦  C Y B E R   S T A R  :  V O I D  W A R S  ✦  ║
║               Void Fleet Command                 ║
╚══════════════════════════════════════════════════╝"""

def hp_bar(current, maximum, width=20):
    filled = int((current / maximum) * width)
    return f"[{'█' * filled}{'░' * (width - filled)}] {current}/{maximum}"

def pause(secs=1.2):
    time.sleep(secs)

def print_header():
    print(HEADER + "\n")

def choose_faction():
    while True:
        CLEAR()
        print_header()
        print("  ── CHOOSE YOUR FACTION ─────────────────────────\n")
        for key, f in FACTIONS.items():
            print(f"  {key}. {f['name']:<12} — {f['desc']}")
        print()
        choice = input("  Enter 1, 2, or 3 → ").strip()
        if choice in FACTIONS:
            faction = FACTIONS[choice]
            CLEAR()
            print_header()
            print(f"  Faction selected: {faction['name']}\n")
            print(f"  Your ships for this run:\n")
            for i, ship in enumerate(faction["ships"], 1):
                print(f"  Wave {i}: {ship['name']}")
                print(f"          HP {ship['hp']}  Shield {ship['shield']}  Energy ⚡{ship['energy']}")
                for move in ship["specials"]:
                    print(f"          ⚡{move['cost']} {move['name']} — {move['desc']}")
                print()
            input("  Press Enter to deploy...")
            return faction
        print("  Invalid choice. Enter 1, 2, or 3.")
        pause(0.8)

def build_player(ship):
    return {
        "name":    ship["name"],
        "art_key": ship["art_key"],
        "hp":      ship["hp"],
        "max_hp":  ship["max_hp"],
        "shield":  ship["shield"],
        "energy":  ship["energy"],
        "specials": ship["specials"],
    }

def show_status(player, enemy, wave_name, enemy_num, total_enemies):
    CLEAR()
    print_header()
    print(f"  ── {wave_name}  │  Enemy {enemy_num}/{total_enemies} ──────────────────────\n")

    p_art = SHIP_ART.get(player["art_key"], [])
    e_art = SHIP_ART.get(enemy.get("art", "drone"), SHIP_ART["drone"])
    max_lines = max(len(p_art), len(e_art))
    p_art = p_art + [""] * (max_lines - len(p_art))
    e_art = e_art + [""] * (max_lines - len(e_art))
    for pl, el in zip(p_art, e_art):
        print(f"  {pl:<26}        {el}")

    print()
    print(f"  {player['name']:<22}{hp_bar(player['hp'], player['max_hp'])}  🛡 {player['shield']}  ⚡ {player['energy']} energy")
    print(f"  {enemy['name']:<22}{hp_bar(enemy['hp'], enemy['max_hp'])}\n")

def player_turn(player, enemy):
    print("  ── YOUR TURN ───────────────────────────────────")
    print("  1. Attack        — standard strike")
    print("  2. Defend        — restore 15 shield")
    print(f"  3. Special moves — costs energy (you have ⚡{player['energy']})")
    print("  0. Quit\n")

    choice = input("  Action → ").strip()

    if choice == "0":
        stop_audio()
        print("\n  Session ended. Sankofa — until next time.\n")
        exit()
    elif choice == "1":
        dmg = random.randint(14, 22)
        enemy["hp"] = max(0, enemy["hp"] - dmg)
        print(f"\n  ▶ Strike hits {enemy['name']} for {dmg} damage.")
    elif choice == "2":
        gain = 15
        player["shield"] = min(80, player["shield"] + gain)
        print(f"\n  ▶ Shields reinforced. +{gain} shield → {player['shield']} total.")
    elif choice == "3":
        print()
        for i, move in enumerate(player["specials"], 1):
            avail = "✔" if player["energy"] >= move["cost"] else "✘"
            print(f"  {i}. {avail} {move['name']} (⚡{move['cost']}) — {move['desc']}")
        print("  0. Back\n")
        sub = input("  Choose move → ").strip()
        if sub in ("1", "2", "3"):
            move = player["specials"][int(sub) - 1]
            if player["energy"] >= move["cost"]:
                player["energy"] -= move["cost"]
                dmg = random.randint(*move["dmg"])
                enemy["hp"] = max(0, enemy["hp"] - dmg)
                print(f"\n  ▶ {move['name']} hits for {dmg} damage! ⚡{player['energy']} energy remaining.")
            else:
                print(f"\n  ▶ Not enough energy for {move['name']}.")
        else:
            print("\n  ▶ Held position.")
    else:
        print("\n  ▶ Invalid input. Turn skipped.")

    pause()

def enemy_turn(player, enemy):
    print(f"  ── {enemy['name'].upper()} ATTACKS ─────────────────────────")
    use_special = random.random() < 0.30
    dmg  = random.randint(*enemy["special_dmg"]) if use_special else random.randint(*enemy["atk"])
    name = enemy["special"] if use_special else "standard strike"

    absorbed = min(player["shield"], dmg)
    player["shield"] = max(0, player["shield"] - absorbed)
    player["hp"]     = max(0, player["hp"] - (dmg - absorbed))

    print(f"\n  ▶ {enemy['name']} uses {name} for {dmg} damage.")
    if absorbed:
        print(f"    Shield absorbed {absorbed}. Hull took {dmg - absorbed}.")
    pause()

def restore_between_fights(player):
    heal = random.randint(12, 20)
    player["hp"]     = min(player["max_hp"], player["hp"] + heal)
    player["energy"] = min(6, player["energy"] + 1)
    print(f"\n  ▶ Ship systems stabilize. +{heal} HP, +1 energy.")
    pause(1.5)

def fight(player, enemy, wave_name, enemy_num, total_enemies):
    while enemy["hp"] > 0 and player["hp"] > 0:
        show_status(player, enemy, wave_name, enemy_num, total_enemies)
        player_turn(player, enemy)
        if enemy["hp"] <= 0:
            break
        show_status(player, enemy, wave_name, enemy_num, total_enemies)
        enemy_turn(player, enemy)

    if player["hp"] <= 0:
        return False
    print(f"\n  ★ {enemy['name']} destroyed!")
    pause()
    return True

def run_wave(player, wave, wave_num):
    CLEAR()
    print_header()
    print(f"  ── WAVE {wave_num} OF 3: {wave['name']} ────────────────────────\n")
    print(f"  Commanding: {player['name']}")
    print(f"  {len(wave['enemies'])} enemy ships detected. Prepare for engagement.")
    input("\n  Press Enter to begin...")

    enemies = [dict(e) for e in wave["enemies"]]
    for i, enemy in enumerate(enemies, 1):
        if not fight(player, enemy, wave["name"], i, len(enemies)):
            return False
        if i < len(enemies):
            CLEAR()
            print_header()
            print(f"  Enemy {i} down. Next target incoming...")
            restore_between_fights(player)
            input("  Press Enter to continue...")

    return True

def play():
    CLEAR()
    print_header()
    play_intro()
    print("  Turn-Based Void Combat\n")
    print("  Three waves stand between the enemy and Earth.")
    print("  Survive all three to win.\n")
    print("  CONTROLS:  1 = Attack   2 = Defend   3 = Special Moves   0 = Quit\n")
    input("  Press Enter to continue...")

    faction = choose_faction()

    for wave_num, wave in enumerate(WAVES, 1):
        player = build_player(faction["ships"][wave_num - 1])
        if wave_num > 1:
            CLEAR()
            print_header()
            print(f"  ★ Upgrading to {player['name']}.")
            print(f"  HP {player['hp']}  Shield {player['shield']}  Energy ⚡{player['energy']}\n")
            input("  Press Enter to deploy...")

        survived = run_wave(player, wave, wave_num)

        if not survived:
            stop_audio()
            CLEAR()
            print_header()
            print("  ✕ ✕ ✕  EARTH HAS FALLEN  ✕ ✕ ✕\n")
            print("  The void swallows all three fleets. The griots weep.\n")
            break

        CLEAR()
        print_header()
        if wave_num < 3:
            print(f"  ★ {wave['name']} cleared. The enemy retreats... for now.\n")
            input("  Press Enter to face the next wave...")
        else:
            stop_audio()
            print("  ★ ★ ★  MISSION COMPLETE  ★ ★ ★\n")
            print("  All three waves defeated. Earth stands.")
            print("  The griots will tell of this victory for generations.\n")

    if input("  Play again? (y/n) → ").strip().lower() == "y":
        play()
    else:
        stop_audio()
        print("\n  Sankofa — go back and fetch it. Until next time.\n")

if __name__ == "__main__":
    play()