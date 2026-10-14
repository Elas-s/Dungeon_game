import random
import messages
#-----------------------------------------------------

def fight (inventory):
    damage_taken = random.randint(5, 30)
    loot = random.randint(10, 40)
    print(random.choice(messages.FIGHT_MESSAGES))

    if "shield" in inventory:
        damage_taken -= 5
        print("You are taking less damage because of your shield")

    print("You lose", damage_taken, "health, but find", loot, "gold.")

    if random.randint(1, 3) == 1:
        inventory.append("potion")
        print(random.choice(messages.POTION_FOUND_MESSAGES))

    return damage_taken, loot

def ask(question , options):
    answer = input(question).lower()
    while answer not in options:
        print(random.choice(messages.INVALID_MESSAGES))
        answer = input(question).lower()
    return answer


def show_stats(health, gold, inventory):
    if health < 0 :
        health = 0

    print("❤️ Health:", health, "| 💰 Gold:", gold, "| 🎒 Inventory:", inventory)



print ("Welcome to the dungeon!")
name = input ("What is your name, brave (or foolish) adventurer?   ")
health = 100
gold = 0
inventory = []
print("Good luck,", name + ". You're going to need it. Like, a LOT of it.\n")
show_stats(health, gold, inventory)


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
else:
    print("You stand still, confused. A bat flies by and judges you silently. \n")

show_stats(health, gold, inventory)

print ("You keep going and find only one door, you open it and find yourself in a room. \n")
room = 1
while health > 0 and room <= 5:
    print("\n --- Room", room, "---")
    action = ask("A monster appears! FIGHT or SNEAK?    ", ["fight", "sneak"])

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
            print(random.choice(messages.NO_POTION_MESSAGES))

        damage_taken, loot = fight(inventory)
        health -= damage_taken
        gold += loot



    elif action == "sneak":
        result = random.randint(1,3)
        if result == 1:
            print(random.choice(messages.SNEAK_SAFE_MESSAGES))
        elif result == 2:
            print(random.choice(messages.SNEAK_NOISE_MESSAGES), "-5 health from pure stress.")
            health -= 5
        elif result == 3:
            print(random.choice(messages.SNEAK_CAUGHT_MESSAGES))

            damage_taken, loot = fight(inventory)
            health -= damage_taken
            gold += loot

    else:
        print(random.choice(messages.HESITATE_MESSAGES), "-15 health")
        health -= 15

    show_stats(health, gold, inventory)
    room += 1

print()
if health > 0:
    print("🏆 You escaped the dungeon with", gold, "gold!", name, "is a legend! (Your shoes are ruined though.)")
else:
    print("💀 You have fallen... The monsters are using your gold to buy snacks. GAME OVER.")