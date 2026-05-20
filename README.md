# Cyber Star: Word Wars

This is a Cyber Punk theme games with hangman and space invader word mechanics.

## How to Play

Run the game from your terminal:

```bash
python3 Cyber_Star.py
```

Guess one letter at a time to reveal the hidden word before your fleets are destroyed.

## Controls

| Input      | Action               |
| ---------- | -------------------- |
| Any letter | Guess a letter       |
| `9`        | Call a Reinforcement |
| `0`        | Quit the game        |

## Fleet System

You have three fleets standing between the enemy and Earth:

1. **Outer Fleet** — first line of defense
2. **Inner Fleet** — engaged if the Outer Fleet falls
3. **Earth Defense Fleet** — last stand; if this falls, Earth is lost

Each wrong guess destroys a starship. Lose all ships in a fleet and the enemy advances to the next one. Guess the word before all three fleets are wiped out.

## Reinforcements

Each fleet comes with **1 reinforcement** that restores one destroyed starship. It does not carry over to the next fleet — use it or lose it.

## Requirements

- Python 3.10+
- `CyberStar_words.csv` must be in the same folder as `Cyber_Star.py`

## Files

| File                  | Description                |
| --------------------- | -------------------------- |
| `Cyber_Star.py`       | Main game file             |
| `CyberStar_words.csv` | Word list used by the game |

## future improvments

1. I would like to pull the words from a external source somewhere on the internet so it could be randomly used. This would ensure no player knows the word before hand.

2. I would like to implement some ASCII art in the future to make the aesthetics look more appealing. Will try and use this online resource: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
