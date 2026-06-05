```python
import random
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# SETTINGS
# =========================

AUTHOR = "azod08"

# =========================
# FUNCTIONS
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def banner():
    print(Fore.RED + r"""
╔════════════════════════════════════╗
║         SNAKE WATER GUN           ║
║            By azod08              ║
╚════════════════════════════════════╝
""")

snake_art = r"""
 /^\/^\
_|__| O|
\/     /~
 \____|
"""

water_art = r"""
     _
  __| |__
 /  ___  \
|  /   \  |
 \_______/
"""

gun_art = r"""
   _______
  / _____ \
 | |     | |
 | |_____| |
  \_______/
      ||
      ||
"""

arts = {
    "snake": snake_art,
    "water": water_art,
    "gun": gun_art
}

taunts = [
    "Too easy 😏",
    "Nice move 🔥",
    "Try harder 😎",
    "Lucky round 😂",
    "Well played 👏"
]

def show_choice(choice):
    print(Fore.CYAN + arts[choice])

def get_winner(player, bot):
    if player == bot:
        return "draw"

    if (
        (player == "snake" and bot == "water") or
        (player == "water" and bot == "gun") or
        (player == "gun" and bot == "snake")
    ):
        return "player"

    return "bot"

# =========================
# MAIN GAME LOOP
# =========================

while True:

    clear()
    banner()

    slow_print(Fore.YELLOW + "Loading Game...", 0.03)
    time.sleep(1)

    player_score = 0
    bot_score = 0

    round_number = 1

    while round_number <= 5:

        clear()
        banner()

        print(Fore.GREEN + f"Round : {round_number}/5")
        print(Fore.YELLOW + f"You : {player_score} | Bot : {bot_score}")
        print()

        print("1. Snake 🐍")
        print("2. Water 💧")
        print("3. Gun   🔫")
        print()

        choice = input("Choose (1-3): ").strip()

        mapping = {
            "1": "snake",
            "2": "water",
            "3": "gun"
        }

        if choice not in mapping:
            print(Fore.RED + "\nInvalid Choice!")
            time.sleep(1.5)
            continue

        player = mapping[choice]
        bot = random.choice(["snake", "water", "gun"])

        clear()
        banner()

        print(Fore.GREEN + "YOUR CHOICE\n")
        show_choice(player)

        print(Fore.MAGENTA + "\nBOT CHOICE\n")
        show_choice(bot)

        result = get_winner(player, bot)

        print()

        if result == "player":
            print(Fore.GREEN + "🏆 YOU WIN THIS ROUND")
            player_score += 1

        elif result == "bot":
            print(Fore.RED + "💀 BOT WINS THIS ROUND")
            bot_score += 1

        else:
            print(Fore.YELLOW + "🤝 DRAW")

        print(Fore.CYAN + "\nBot Says: " + random.choice(taunts))

        round_number += 1

        input("\nPress Enter To Continue...")

    clear()
    banner()

    print(Fore.WHITE + "=" * 40)
    print(Fore.YELLOW + f"FINAL SCORE")
    print(Fore.GREEN + f"You : {player_score}")
    print(Fore.RED + f"Bot : {bot_score}")
    print(Fore.WHITE + "=" * 40)

    print()

    if player_score > bot_score:
        print(Fore.GREEN + "🏆 CONGRATULATIONS! YOU WON THE MATCH")

    elif bot_score > player_score:
        print(Fore.RED + "💀 BOT WON THE MATCH")

    else:
        print(Fore.YELLOW + "🤝 MATCH DRAW")

    print()

    again = input("Play Again? (y/n): ").lower()

    if again != "y":
        clear()
        print(Fore.RED + "\nThanks For Playing ❤️")
        print(Fore.RED + f"Author : {AUTHOR}\n")
        break
```
