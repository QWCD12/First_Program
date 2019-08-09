import random

#assign your prompts to variables
character_prompt = "What is your character?"
character_confirm = "Quickly ready your weapon and prepare for battle."
prompt1 = "There are two orcs right behind you! Quick (a)ttack them with your weapon!"
prompt2 = "Orc boss on your left, he's too strong. (d)effend yourself from his attacks!"
prompt3 = "He's worn out, hit him with your (s)pecial attack."
player_death = "You are dead"
background_information = "You fought well young warrior!\n"
                         "My name is doug, me and my men stumbled upon this cave thinking these orcs might be hiding some treasure.\n"
                         "Instead of finding treasure we happened to find you unconsious held captive by orcs\n"
                         "As soon we got to you we woke you up so you could hopefully help us out in battle\n"
                         "You really helped us out back there\n"
                         "Say what do they call you?"

#assign characters to dictionaries
robot = {'weapon':"radiation laser", 'special_attack':"nuclear reaction"}
captain = {'weapon': "broad sword", 'special_attack':"Atack of the fallen"}
beast = {'weapon': "claws", 'special_attack':"rampage"}
characters = [robot, captain, beast]
character_list = "robot, captain, beast"
skill_cooldown = "You're skill is on a cooldown for 3 turns."

#player inputs character
def character_select():
    print (character_list)
    character_input = None
    while character_input != "robot" or character_input != "captain" or character_input !="beast" or character_input !="lover" or character_input !="op":
        character_input = raw_input(character_prompt + "\n")
        if character_input == "robot" or character_input == "captain" or character_input =="beast" or character_input =="lover" or character_input =="op":
            print(character_confirm)
            break
    return character_input
player_character = character_select()

#attack function
def attack():
    die_roll = random.randint(1, 21)
    print "Your attack did " + str(die_roll) + " damage."

#defend function
def deffend():
    die_roll = random.randint(1, 21)
    print "You blocked " + str(die_roll) + " damage from the enemy"

#character special attacks
def special_attack():
    if player_character == "robot":
        print "A nuclear weapon fires from your hands causing a massive explosion.\n"
    elif player_character == "captain":
        print "You're fallen troops come to aid you in you're battle.\n"
    elif player_character == "beast":
        print "You're vision turns red as you tear through your enemies.\n"
    #special attack cooldown
    def special_cooldown():
        print skill_cooldown
        turns = []
        for i in turns:
            # if number of turns is divisible by 3 after special attack
            # make special attack available

#First battle
def first_battle():
    def first_fight():
        player_input = raw_input(prompt1 + "\n")
        if player_input != "a":
            print(player_death)
        else:
            attack()
            print("Both orcs lay at your feet.")
    first_fight()

    def boss_encounter():
        player_input = raw_input(prompt2 +"\n")
        if player_input != "d":
            print(player_death)
        else:
            deffend()
    boss_encounter()

    def boss_fight():
        player_input = raw_input(prompt3 + "\n")
        if player_input != "s":
            print(player_death)
        else:
            special_attack()
    boss_fight()
    #first_battle()

#character introduction
def chracter_introductio():
print background_information
