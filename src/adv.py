from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def main():
    user_input = ""
    player_name = input("Enter player name: ")
    player = Player(player_name, room["outside"])
    while True:
        user_input = input().split()
        if len(user_input) == 1:
            if user_input[0] == "q":
                break
            elif user_input[0] == "n":
                if player.current_room.n_to is not None:
                    player.current_room = player.current_room.n_to
                    print(f"Moved to {player.current_room.name}. {player.current_room.description}")
                else:
                    print("Cannot move north.")
            elif user_input[0] == "s":
                if player.current_room.s_to is not None:
                    player.current_room = player.current_room.s_to
                    print(f"Moved to {player.current_room.name}. {player.current_room.description}")
                else:
                    print("Cannot move south.")
            elif user_input[0] == "e":
                if player.current_room.e_to is not None:
                    player.current_room = player.current_room.e_to
                    print(f"Moved to {player.current_room.name}. {player.current_room.description}")
                else:
                    print("Cannot move east.")
            elif user_input[0] == "w":
                if player.current_room.w_to is not None:
                    player.current_room = player.current_room.w_to
                    print(f"Moved to {player.current_room.name}. {player.current_room.description}")
                else:
                    print("Cannot move west.")
            elif user_input[0] == "i" or user_input[0] == "inventory":
                if len(player.inventory) == 0:
                    print("You have nothing in your inventory.")
                elif len(player.inventory) == 1:
                    print(f"Your inventory contains the following: {player.inventory[0].name}.")
                elif len(player.inventory) == 2:
                    print(f"Your inventory contains the following: {player.inventory[0].name} and {player.inventory[1].name}.")
                else:
                    inventory_separator = ", "
                    print(f"Your inventory contains the following: {inventory_separator.join([player.inventory[i].name for i in range(len(player.inventory) - 1)])}, and {player.inventory[-1].name}.")
            elif user_input[0] == 'look':
                if len(player.current_room.items) == 0:
                    print(f"{player.current_room.name} is empty.")
                elif len(player.current_room.items) == 1:
                    print(f"{player.current_room.name} contains the following: {player.current_room.items[0].name}.")
                elif len(player.current_room.items) == 2:
                    print(f"{player.current_room.name} contains the following: {player.current_room.items[0].name} and {player.current_room.items[1].name}.")
                else:
                    inventory_separator = ", "
                    print(f"{player.current_room} contains the following: {inventory_separator.join([player.current_room.items[i].name for i in range(len(player.current_room.items) - 1)])}, and {player.current_room.items[-1].name}.")
        elif len(user_input) == 2:
            if user_input[0] == "get" or user_input[0] == "take":
                taken_item = None
                for i in range(len(player.current_room.items)):
                    if player.current_room.items[i].name == user_input[1]:
                        taken_item = player.current_room.items.pop(i)
                        break
                if taken_item is not None:
                    taken_item.on_take()
                    player.inventory.append(taken_item)
                else:
                    print(f"There is no {user_input[1]} in {player.current_room.name}.")
            if user_input[0] == "drop":
                dropped_item = None
                for i in range(len(player.inventory)):
                    if player.inventory[i].name == user_input[1]:
                        dropped_item = player.inventory.pop(i)
                        break
                if dropped_item is not None:
                    dropped_item.on_drop()
                    player.current_room.items.append(dropped_item)
                else:
                    print(f"There is no {user_input[1]} in your inventory.")




if __name__ == "__main__":
    main()
