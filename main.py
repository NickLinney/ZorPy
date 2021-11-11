import character

# Game function.
def game():
    print("Game started.")
    new_character = character.characterDictionaryAppend("samplechar")

    print("Press Enter to view your abilities...")
    keyPress = input()
    
    for ability in new_character["abilities"]:
        print(ability)

# Main program.
game()