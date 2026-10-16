from player import Player

def test_new_player_has_100_health():
    hero = Player("Chayma")
    assert hero.health == 100

def test_new_player_starts_with_no_gold():
    hero = Player("Chayma")
    assert hero.gold == 0

def test_take_damage_never_goes_below_zero():
    hero = Player("Chayma")
    hero.take_damage(300)
    assert hero.health == 0

def test_add_gold():
    hero = Player("Chayma")
    hero.add_gold(25)
    assert hero.gold == 25

def test_add_item():
    hero = Player("Chayma")
    hero.add_item("sword")
    assert hero.inventory == ["sword"]

def test_heal_adds_health():
    hero = Player("Chayma")
    hero.heal(30)
    assert hero.health == 130

def test_is_alive_false_at_zero_health():
    hero = Player("Chayma")
    hero.take_damage(100)
    assert hero.is_alive() == False

def test_potion_count():
    hero = Player("Chayma")
    hero.add_item("sword")
    hero.add_item("potion")
    hero.add_item("potion")
    assert hero.potion_count() == 2

def test_drink_potion_with_no_potions():
    hero = Player("Chayma")
    assert hero.drink_potion() == False
    assert hero.health == 100

def test_drink_potion_heals_and_uses_it_up():
    hero = Player("Chayma")
    hero.take_damage(50)
    hero.add_item("potion")
    result = hero.drink_potion()
    assert result == True
    assert  hero.health == 80
    assert hero.potion_count() == 0





