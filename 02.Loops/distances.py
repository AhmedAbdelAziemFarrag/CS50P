distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance_au in distances.values():
        print(f"{distance_au} AU is equal to {convert(distance_au)} m from Earth.")


def convert(distance_au):
    return distance_au * 19597870700

main()
