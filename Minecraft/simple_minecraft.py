from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Audio files
place_sound = Audio("Sound/Break.ogg", autoplay=False)
dig_sound = Audio("Sound/Dig.ogg", autoplay=False)
walk_sound = Audio("Sound/Walking.ogg", loop=True, autoplay=False)
background_music = Audio('Sound/theme.ogg', loop=True, autoplay=True, volume=0.5)  # Background music

# Sky for background
Sky()

# Create the terrain with boxes
boxes = []
for i in range(25):
    for j in range(25):
        box = Button(color=color.white, model='cube', position=(j, 0, i),
                     texture='Textures/grass_texture.png', parent=scene, origin_y=0.5)
        boxes.append(box)

# Track the player's previous position
previous_position = Vec3(0, 0, 0)

# Walking sound when the player moves
def update():
    global previous_position
    if player.position != previous_position:  # Check if the player moved
        if not walk_sound.playing:
            walk_sound.play()  # Play walking sound when moving
    else:
        if walk_sound.playing:
            walk_sound.stop()  # Stop walking sound when player stops

    previous_position = player.position  # Update previous position to current

# Input events
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                             texture='Textures/brick.png', parent=scene, origin_y=0.5)
                boxes.append(new)
                place_sound.play()
            if key == 'left mouse down':
                boxes.remove(box)
                dig_sound.play()
                destroy(box)
            if key == "q":
                application.quit()

# Player controller
player = FirstPersonController()

background_music.play()  # Play background music

# Run the game
app.run()
