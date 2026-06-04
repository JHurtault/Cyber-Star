import random
import os
import time

from audio import play_sfx, play_menu_music
from data import SHIP_ART, ENEMY_LORE, VOID_EVENTS, FACTIONS, COMMANDER_NAME

CRIT_CHANCE = 0.15
CLEAR = lambda: os.system("cls" if os.name == "nt" else "clear")

HEADER = """\
╔══════════════════════════════════════════════════╗
║   ✦  C Y B E R   S T A R  :  V O I D  W A R S  ✦  ║
║               Void Fleet Command                 ║
╚══════════════════════════════════════════════════╝"""

# Visual HP bar shown in combat
def hp_bar(current, maximum, width=20):
    filled = int((current / maximum) * width)
    return f"[{'█' * filled}{'░' * (width - filled)}] {current}/{maximum}"

def pause(secs=1.2):
    time.sleep(secs)

def print_header():
    print(HEADER + "\n")

# Clean exit from anywhere in the game
def quit_game():
    from audio import stop_audio
    stop_audio()
    print("\n  Session ended. Sankofa - until next time.\n")
    exit()

def check_quit(ans):
    if ans.strip() == "0":
        quit_game()

# Builds player dict from selected faction ship - 1 repair kit per wave
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

# Faction selection screen - loops until valid input
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

# Draws player and enemy ships side by side with stats below
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

# Handles all player actions each turn
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

    # Scan - no turn cost, holds until player presses enter
    if choice == "4":
        lore = ENEMY_LORE.get(enemy["name"], "No data found on this vessel.")
        hp_pct = int((enemy["hp"] / enemy["max_hp"]) * 100)
        print(f"\n  > SCAN: {enemy['name']}")
        print(f"    Hull integrity : {hp_pct}%")
        print(f"    Special weapon : {enemy['special']}")
        print(f"    Intel          : {lore}")
        input("\n  Press Enter to return to battle -> ")

    # Repair kit - 1 per wave, restores 30 HP
    elif choice == "5":
        if player.get("repair_kits", 0) > 0:
            player["hp"] = min(player["max_hp"], player["hp"] + 30)
            player["repair_kits"] -= 1
            print(f"\n  > Hull repair activated. +30 HP restored. {player['repair_kits']} kit(s) remaining.")
        else:
            print("\n  > No repair kits remaining.")

    # Attack - 15% chance to crit for double damage
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

    # Defend - caps shield at 80
    elif choice == "2":
        play_sfx("defend")
        player["shield"] = min(80, player["shield"] + 15)
        print(f"\n  > Shields reinforced. +15 shield -> {player['shield']} total.")

    # Special moves - faction specific, costs energy
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

# Enemy attacks - 30% chance to use special, 20% chance void event fires after
def enemy_turn(player, enemy):
    print(f"  -- {enemy['name'].upper()} ATTACKS -------------------------")
    use_special = random.random() < 0.30
    dmg  = random.randint(*enemy["special_dmg"]) if use_special else random.randint(*enemy["atk"])
    name = enemy["special"] if use_special else "standard strike"

    # Shield absorbs damage before HP is hit
    absorbed = min(player["shield"], dmg)
    player["shield"] = max(0, player["shield"] - absorbed)
    player["hp"]     = max(0, player["hp"] - (dmg - absorbed))
    print(f"\n  > {enemy['name']} uses {name} for {dmg} damage.")
    if absorbed:
        print(f"    Shield absorbed {absorbed}. Hull took {dmg - absorbed}.")

    # Void event - fires randomly after enemy attack
    if random.random() < 0.20:
        event_name, event_desc, event_type, event_val = random.choice(VOID_EVENTS)
        print(f"\n  ! VOID EVENT: {event_name} - {event_desc}")
        if event_type == "shield" and event_val > 0:
            enemy["hp"] = min(enemy["max_hp"], enemy["hp"] + event_val)
        elif event_type == "energy":
            player["energy"] = max(0, player["energy"] + event_val)
        elif event_type == "shield_p":
            player["shield"] = max(0, player["shield"] + event_val)
    pause()

# Heals HP and restores 1 energy between enemies in the same wave
def restore_between_fights(player):
    heal = random.randint(25, 40)
    player["hp"]     = min(player["max_hp"], player["hp"] + heal)
    player["energy"] = min(6, player["energy"] + 1)
    print(f"\n  > Ship systems stabilize. +{heal} HP, +1 energy.")
    pause(1.5)

# Main combat loop - alternates player and enemy turns
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