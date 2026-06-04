import random
import os
import time

try:
    import pygame
    AUDIO = True
except ImportError:
    AUDIO = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MENU_MUSIC    = os.path.join(BASE_DIR, "Colony Sunrise", "Deep-Africa-Sunrise-WVM013601.wav")
WAVE_MUSIC    = [
    os.path.join(BASE_DIR, "Echoes from Epsilon", "AAM510_08_Calamity.wav"),
    os.path.join(BASE_DIR, "Echoes from Epsilon", "AAM552_34_CodeConspiracy_Full.wav"),
    os.path.join(BASE_DIR, "Echoes from Epsilon", "16-Darkness-Growing_Full_FM2235.wav"),
]
VICTORY_MUSIC = os.path.join(BASE_DIR, "Colony Sunrise", "Deep-Africa-Sunrise-WVM013601.wav")
DEFEAT_MUSIC  = os.path.join(BASE_DIR, "Cosmic Horror Tech", "CosmicStorm.wav")

SFX_FILES = {
    "attack":  os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Lazers and Tazers", "Pulsing Vaporwave B.wav"),
    "defend":  os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Pulse and Surge", "Mini Electric Swell.wav"),
    "special": os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Lazers and Tazers", "Subtle Shooter A.wav"),
}
SFX_CACHE = {}
CURRENT_TRACK = {"path": None}

def init_audio():
    if not AUDIO:
        return
    try:
        pygame.mixer.quit()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        SFX_CACHE.clear()
        for key, path in SFX_FILES.items():
            if os.path.isfile(path):
                try:
                    SFX_CACHE[key] = pygame.mixer.Sound(path)
                    SFX_CACHE[key].set_volume(0.25)
                except Exception:
                    pass
    except Exception as e:
        print(f"  [audio init] {e}")

def play_sfx(key):
    if not AUDIO:
        return
    sound = SFX_CACHE.get(key)
    if sound:
        try:
            sound.stop()
            sound.play(maxtime=2000)
        except Exception:
            pass

def play_music(path, volume=0.6, loop=-1):
    if not AUDIO or not os.path.isfile(path):
        return
    if CURRENT_TRACK["path"] == path:
        return
    try:
        pygame.mixer.music.stop()
        time.sleep(0.2)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
        CURRENT_TRACK["path"] = path
    except Exception as e:
        print(f"  [audio] {e}")

def play_menu_music():
    play_music(MENU_MUSIC, volume=0.6, loop=-1)

def play_wave_music(wave_index):
    path = WAVE_MUSIC[wave_index % len(WAVE_MUSIC)]
    CURRENT_TRACK["path"] = None
    play_music(path, volume=0.55, loop=-1)

def play_result_music(result):
    path = VICTORY_MUSIC if result == "victory" else DEFEAT_MUSIC
    CURRENT_TRACK["path"] = None
    play_music(path, volume=0.6, loop=0)

def play_intro():
    init_audio()
    play_menu_music()

def stop_audio():
    if AUDIO:
        try:
            pygame.mixer.music.stop()
            CURRENT_TRACK["path"] = None
        except Exception:
            pass

# -- Faction definitions -------------------------------------------------------

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

# -- Ship ASCII art ------------------------------------------------------------

SHIP_ART = {
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
        "name": "EARTH DEFENSE - FINAL WAVE",
        "enemies": [
            {"name": "Ogun Iron Destroyer",  "art": "destroyer", "hp": 90,  "max_hp": 90,  "atk": (18, 24), "special": "Iron Surge",       "special_dmg": (28, 38)},
            {"name": "Nyame Void Titan",     "art": "titan",     "hp": 100, "max_hp": 100, "atk": (20, 26), "special": "Sky Collapse",     "special_dmg": (30, 42)},
            {"name": "Sankofa Final Reaper", "art": "reaper",    "hp": 120, "max_hp": 120, "atk": (22, 28), "special": "Ancestor's Wrath", "special_dmg": (34, 46)},
        ]
    },
]

CRIT_CHANCE = 0.15

COMMANDER_NAME = {"name": "Commander"}

ENEMY_LORE = {
    "Void Drone MK-I":     "A disposable recon unit. Mass produced in the outer colonies. No soul, no mercy.",
    "Neon Jackal":         "A scavenger class fighter reprogrammed for war. Unpredictable attack patterns.",
    "Griot-Class Stalker": "Named after the ancient storytellers. It records every move before it strikes.",
    "Adinkra War Sentinel":"Etched with sacred symbols that absorb energy. Older than the conflict itself.",
    "Juju Wraith":         "A ghost ship running on spiritual code. Its origins are unknown even to its pilots.",
    "Anansi Web Cruiser":  "Modeled after the trickster spider god. It fights by tangling you in its systems.",
    "Ogun Iron Destroyer": "Forged in the image of the iron god. Built to outlast everything it faces.",
    "Nyame Void Titan":    "A sky god vessel. It believes it cannot be defeated. It has been right until now.",
    "Sankofa Final Reaper":"The last ship built before the war ended the shipyards. It carries that grief.",
}

VOID_EVENTS = [
    ("VOID SURGE",       "enemy shields restored.",         "shield",  20),
    ("KENTE DISRUPTION", "your energy drops by 1.",         "energy",  -1),
    ("STATIC PULSE",     "your shield drops by 10.",        "shield_p",-10),
    ("ANCESTOR BLOCK",   "enemy deflects your next strike.","block",    1),
    ("NEON SURGE",       "enemy gains +5 attack this turn.","atk_up",   5),
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

def quit_game():
    stop_audio()
    print("\n  Session ended. Sankofa - until next time.\n")
    exit()

def check_quit(ans):
    if ans.strip() == "0":
        quit_game()

def choose_faction():
    while True:
        play_menu_music()
        CLEAR()
        print_header()
        print("  -- CHOOSE YOUR FACTION -------------------------\n")
        for key, f in FACTIONS.items():
            print(f"  {key}. {f['name']:<12} - {f['desc']}")
        print()
        choice = input("  Enter 1, 2, or 3, or 0 to quit -> ").strip()
        check_quit(choice)
        if choice in FACTIONS:
            faction = FACTIONS[choice]
            CLEAR()
            print_header()
            print(f"  Faction selected: {faction['name']}\n")
            print(f"  Your ships for this run:\n")
            for i, ship in enumerate(faction["ships"], 1):
                print(f"  Wave {i}: {ship['name']}")
                print(f"          HP {ship['hp']}  Shield {ship['shield']}  Energy {ship['energy']} energy")
                for move in ship["specials"]:
                    print(f"          {move['cost']} {move['name']} - {move['desc']}")
                print()
            check_quit(input("  Press Enter to deploy, or 0 to quit -> "))
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
        "repair_kits": 1,
    }

def show_status(player, enemy, wave_name, enemy_num, total_enemies):
    CLEAR()
    print_header()
    print(f"  -- {wave_name}  |  Enemy {enemy_num}/{total_enemies} ----------------------\n")

    p_art = SHIP_ART.get(player["art_key"], [])
    e_art = SHIP_ART.get(enemy.get("art", "drone"), SHIP_ART["drone"])
    max_lines = max(len(p_art), len(e_art))
    p_art = p_art + [""] * (max_lines - len(p_art))
    e_art = e_art + [""] * (max_lines - len(e_art))
    for pl, el in zip(p_art, e_art):
        print(f"  {pl:<26}        {el}")

    print()
    repair_str = f"  Repair Kits: {player['repair_kits']}" if player['repair_kits'] > 0 else "  Repair Kits: NONE"
    print(f"  {player['name']:<22}{hp_bar(player['hp'], player['max_hp'])}  Shield {player['shield']}  Energy {player['energy']}  {repair_str}")
    print(f"  {enemy['name']:<22}{hp_bar(enemy['hp'], enemy['max_hp'])}\n")

def player_turn(player, enemy):
    print("  -- YOUR TURN -----------------------------------")
    print("  1. Attack        - standard strike")
    print("  2. Defend        - restore 15 shield")
    print(f"  3. Special moves - costs energy (you have {player['energy']} energy)")
    print("  4. Scan enemy    - reveal enemy intel")
    kits = player.get("repair_kits", 0)
    print(f"  5. Repair kit    - restore 30 HP ({kits} remaining)")
    print("  0. Quit\n")

    choice = input("  Action -> ").strip()
    check_quit(choice)

    if choice == "4":
        lore = ENEMY_LORE.get(enemy["name"], "No data found on this vessel.")
        hp_pct = int((enemy["hp"] / enemy["max_hp"]) * 100)
        print(f"\n  > SCAN: {enemy['name']}")
        print(f"    Hull integrity : {hp_pct}%")
        print(f"    Special weapon : {enemy['special']}")
        print(f"    Intel          : {lore}")
        input("\n  Press Enter to return to battle -> ")

    elif choice == "5":
        if player.get("repair_kits", 0) > 0:
            heal = 30
            player["hp"] = min(player["max_hp"], player["hp"] + heal)
            player["repair_kits"] -= 1
            print(f"\n  > Hull repair activated. +{heal} HP restored. {player['repair_kits']} kit(s) remaining.")
        else:
            print("\n  > No repair kits remaining.")

    elif choice == "1":
        play_sfx("attack")
        dmg = random.randint(14, 22)
        crit = random.random() < CRIT_CHANCE
        if crit:
            dmg *= 2
        enemy["hp"] = max(0, enemy["hp"] - dmg)
        if crit:
            print(f"\n  > ANCESTOR GUIDED STRIKE! Critical hit on {enemy['name']} for {dmg} damage!")
        else:
            print(f"\n  > Strike hits {enemy['name']} for {dmg} damage.")
    elif choice == "2":
        play_sfx("defend")
        gain = 15
        player["shield"] = min(80, player["shield"] + gain)
        print(f"\n  > Shields reinforced. +{gain} shield -> {player['shield']} total.")
    elif choice == "3":
        print()
        for i, move in enumerate(player["specials"], 1):
            avail = "OK" if player["energy"] >= move["cost"] else "NO"
            print(f"  {i}. [{avail}] {move['name']} (cost {move['cost']}) - {move['desc']}")
        print("  0. Back\n")
        sub = input("  Choose move -> ").strip()
        check_quit(sub)
        if sub in ("1", "2", "3"):
            move = player["specials"][int(sub) - 1]
            if player["energy"] >= move["cost"]:
                play_sfx("special")
                player["energy"] -= move["cost"]
                dmg = random.randint(*move["dmg"])
                crit = random.random() < CRIT_CHANCE
                if crit:
                    dmg *= 2
                enemy["hp"] = max(0, enemy["hp"] - dmg)
                if crit:
                    print(f"\n  > ANCESTOR GUIDED STRIKE! {move['name']} critical for {dmg} damage! {player['energy']} energy remaining.")
                else:
                    print(f"\n  > {move['name']} hits for {dmg} damage! {player['energy']} energy remaining.")
            else:
                print(f"\n  > Not enough energy for {move['name']}.")
        else:
            print("\n  > Held position.")
    else:
        print("\n  > Invalid input. Turn skipped.")

    pause()

def enemy_turn(player, enemy):
    print(f"  -- {enemy['name'].upper()} ATTACKS -------------------------")
    use_special = random.random() < 0.30
    dmg  = random.randint(*enemy["special_dmg"]) if use_special else random.randint(*enemy["atk"])
    name = enemy["special"] if use_special else "standard strike"

    absorbed = min(player["shield"], dmg)
    player["shield"] = max(0, player["shield"] - absorbed)
    player["hp"]     = max(0, player["hp"] - (dmg - absorbed))

    print(f"\n  > {enemy['name']} uses {name} for {dmg} damage.")
    if absorbed:
        print(f"    Shield absorbed {absorbed}. Hull took {dmg - absorbed}.")

    if random.random() < 0.20:
        event_name, event_desc, event_type, event_val = random.choice(VOID_EVENTS)
        print(f"\n  ! VOID EVENT: {event_name} - {event_desc}")
        if event_type == "shield":
            enemy["hp"] = max(0, min(enemy["max_hp"], enemy["hp"] - event_val)) if event_val < 0 else enemy["hp"]
            if event_val > 0:
                enemy["hp"] = min(enemy["max_hp"], enemy["hp"] + event_val)
        elif event_type == "energy":
            player["energy"] = max(0, player["energy"] + event_val)
        elif event_type == "shield_p":
            player["shield"] = max(0, player["shield"] + event_val)

    pause()

def restore_between_fights(player):
    heal = random.randint(25, 40)
    player["hp"]     = min(player["max_hp"], player["hp"] + heal)
    player["energy"] = min(6, player["energy"] + 1)
    print(f"\n  > Ship systems stabilize. +{heal} HP, +1 energy.")
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
    print(f"\n  * {enemy['name']} destroyed!")
    pause()
    return True

def run_wave(player, wave, wave_num):
    CLEAR()
    print_header()
    print(f"  -- WAVE {wave_num} OF 3: {wave['name']} ------------------------\n")
    print(f"  Commander: {COMMANDER_NAME['name']}  |  Ship: {player['name']}")
    print(f"  {len(wave['enemies'])} enemy ships detected. Prepare for engagement.")
    check_quit(input("\n  Press Enter to begin, or 0 to quit -> "))

    play_wave_music(wave_num - 1)
    enemies = [dict(e) for e in wave["enemies"]]
    for i, enemy in enumerate(enemies, 1):
        if not fight(player, enemy, wave["name"], i, len(enemies)):
            return False
        if i < len(enemies):
            CLEAR()
            print_header()
            print(f"  Enemy {i} down. Next target incoming...")
            restore_between_fights(player)
            check_quit(input("  Press Enter to continue, or 0 to quit -> "))

    return True

def play():
    CLEAR()
    print_header()
    play_intro()
    print("  Turn-Based Void Combat\n")
    print("  Three waves stand between the enemy and Earth.")
    print("  Survive all three to win.\n")
    print("  CONTROLS:  1 = Attack   2 = Defend   3 = Special Moves   0 = Quit\n")
    check_quit(input("  Press Enter to continue, or 0 to quit -> "))

    CLEAR()
    print_header()
    raw_name = input("  Enter your commander name (or press Enter for default) -> ").strip()
    COMMANDER_NAME["name"] = raw_name if raw_name else "Commander"
    print(f"\n  Commander {COMMANDER_NAME['name']} reporting for duty.\n")
    pause(1.0)

    faction = choose_faction()

    for wave_num, wave in enumerate(WAVES, 1):
        player = build_player(faction["ships"][wave_num - 1])
        if wave_num > 1:
            CLEAR()
            print_header()
            print(f"  * Commander {COMMANDER_NAME['name']} upgrading to {player['name']}.")
            print(f"  HP {player['hp']}  Shield {player['shield']}  Energy {player['energy']}\n")
            check_quit(input("  Press Enter to deploy, or 0 to quit -> "))

        survived = run_wave(player, wave, wave_num)

        if not survived:
            play_result_music("defeat")
            CLEAR()
            print_header()
            print("  X X X  EARTH HAS FALLEN  X X X\n")
            print(f"  Commander {COMMANDER_NAME['name']} has fallen. The griots weep.\n")
            break

        CLEAR()
        print_header()
        if wave_num < 3:
            print(f"  * {wave['name']} cleared. The enemy retreats... for now.\n")
            check_quit(input("  Press Enter to face the next wave, or 0 to quit -> "))
        else:
            play_result_music("victory")
            print("  * * *  MISSION COMPLETE  * * *\n")
            print("  All three waves defeated. Earth stands.")
            print(f"  Commander {COMMANDER_NAME['name']} - the griots will tell of this victory for generations.\n")

    if input("  Play again? (y/n) -> ").strip().lower() == "y":
        play()
    else:
        stop_audio()
        print("\n  Sankofa - go back and fetch it. Until next time.\n")

if __name__ == "__main__":
    play()