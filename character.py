import jsonFile

characters = {}

# Load a new character data.
def loadCharacter(characterName):
    characterData = jsonFile.jsonFileOpen("./characters/" + characterName + ".json")
    print("Loaded character Data.\n")
    return characterData

# Append character data to the characters dictionary.
def characterDictionaryAppend(characterName):
    characters.update({characterName: loadCharacter(characterName)})
    print("Added character to dictionary.\n")
    return characters[characterName]

# Get the values of the dictionary.
def characterGetAll():
    print("Getting all characters.")
    return characters.items()

# Get the character's abilities and their values.
def getAbilities(characterName):
    for ability in characterName["abilities"]:
        print(ability)