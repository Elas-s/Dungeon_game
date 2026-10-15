import random
import messages
import scores
import monsters


#-----------------------------------------------------


#prints a random message with monster's name
def say(message_list, monster):
    text = random.choice(message_list)
    print(text.replace("{monster}", monster["name"]).strip())

#prints a title between two lines, like a chapter heading
def title(text):
    print()
    print("=" * 50)
    print(text.center(50))
    print("=" * 50)

#fighting the monster, one turn at a time
def fight(health, inventory, monster):
    monster_hp = monster["health"]
    loot = 0
    first_turn = True

    if "shield" in inventory:
        print("🛡️  You raise your shield. It will block 5 damage from every hit.")
    print()
    print(f"⚔️  FIGHT!  You ({health} HP)  vs  {monster['name']} ({monster_hp} HP)")
    print()

    while monster_hp > 0 and health > 0:
        if first_turn:
            move = "attack"
            first_turn = False
        else:
            print(f"🧪 Potions: {inventory.count('potion')}")
            can_run = health < 30 or monster_hp > 30
            if can_run:
                move = ask("ATTACK, drink a POTION, or RUN?  ", ["attack", "potion", "run"])
            else:
                move = ask("ATTACK or drink a POTION?  ", ["attack", "potion"])
            print()

        #player's turn
        if move == "attack":
            if "sword" in inventory:
                say(messages.SWORD_MESSAGES, monster)
                player_hit = random.randint(10, 15)
            else:
                say(messages.NO_SWORD_MESSAGES, monster)
                player_hit = random.randint(5, 10)
            monster_hp -= player_hit
            print(f"   🎯 You hit the {monster['name']} for {player_hit}!   ({monster['name']}: {max(monster_hp, 0)} HP left)")

        elif move == "potion":
            if "potion" in inventory:
                inventory.remove("potion")
                health += 30
                print(f"   🧪 Glug glug glug... +30 health!   (You: {health} HP)")
            else:
                say(messages.NO_POTION_MESSAGES, monster)
                print("   You wasted your turn looking for a potion you don't have.")

        elif move == "run":
            if random.randint(1, 2) == 1:
                say(messages.RUN_SUCCESS_MESSAGES, monster)
                return health, 0
            else:
                say(messages.RUN_FAIL_MESSAGES, monster)

        #monster's turn (only if it's still alive)
        if monster_hp > 0:
            monster_hit = random.randint(monster["min_damage"], monster["max_damage"])
            if "shield" in inventory:
                monster_hit = max(monster_hit - 5, 0)
            health -= monster_hit
            print(f"   💥 The {monster['name']} hits you for {monster_hit}!   (You: {max(health, 0)} HP left)")
        print()

    if monster_hp <= 0:
        loot = random.randint(monster["min_loot"], monster["max_loot"])
        print(f"🏆 The {monster['name']} is defeated! You loot {loot} gold.")

        if random.randint(1, 3) == 1:
            inventory.append("potion")
            say(messages.POTION_FOUND_MESSAGES, monster)
    else:
        print(f"💀 The {monster['name']} wins... You fought bravely. Not well, but bravely.")

    return health, loot


#asking questions and getting desired answers
def ask(question, options):
    answer = input(question).lower()
    while answer not in options:
        print(random.choice(messages.INVALID_MESSAGES).strip())
        answer = input(question).lower()
    return answer

#showing stats of player
def show_stats(health, gold, inventory):
    if health < 0:
        health = 0
    if inventory:
        items = ", ".join(inventory)
    else:
        items = "empty"
    print()
    print(f"❤️  Health: {health}   💰 Gold: {gold}   🎒 Inventory: {items}")
    print("-" * 50)


#-------------------------------------------------------

#-----------Welcome player-------------

title("🏰 WELCOME TO THE DUNGEON 🏰")
print()
name = input("What is your name, brave (or foolish) adventurer?  ")
health = 100
gold = 0
inventory = []
print(f"\nGood luck, {name}. You're going to need it. Like, a LOT of it.")
show_stats(health, gold, inventory)

#-----------Entrance-------------

title("🚪 THE ENTRANCE 🚪")
print("You stand before three doors. One smells funky. You don't know which one.\n")

choice = ask("Do you wish to go LEFT, RIGHT or STRAIGHT?  ", ["left", "right", "straight"])
print()
if choice == "left":
    print("A goblin jumps out and slaps you with a half eaten fish! -20 health")
    health -= 20
elif choice == "right":
    print("A treasure chest! Inside: 50 gold and a potion. Today is your day! ✨")
    gold = gold + 50
    inventory.append("potion")
elif choice == "straight":
    print("You find a sword and a shield! You feel like you won in life. +20 health ⚔️")
    health += 20
    inventory.append("sword")
    inventory.append("shield")

show_stats(health, gold, inventory)

#----------------Rooms-----------

print("\nYou keep going and find only one door. You open it and find yourself in a room...")
room = 1
while health > 0 and room <= 5:
    title(f"ROOM {room} of 5")

    monster = random.choice(monsters.MONSTERS)
    print(monster["intro"])
    print()

    action = input(f"Do you FIGHT the {monster['name']}, SNEAK, or RUN?  ").lower()
    print()

    if action == "fight":
        if "potion" in inventory:
            print(f"🧪 You have {inventory.count('potion')} potion(s) in your inventory.")
            answer = ask("Do you wish to drink a potion before the fight? (yes/no)  ", ["yes", "no"])
            if answer == "yes":
                print("🧪 You drink a potion and feel stronger, grrr!! +30 health 💪")
                inventory.remove("potion")
                health += 30
            else:
                print("Saving it for later? Bold strategy.")
        else:
            print("🧪 You don't have any potions.")
            say(messages.NO_POTION_MESSAGES, monster)

        health, loot = fight(health, inventory, monster)
        gold += loot

    elif action == "sneak":
        result = random.randint(1, 3)
        if result == 1:
            say(messages.SNEAK_SAFE_MESSAGES, monster)
        elif result == 2:
            say(messages.SNEAK_NOISE_MESSAGES, monster)
            print("-5 health from pure stress.")
            health -= 5
        elif result == 3:
            say(messages.SNEAK_CAUGHT_MESSAGES, monster)

            health, loot = fight(health, inventory, monster)
            gold += loot

    elif action == "run":
        if random.randint(1, 2) == 1:
            say(messages.RUN_SUCCESS_MESSAGES, monster)
        else:
            say(messages.RUN_FAIL_MESSAGES, monster)
            health, loot = fight(health, inventory, monster)
            gold += loot

    else:
        say(messages.HESITATE_MESSAGES, monster)
        print("-15 health")
        health -= 15

    show_stats(health, gold, inventory)
    room += 1


#------Game Over-----

if health > 0:
    title("🏆 YOU ESCAPED! 🏆")
    print(f"You escaped the dungeon with {gold} gold! {name} is a legend! (Your shoes are ruined though.)")
else:
    title("💀 GAME OVER 💀")
    print("You have fallen... The monsters are using your gold to buy snacks.")

scores.save_score(name, gold, health > 0)
scores.show_top_scores()
print()
print(f"🎮 Games played so far: {scores.total_games()}")
print(f"💰 Average gold in all games: {round(scores.average_gold(), 1)}")
