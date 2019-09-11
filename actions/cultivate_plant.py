from plants.complete_plants import BlueJade
from plants.complete_plants import MountainApple
from plants.complete_plants import Rainbow
from plants.complete_plants import Silversword


def cultivate_plant(arboretum):
    plant = None

    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")

    choice1 = input("Choose plant to cultivate > ")

    if choice1 == "1":
        plant = BlueJade()

    if choice1 == "2":
        plant = MountainApple()

    if choice1 == "3":
        plant = Rainbow()

    if choice1 == "4":
        plant = Silversword()

    print("\n\nwhich Biome would you like to put the plant in? \n")
    print("1. Swamp")
    print("2. Grassland")
    print("3. Mountain")
    print("4. Forest")
    print("5. Back")

    choice2 = input("Choose your habitat > ")

    if choice2 == "1":
        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp ({len(swamp.contains_plants)} plants) {swamp.id}')
        print("Release the plant into which biome?")
        choice = input("> ")
        arboretum.swamps[int(choice) - 1].add_plant(plant)
    if choice2 == "2":
        for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland ({len(grassland.contains_plants)} plants) {grassland.id}')
        print("Release the plant into which biome?")
        choice = input("> ")
        arboretum.grasslands[int(choice) - 1].add_plant(plant)
    if choice2 == "3":
        for index, mountain in enumerate(arboretum.mountains):
            print(f'{index + 1}. Mountain ({len(mountain.contains_plants)} plants) {mountain.id}')
        print("Release the plant into which biome?")
        choice = input("> ")
        arboretum.mountains[int(choice) - 1].add_plant(plant)
    if choice2 == "4":
        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest ({len(forest.contains_plants)} plants) {forest.id}')
        print("Release the plant into which biome?")
        choice = input("> ")
        arboretum.forests[int(choice) - 1].add_plant(plant)
    if choice2 == "5":
        pass
