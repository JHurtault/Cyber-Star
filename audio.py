import os
import time

try:
    import pygame
    AUDIO = True
except ImportError:
    AUDIO = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Music file paths
MENU_MUSIC    = os.path.join(BASE_DIR, "Colony Sunrise", "Deep-Africa-Sunrise-WVM013601.wav")
WAVE_MUSIC    = [
    os.path.join(BASE_DIR, "Echoes from Epsilon", "AAM510_08_Calamity.wav"),
    os.path.join(BASE_DIR, "Echoes from Epsilon", "AAM552_34_CodeConspiracy_Full.wav"),
    os.path.join(BASE_DIR, "Echoes from Epsilon", "16-Darkness-Growing_Full_FM2235.wav"),
]
VICTORY_MUSIC = os.path.join(BASE_DIR, "Colony Sunrise", "Deep-Africa-Sunrise-WVM013601.wav")
DEFEAT_MUSIC  = os.path.join(BASE_DIR, "Cosmic Horror Tech", "CosmicStorm.wav")

# Sound effect file paths
SFX_FILES = {
    "attack":  os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Lazers and Tazers", "Pulsing Vaporwave B.wav"),
    "defend":  os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Pulse and Surge", "Mini Electric Swell.wav"),
    "special": os.path.join(BASE_DIR, "Cyberpunk Sound FX Pack Vol. 1", "Lazers and Tazers", "Subtle Shooter A.wav"),
}
SFX_CACHE = {}
CURRENT_TRACK = {"path": None}

# Init mixer, load all SFX into cache
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

# Play a sound effect by key name
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

# Stop current track and load a new one
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

# Reset track state so new wave always forces a fresh load
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