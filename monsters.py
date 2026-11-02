
MONSTERS = [
    {"name": "Goblin","health": 20,
     "min_damage": 3, "max_damage": 6,
     "min_loot": 5, "max_loot": 20,
     "intro": "A goblin appears, holding a half-eaten sandwich. It looks annoyed you interrupted lunch.",
     "personality":"greedy, talks fast, obsessed with sandwiches",
     "wants": "at least 20 gold, or a really good sandwich recipe",
     "hint": "You notice sandwich crumbs everywhere. The goblin keeps glancing at your pockets and muttering something about gold.",
     "can_be_convinced": True},

    {
        "name": "Sleep-Deprived Wizard", "health": 20,
        "min_damage": 8, "max_damage": 13,
        "min_loot": 15, "max_loot": 40,
        "intro": "A wizard appears, holding three empty coffee cups. "
                 "\"I cast... wait, what was I doing?\"",
        "personality":"very tired and hallucinates, really need some sleep but is addicted to this potion that keeps him awake",
        "wants": "some good coffee, someone to sing a lullaby for him to sleep, or ideas for potions and wizard stuff",
        "hint": "Three empty coffee cups lie beside a book of potions. The wizard keeps yawning and mumbling about a spell he can't finish.",
        "can_be_convinced": True
    },

    {
        "name": "Skeleton","health": 24,
        "min_damage": 4, "max_damage": 8,
        "min_loot": 5, "max_loot": 20,
        "intro": "A skeleton rattles toward you. It looks like "
                 "it hasn't had a decent meal in 400 years.",
        "personality":"shivers and stutters when talking, is cold and hungry and wants to carry his eyeballs with him",
        "wants": "a jacket, some food or a safe place to keep his eyeballs in or if someone fixes them for him",
        "hint": "The skeleton is shivering despite having no skin. It keeps fumbling with its loose eyeballs and staring longingly at your supplies.",
        "can_be_convinced": True
    },

    {
        "name": "Zombie","health": 28,
        "min_damage": 5, "max_damage": 9,
        "min_loot": 5, "max_loot": 25,
        "intro": "A zombie drags itself out of the darkness. "
                 "It looks exhausted. Honestly, same.",
        "personality": "bored to death (literally), slow, groans between words and loves gossip",
        "wants": "juicy drama from the other rooms, a good joke, or a brain snack (a cauliflower also works)",
        "hint": "The zombie perks up whenever it overhears a conversation from another room. It seems strangely excited about something it calls 'the latest drama.'",
        "can_be_convinced": True
    },

    {
        "name": "Mimic", "health": 30,
        "min_damage": 2, "max_damage": 5,
        "min_loot": 30, "max_loot": 90,
        "intro": "A beautiful treasure chest sits in the corner. "
                 "It has teeth. Oh. OH NO.",
        "personality": "a hungry treasure chest that clacks its lid, pretends to be a normal chest and is offended when people call it furniture",
        "wants": "at least 15 shiny coins to eat, or someone to admit it is the most beautiful chest in the dungeon",
        "hint": "The treasure chest keeps opening its lid just enough to show off its shiny teeth. It seems offended when you look at the coins inside instead of admiring it.",
        "can_be_convinced": True
    },

    {"name": "Troll", "health": 30,
     "min_damage": 6, "max_damage": 9,
     "min_loot": 20, "max_loot": 40,
     "intro": "A troll blocks the way. It smells like old cheese and bad decisions. Yup, that's the funky smell from before!",
     "personality": "big and grumpy on the outside but secretly sweet, very insecure about how he smells",
     "wants": "a compliment that will make him more confident",
     "hint": "You notice three tiny perfume bottles beside the troll. All empty. He keeps sniffing his sleeve and looking rather embarrassed.",
     "can_be_convinced": True},

    {
        "name": "Werewolf", "health": 30,
        "min_damage": 7, "max_damage": 10,
        "min_loot": 15, "max_loot": 40,
        "intro": "A werewolf howls at the moon... "
                 "It's indoors. There is no moon.",
        "personality": "dramatic teenager energy, always hungry, howls when emotional and is embarrassed there is no moon",
        "wants": "a snack (a potion counts), someone to pretend the ceiling is the moon, or a belly rub",
        "hint": "The werewolf keeps looking up at the ceiling, whining about the missing moon. Its stomach growls loudly and looks like he is bored.",
        "can_be_convinced": True
    },

    {
        "name": "Vampire", "health": 30,
        "min_damage": 10, "max_damage": 15,
        "min_loot": 20, "max_loot": 50,
        "intro": "A vampire appears, cape flowing dramatically. "
                 "You can tell it practised that entrance.",
        "personality": "theatrical and elegant, calls everyone darling, lives for gossip and scandal",
        "wants": "scandalous drama from the other rooms, praise for its dramatic entrance, or a fashion compliment about its cape",
        "hint": "The vampire keeps adjusting its cape in a cracked mirror. It perks up at the sound of distant gossip and seems to be waiting for someone to notice its entrance.",
        "can_be_convinced": True
    },

    {
        "name": "Ogre", "health": 30,
        "min_damage": 10, "max_damage": 18,
        "min_loot": 15, "max_loot": 40,
        "intro": "An enormous ogre blocks your path. "
                 "It picks its teeth with what appears to be a sword.",
        "personality": "simple and polite, talks about himself in third person, always snacking",
        "wants": "food or a potion, or someone to help him get the sword out of his teeth",
        "hint": "The ogre is trying to dislodge a sword stuck between his teeth. A half-eaten snack sits on his chair, and he looks rather frustrated.",
        "can_be_convinced": True
    },

    {"name": "Dragon","health": 33,
     "min_damage": 12, "max_damage": 20,
     "min_loot": 50, "max_loot": 100,
     "intro": "A DRAGON?! Is this a joke ??! Who designed this dungeon?!",
     "personality": "proud and ancient hoarder, counts every coin twice, loves to be admired",
     "wants": "at least 50 gold for its hoard, or a very rare treasure, or someone to bow and admire its scales",
     "hint": "The dragon guards a mountain of gold, counting the coins repeatedly. It keeps spreading its wings whenever it catches you looking at its scales.",
     "can_be_convinced": True},

    {"name": "Karen","health": 35,
     "min_damage": 14, "max_damage": 22,
     "min_loot": 60, "max_loot": 120,
     "intro": "Oh crap a Karen.. A dragon would have been better",
     "personality": "rude and entitled, always wants to speak to the dungeon manager, complains about everything",
     "wants": "nothing, she just wants to complain and will never let anyone pass",
     "hint": "The woman is holding a complaint form, three more complaint forms, and a sign reading 'I DEMAND TO SPEAK TO THE MANAGER.' She doesn't appear interested in negotiation.",
     "can_be_convinced": False},

    {
        "name": "Demon","health": 40,
        "min_damage": 18, "max_damage": 30,
        "min_loot": 35, "max_loot": 80,
        "intro": "A demon crawls out of a portal in the floor. "
                 "It looks disappointed. Apparently, you were not worth the trip.",
        "personality": "bored and unimpressed, crossed nine circles of fire to get here and thinks you are a waste of its time",
        "wants": "nothing, it came here to fight and will never let anyone pass",
        "hint": "The demon's claws are already glowing with dark energy. It ignores your belongings and pleasantries, staring directly at you with a look that says it came here for one reason.",
        "can_be_convinced": False
    },

]
