from character import loadCharacter, characterDictionaryAppend, characterGetAll

# Game function.
def game():
    print("Game started.")
    loadCharacter("samplechar")
    new_character = characterDictionaryAppend("samplechar")

    print(new_character["name"])

    print("Press Enter to view your abilities...")
    keyPress = input()
    
    for ability in new_character["abilities"]:
        print(ability)

# Main program.
game()