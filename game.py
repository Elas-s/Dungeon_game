import random
import messages
import scores
import monsters


#-----------------------------------------------------


#prints a random message with monster's name
def say (message_list,monster):
    text = random.choice(message_list)
    print(text.replace("{monster}",monster["name"]))

#fighting the monster
def fight (inventory,monster):
    damage_taken = random.randint(monster["min_damage"],monster["max_damage"])
    loot = random.randint(monster["min_loot"],monster["max_loot"])
    say(messages.FIGHT_MESSAGES,monster)

    if "shield" in inventory:
        damage_taken -= 5
        print("You are taking less damage because of your shield. \n")

    print("The", monster["name"], "hits you for", damage_taken, "damage, but you find", loot, "gold. \n")

    if random.randint(1, 3) == 1:
        inventory.append("potion")
        say(messages.POTION_FOUND_MESSAGES,monster)

    return damage_taken, loot


#asking questions and getting desired answers
def ask(question , options):
    answer = input(question).lower()
    while answer not in options:
        print(random.choice(messages.INVALID_MESSAGES))
        answer = input(question).lower()
    return answer

#showing stats of player
def show_stats(health, gold, inventory):
    if health < 0 :
        health = 0

    print("❤️ Health:", health, "| 💰 Gold:", gold, "| 🎒 Inventory:", inventory, "\n")


#-------------------------------------------------------

#-----------Welcome player-------------

print ("Welcome to the dungeon! \n")
name = input ("What is your name, brave (or foolish) adventurer?   ")
health = 100
gold = 0
inventory = []
print("Good luck,", name + ". You're going to need it. Like, a LOT of it.\n")
show_stats(health, gold, inventory)

#-----------Entrance-------------


print("\n --- ENTRANCE---")
print("You stand before three doors. One smells funky. You don't know which one.\n")

choice = ask("Do you wish to go LEFT, RIGHT or STRAIGHT?    ", ["left", "right", "straight"])
if choice == "left":
    print("A goblin jumps out and slaps you with a half eaten fish! -20 health \n")
    health -= 20
elif choice == "right":
    print("A treasure chest! Inside: 50 gold and a potion. Today is your day! ✨ \n")
    gold = gold + 50
    inventory.append("potion")
elif choice == "straight":
    print("You find a sword and a shield! You feel like you won in life. +20 health ⚔️ \n")
    health += 20
    inventory.append("sword")
    inventory.append("shield")

show_stats(health, gold, inventory)

#----------------Rooms-----------

print ("You keep going and find only one door, you open it and find yourself in a room. \n")
room = 1
while health > 0 and room <= 5:
    print("\n --- Room", room, "---")

    monster = random.choice(monsters.MONSTERS)
    print(monster["intro"])

    action = input("Do you FIGHT the " + monster["name"] + " or SNEAK?    ").lower()

    if action == "fight":
        print("You have", inventory.count("potion"), "potions")

        if "potion" in inventory:
            drink = ask("Drink a potion before the fight? (yes/no)   ", ["yes", "no"])
            if drink == "yes":
                inventory.remove("potion")
                health += 30
                print("Glug glug glug... You feel AMAZING! +30 health 💪")
            elif drink == "no":
                print("Saving it for later? Bold strategy. Let's see if it pays off.")

        else:
            say(messages.NO_POTION_MESSAGES,monster)

        damage_taken, loot = fight(inventory,monster)
        health -= damage_taken
        gold += loot

    elif action == "sneak":
        result = random.randint(1,3)
        if result == 1:
            say(messages.SNEAK_SAFE_MESSAGES,monster)
        elif result == 2:
            say(messages.SNEAK_NOISE_MESSAGES, monster)
            print("-5 health from pure stress.")
            health -= 5
        elif result == 3:
            say(messages.SNEAK_CAUGHT_MESSAGES,monster)

            damage_taken, loot = fight(inventory,monster)
            health -= damage_taken
            gold += loot

    else:
        say(messages.HESITATE_MESSAGES, monster)
        print("-15 health")
        health -= 15

    show_stats(health, gold, inventory)
    room += 1


#------Game Over-----

print()
if health > 0:
    print("🏆 You escaped the dungeon with", gold, "gold!", name, "is a legend! (Your shoes are ruined though.)")
else:
    print("💀 You have fallen... The monsters are using your gold to buy snacks. GAME OVER.")

scores.save_score(name,gold,health > 0)
scores.show_top_scores()
print("Games played so far : ", scores.total_games())
print("Average gold in all games :", round(scores.average_gold(),1))