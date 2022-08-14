import character

# Game function.
def game():
    print("Game started.")
    newCharacter = character.characterDictionaryAppend("samplechar")

    print("Press Enter to view your abilities...")
    keyPress = input()
    
    character.getAbilities(newCharacter)


# Main program.
game()