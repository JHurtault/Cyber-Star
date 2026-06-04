# All static game data - factions, waves, art, lore, events

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

# 3 waves, 3 enemies each - gets harder every wave
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

# Ship ASCII art - player and enemy
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

# Lore text shown when player scans an enemy
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

# Random events that fire 20% of the time after an enemy attack
VOID_EVENTS = [
    ("VOID SURGE",       "enemy shields restored.",         "shield",  20),
    ("KENTE DISRUPTION", "your energy drops by 1.",         "energy",  -1),
    ("STATIC PULSE",     "your shield drops by 10.",        "shield_p",-10),
    ("ANCESTOR BLOCK",   "enemy deflects your next strike.","block",    1),
    ("NEON SURGE",       "enemy gains +5 attack this turn.","atk_up",   5),
]

# Stores commander name entered at game start
COMMANDER_NAME = {"name": "Commander"}