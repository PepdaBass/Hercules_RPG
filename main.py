import random

#Intro to the story
def intro():
    print("""
Hercules is bored on Earth and wishes to pull a prank on his uncle, Hades. He thinks it would be a clever joke to kidnap
Cerberus so there are none to guard the gate to the Underworld for a day. However, Cerberus does not like him and Hercules
knows that he will have to fight the devil dog to the point of submission to capture him.

Hercules arrives to the cave entrance to the Underworld, but there are two entrances. He did not remember there being two last
time he came this way. He cannot remember if it is the cave on the right or left that would lead him to Cerberus...
""")

# Determines which path to take.
def right_or_left():
    make_a_decision = False
    while make_a_decision is False:
        choice = input("Should Hercules go right or left? ")
        if choice == "right" or choice == "Right":
            make_a_decision = True
            return True
        elif choice == "left" or choice == "Left":
            make_a_decision = True
            return False
        elif choice != "left" or choice != "Left" or choice != "right" or choice != "Right":
            print("Invalid entry. Try again.")
            continue


# Determines who will attack first.
def initiative():
    random_initiative = random.randrange(1, 20)
    if random_initiative >= 6:
        return True
    else:
        return False


# def attack():

# def RunGame():

# #Hero and villain stats.
# hercules_stats = {
#     'Hit Points': 30,
#     'Attack': 11,
#     'Action': ['punch', 'kick', 'bite', 'headbutt']
# }

# lion_stats = {
#     'Hit Points': 41,
#     'Attack': 8,
#     'Action': ['bite', 'scratch']
# }

# hydra_stats = {
#     'Hit Points': 59,
#     'Attack': 16,
#     'Action': ['bite', 'scratch', 'poison breath']
# }

# cerberus_stats = {
#     'Hit Points': 75,
#     'Attack': 13,
#     'Action': ['bite', 'scratch', 'fire breath']
# }

