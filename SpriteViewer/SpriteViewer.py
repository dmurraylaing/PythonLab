import os
from sprite import Sprite

# Support function definitions
def list_sprite_files(directory):
    """Get the list of sprite files from the current directory"""
    files = os.listdir(directory)

    sprite_files = []
    for file in files:
        if file.endswith(".sprite"):
           sprite_files.append(directory + "/" + file)

    return sprite_files

    #return [x for x in os.listdir(directory) if x.endswith(".sprite")]

def pick_sprite_file(filelist):
    """Function to show list to user and get them to pick one"""

    print("Select a sprite to draw from:")
    optionNumber = 0
    for file in filelist:
        print(str(optionNumber) + ": " + file)
        optionNumber = optionNumber+1

    selected = input("Enter number:")
    return filelist[int(selected)]

# Get the list of sprite files
sprite_files = list_sprite_files("Sprites")

# Display list to user and get them to pick one
selected_file = pick_sprite_file(sprite_files)

print("selected file " + selected_file)

# Create a sprite object to hold the data
sprite = Sprite()

# Load the sprite data
sprite.load_from_file(selected_file)

# Display the sprite
sprite.draw()
