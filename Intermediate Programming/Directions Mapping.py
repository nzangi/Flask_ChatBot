opposite_directions = {
    "NORTH": "SOUTH",
    "EAST": "WEST",
    "SOUTH": "NORTH",
    "WEST": "EAST"
}


def directions(get_directions):
    final_directions = []
    for distance in range(0, len(get_directions)):
        if final_directions:
            if final_directions[-1] == opposite_directions[get_directions[distance]]:
                final_directions.pop()
            else:
                final_directions.append(get_directions[distance])
        else:
            final_directions.append(get_directions[distance])

    final_directions = "".join(final_directions)

    return final_directions


print(directions(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
