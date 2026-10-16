import random
import messages
import scores
import monsters
#-----------------------------------------------------

from player import Player

#-----------------------------------------------------


#prints a random message with monster's name
def say(message_list, monster):
    text = random.choice(message_list)
    print(text.replace("{monster}", monster["name"]).strip())

#prints a title between two lines
def title(text):
    print()
    print("=" * 50)
    print(text.center(50))
    print("=" * 50)

#fighting the monster, one turn at a time
def fight(hero, monster):
    monster_hp = monster["health"]
    loot = 0
    first_turn = True

    if "shield" in hero.inventory:
        print("🛡️  You raise your shield. It will block 5 damage from every hit.")
    print()
    print(f"⚔️  FIGHT!  You ({hero.health} HP)  vs  {monster['name']} ({monster_hp} HP)")
    print()

    while monster_hp > 0 and hero.is_alive():
        if first_turn:
            move = "attack"
            first_turn = False
        else:
            print(f"🧪 Potions: {hero.potion_count()}")
            can_run = hero.health < 30 or monster_hp > 30
            if can_run:
                move = ask("ATTACK, drink a POTION, or RUN?  ", ["attack", "potion", "run"])
            else:
                move = ask("ATTACK or drink a POTION?  ", ["attack", "potion"])
            print()

        #player's turn
        if move == "attack":
            if "sword" in hero.inventory:
                say(messages.SWORD_MESSAGES, monster)
                player_hit = random.randint(10, 15)
            else:
                say(messages.NO_SWORD_MESSAGES, monster)
                player_hit = random.randint(5, 10)
            monster_hp -= player_hit
            print(f"   🎯 You hit the {monster['name']} for {player_hit}!   ({monster['name']}: {max(monster_hp, 0)} HP left)")

        elif move == "potion":
            if hero.drink_potion():
                print(f"   🧪 Glug glug glug... +30 health!   (You: {hero.health} HP)")
            else:
                say(messages.NO_POTION_MESSAGES, monster)
                print("   You wasted your turn looking for a potion you don't have.")

        elif move == "run":
            if random.randint(1, 2) == 1:
                say(messages.RUN_SUCCESS_MESSAGES, monster)
                return
            else:
                say(messages.RUN_FAIL_MESSAGES, monster)

        #monster's turn (only if it's still alive)
        if monster_hp > 0:
            monster_hit = random.randint(monster["min_damage"], monster["max_damage"])
            if "shield" in hero.inventory:
                monster_hit = max(monster_hit - 5, 0)
            hero.take_damage(monster_hit)
            print(f"   💥 The {monster['name']} hits you for {monster_hit}!   (You: {hero.health} HP left)")
        print()

    if monster_hp <= 0:
        loot = random.randint(monster["min_loot"], monster["max_loot"])
        print(f"🏆 The {monster['name']} is defeated! You loot {loot} gold.")
        hero.add_gold(loot)

        if random.randint(1, 3) == 1:
            hero.add_item("potion")
            say(messages.POTION_FOUND_MESSAGES, monster)
    else:
        print(f"💀 The {monster['name']} wins... You fought bravely. Not well, but bravely.")


#asking questions and getting desired answers
def ask(question, options):
    answer = input(question).lower()
    while answer not in options:
        print(random.choice(messages.INVALID_MESSAGES).strip())
        answer = input(question).lower()
    return answer


#-------------------------------------------------------

def main():
    # -----------Welcome player-------------
    title("🏰 WELCOME TO THE DUNGEON 🏰")
    print()
    name = input("What is your name, brave (or foolish) adventurer?  ")
    hero = Player(name)
    print(f"\nGood luck, {hero.name}. You're going to need it. Like, a LOT of it.")
    hero.show_stats()

    # -----------Entrance-------------

    title("🚪 THE ENTRANCE 🚪")
    print("You stand before three doors. One smells funky. You don't know which one.\n")

    choice = ask("Do you wish to go LEFT, RIGHT or STRAIGHT?  ", ["left", "right", "straight"])
    print()
    if choice == "left":
        print("A goblin jumps out and slaps you with a half eaten fish! -20 health")
        hero.take_damage(20)
    elif choice == "right":
        print("A treasure chest! Inside: 50 gold and a potion. Today is your day! ✨")
        hero.add_gold(50)
        hero.add_item("potion")
    elif choice == "straight":
        print("You find a sword and a shield! You feel like you won in life. +20 health ⚔️")
        hero.heal(20)
        hero.add_item("sword")
        hero.add_item("shield")

    hero.show_stats()

    # ----------------Rooms-----------

    print("\nYou keep going and find only one door. You open it and find yourself in a room...")
    room = 1
    while hero.is_alive() and room <= 5:
        title(f"ROOM {room} of 5")

        monster = random.choice(monsters.MONSTERS)
        print(monster["intro"])
        print()

        action = input(f"Do you FIGHT the {monster['name']}, SNEAK, or RUN?  ").lower()
        print()

        if action == "fight":
            if hero.potion_count() > 0:
                print(f"🧪 You have {hero.potion_count()} potion(s) in your inventory.")
                answer = ask("Do you wish to drink a potion before the fight? (yes/no)  ", ["yes", "no"])
                if answer == "yes":
                    hero.drink_potion()
                    print("🧪 You drink a potion and feel stronger, grrr!! +30 health 💪")
                else:
                    print("Saving it for later? Bold strategy.")
            else:
                print("🧪 You don't have any potions.")
                say(messages.NO_POTION_MESSAGES, monster)

            fight(hero, monster)

        elif action == "sneak":
            result = random.randint(1, 3)
            if result == 1:
                say(messages.SNEAK_SAFE_MESSAGES, monster)
            elif result == 2:
                say(messages.SNEAK_NOISE_MESSAGES, monster)
                print("-5 health from pure stress.")
                hero.take_damage(5)
            elif result == 3:
                say(messages.SNEAK_CAUGHT_MESSAGES, monster)
                fight(hero, monster)

        elif action == "run":
            if random.randint(1, 2) == 1:
                say(messages.RUN_SUCCESS_MESSAGES, monster)
            else:
                say(messages.RUN_FAIL_MESSAGES, monster)
                fight(hero, monster)

        else:
            say(messages.HESITATE_MESSAGES, monster)
            print("-15 health")
            hero.take_damage(15)

        hero.show_stats()
        room += 1

    # ------Game Over-----

    if hero.is_alive():
        title("🏆 YOU ESCAPED! 🏆")
        print(
            f"You escaped the dungeon with {hero.gold} gold! {hero.name} is a legend! (Your shoes are ruined though.)")
    else:
        title("💀 GAME OVER 💀")
        print("You have fallen... The monsters are using your gold to buy snacks.")

    scores.save_score(hero.name, hero.gold, hero.is_alive())
    scores.show_top_scores()
    print()
    print(f"🎮 Games played so far: {scores.total_games()}")
    print(f"💰 Average gold in all games: {round(scores.average_gold(), 1)}")

#-------------------------------------------------------

if __name__ == "__main__":
    main()