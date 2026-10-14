import random

# --- Funny message lists ---

FIGHT_MESSAGES = ["You and the monster slap-fight for 3 minutes. Nobody is proud of this.",
                  "You throw your shoe. Critical hit!",
                  "You swing wildly with your eyes closed. Somehow it works."]

SNEAK_SAFE_MESSAGES = ["You tiptoe past like a ninja. A very sweaty ninja, but still.",
                       "The monster is busy scrolling on its phone. You walk right past.",
                       "You hide behind a suspiciously small plant. It works?!"]

SNEAK_NOISE_MESSAGES = [
    "You crouch a little too low... Your pants split wide open. The monster didn't hear it, but you'll be finishing this dungeon with a breeze where no breeze should be.",
    "Your stomach growls louder than the monster. It looks confused but stays put.",
     "You turn off your flashlight. Congratulations. Now you're scared AND lost. You shivering so much the monster felt bad for you."
]


SNEAK_CAUGHT_MESSAGES = [
    "The monster heard you equip your weapon. Bro, this isn't a fashion show.",
    "You accidentally make eye contact with the monster. Awkward. Now what?",
    "You throw a bottle to distract the monster. It lands perfectly. You trip over the bottle."
]

HESITATE_MESSAGES = [
    "You stand there thinking about life. The monster bites you. Rude.",
    "That wasn't an option, genius. The monster bites you for being weird.",
    "You try to negotiate. The monster does not speak 'whatever that was'.",
]

NO_POTION_MESSAGES = [
    "Even the monster brought snacks. Just saying.",
    "You have no potions. The emergency supplies are you. Good luck, champ",
    "Not a single potion. The consequences are about to be hilarious.",
]

POTION_FOUND_MESSAGES = [
    "The monster drops a potion! It smells weird but whatever.",
    "You find a potion! Expiry date: 1347. Probably fine.",
    "A potion rolls out from under the monster. Gross, but useful.",
]

INVALID_MESSAGES = [
    "That's not an option. The monster is laughing at you.",
    "Are you typing with your elbows? Try again.",
    "Bro. Read the options.",
]

#-----------------------------------------------------

def fight (inventory):
    damage_taken = random.randint(5, 30)
    loot = random.randint(10, 40)
    print(random.choice(FIGHT_MESSAGES))

    if "shield" in inventory:
        damage_taken -= 5
        print("You are taking less damage because of your shield")

    print("You lose", damage_taken, "health, but find", loot, "gold.")

    if random.randint(1, 3) == 1:
        inventory.append("potion")
        print(random.choice(POTION_FOUND_MESSAGES))

    return damage_taken, loot

def ask(question , options):
    answer = input(question).lower()
    while answer not in options:
        print(random.choice(INVALID_MESSAGES))
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
            print(random.choice(NO_POTION_MESSAGES))

        damage_taken, loot = fight(inventory)
        health -= damage_taken
        gold += loot



    elif action == "sneak":
        result = random.randint(1,3)
        if result == 1:
            print(random.choice(SNEAK_SAFE_MESSAGES))
        elif result == 2:
            print(random.choice(SNEAK_NOISE_MESSAGES), "-5 health from pure stress.")
            health -= 5
        elif result == 3:
            print(random.choice(SNEAK_CAUGHT_MESSAGES))

            damage_taken, loot = fight(inventory)
            health -= damage_taken
            gold += loot

    else:
        print(random.choice(HESITATE_MESSAGES), "-15 health")
        health -= 15

    show_stats(health, gold, inventory)
    room += 1

print()
if health > 0:
    print("🏆 You escaped the dungeon with", gold, "gold!", name, "is a legend! (Your shoes are ruined though.)")
else:
    print("💀 You have fallen... The monsters are using your gold to buy snacks. GAME OVER.")