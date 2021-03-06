import random

#Hero and villain stats.
hercules_stats = {
    "Hit Points": 30,
    "Attack": 11,
    "Action": ["Punch", "Kick", "Bite", "Headbutt"]
}

lion_stats = {
    "Hit Points": 41,
    "Attack": 8,
    "Action": ["Bite", "Scratch"]
}

hydra_stats = {
    "Hit Points": 59,
    "Attack": 16,
    "Action": ["Bite", "Scratch", "Poison Breath"]
}

cerberus_stats = {
    "Hit Points": 75,
    "Attack": 13,
    "Action": ["Bite", "Scratch", "Fire Breath"]
}

# # Story narrative sections
# def intro():
#     print("""
# Hercules has been tasked by the great King Eurystheus to slay the Nemean Lion, defeat the nine-headed Lernaean Hydra, and
# capture the guard dog of the Underworld -- Cerberus. Hercules sets off to find these foes. He knows he can count on the 
# hydra wandering the caves that lead to the gates of the Underworld. The lion is known to wander the plains surrounding the
# cave. Hercules sets off with great determination and confidence.
# """)

# def the_plains():
#     print("""
# Hercules wanders the plains for many hours, but has no luck locating the Nemean Lion. His throat is parched, so he stops by
# a stream of water near an old olive tree. After he drinks his fill of water, he notices a low, rumbling snore coming from the
# tree. He goes to investigate and --what luck!-- the old lion is sleeping in the shade defenseless. Or so he thought...
# The beast opens one eye and stares directly at his next meal. Considering the monstrous things this lion has done, 
# Hercules can offer no quarter. Time to fight or die!
# """)

# def the_cave():
#     print("""
# Hercules arrives to the cave entrance to the Underworld, but there is a fork not far inside. He did not remember 
# there being a fork the last time he came this way. He does not know which direction would lead him to Cerberus or the
# hydra...
# """)

# # Asks user which path to take.
# def right_or_left():
#     make_a_decision = False
#     while make_a_decision is False:
#         choice = input("Should Hercules go right or left? ")
#         if choice == "right" or choice == "Right":
#             make_a_decision = True
#             return True
#         elif choice == "left" or choice == "Left":
#             make_a_decision = True
#             return False
#         elif choice != "left" or choice != "Left" or choice != "right" or choice != "Right":
#             print("Invalid entry. Try again.")
#             continue


# # Determines who will attack first.
# def initiative():
#     random_initiative = random.randrange(1, 20)
#     if random_initiative >= 6:
#         return True
#     else:
#         return False


# def attack():
#     herc_attack = True
#     if first_blood is True:
#         while herc_attack is True:
            # Still trying to work out mechanics of how attacking works back and forth


def hercules_attack_options():
    for option in hercules_stats["Action"]:
        print(option)
    action_attack = input("Choose Hercules' attack: ")
    herc_attack = True
    while herc_attack is True:
        if action_attack == "Punch":
            attack_results = hercules_stats["Attack"] * 1.3
            return attack_results
        elif action_attack == "Kick":
            attack_results = hercules_stats["Attack"] * 1.7
            return attack_results
        elif action_attack == "Bite":
            attack_results = hercules_stats["Attack"] * 1.2
            return attack_results
        elif action_attack == "Headbutt":
            attack_results = hercules_stats["Attack"] * 1.5
            return attack_results

hercules_attack_power = hercules_attack_options()
print(hercules_attack_power)
# # Rough draft order of rungame function. 
# def RunGame():
#     intro()
#     the_plains()
#     initiative()
#     attack()




# first_blood = initiative()