## Update - June 2026

Refactored the codebase into 4 separate modules. Main file is now 85 lines.

1. `audio.py` - handles all music and sound effects
2. `data.py` - stores all game data, factions, ships and lore
3. `combat.py` - all combat logic and player actions
4. `Cyber_Star.py` - main entry point, runs the game loop

## Future Improvements

1. I would like to pull the words from a external source somewhere on the internet so it could be randomly used. This would ensure no player knows the word before hand.

2. I would like to implement some ASCII art in the future to make the aesthetics look more appealing. Will try and use this online resource: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false


## Audio Resources

**pygame.mixer - Official Documentation**
Used to initialize the audio system, load and play music tracks and sound effects.
https://www.pygame.org/docs/ref/mixer.html

**pygame.mixer.music - Official Documentation**
Used specifically for background music streaming and track switching between waves.
https://www.pygame.org/docs/ref/music.html

**pygame.mixer.Sound - Official Documentation**
Used to load and play short sound effects for attack, defend and special moves.
https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound

**SDL2 Audio Documentation**
pygame is built on top of SDL2. This explains the underlying audio system behavior on macOS and why proper mixer init and quit order matters.
https://wiki.libsdl.org/SDL2/CategoryAudio

**Git LFS - Large File Storage**
Used to store WAV audio files in the GitHub repo without hitting file size limits.
https://git-lfs.com

**AudioHero - Royalty Free Audio**
Source for all music and sound effect files used in the game. Royalty free license included with purchase.
https://audiohero.com

## Audio Bug Notes

Ran into a persistent issue where background music tracks were playing on top of each other when switching between waves. Traced it back to two root causes. First, `pygame.mixer.init()` was being called at module level and again inside a function, creating two separate audio sessions that never got properly cleaned up. Second, `pygame.mixer.Sound` objects loaded into the SFX cache were 30-80 seconds long, causing them to loop and stack on every button press.

Fixed it by removing the duplicate init call, building a single `init_audio()` function that does one clean `quit()` then `init()` then SFX reload in the right order. Also swapped out the long SFX files for short ones under 2 seconds and capped playback with `maxtime=2000`.

Key docs that had the answers:

- https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
- https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.quit
- https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.load
- https://stackoverflow.com/questions/44361196/pygame-mixer-music-plays-over-itself