from audio import play_intro, play_wave_music, play_result_music, stop_audio
from data import WAVES, COMMANDER_NAME
from combat import build_player, choose_faction, fight, restore_between_fights, check_quit, CLEAR, print_header, pause

# Entry point - handles title, commander name, faction select and wave loop
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

    # Each wave upgrades the player ship automatically
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

# Runs all 3 enemies in a wave, heals between each fight
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

if __name__ == "__main__":
    play()