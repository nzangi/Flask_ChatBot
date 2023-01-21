opposite = {
    "NORTH": "SOUTH",
    "EAST": "WEST",
    "SOUTH": "NORTH",
    "WEST": "EAST"
}


# find the direction
def reduced_direction(directions):
    final_directions = []
    for distance in range(0, len(directions)):
        if final_directions:
            if final_directions[-1] == opposite[directions[distance]]:
                final_directions.pop()
            else:
                final_directions.append(directions[distance])
        else:
            final_directions.append(directions[distance])

    return final_directions


print(reduced_direction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH","WEST"]))
