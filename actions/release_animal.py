from animals import RiverDolphin
from animals import Opeapea
from animals import Pueo
from animals import Gecko
from animals import Ulae
from animals import Goose
from animals import Kikakapu
from animals import Spider



def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Opeapea")
    print("3. Peuo")
    print("4. Gold Dust Day Gecko")
    print("5. Ulae")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Hawaiian Happy Face Spider")

    choice1 = input("Choose animal to release > ")

    if choice1 == "1":
        animal = RiverDolphin()

    if choice1 == "2":
        animal = Opeapea()

    if choice1 == "3":
        animal = Pueo()

    if choice1 == "4":
        animal = Gecko()

    if choice1 == "5":
        animal = Ulae()

    if choice1 == "6":
        animal = Goose()

    if choice1 == "7":
        animal = Kikakapu()

    if choice1 == "8":
        animal = Spider()

    print("\n\nwhich Biome would you like to put the animal in? \n")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    print("7. Back")

    choice2 = input("Choose your habitat > ")

    if choice2 == "1":
        for index, river in enumerate(arboretum.rivers):
            print(f'{index + 1}. River {river.id}\n\n')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.rivers[int(choice) - 1].add_animal(animal)
    if choice2 == "2":
        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp {swamp.id}')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.swamps[int(choice) - 1].add_animal(animal)
    if choice2 == "3":
        for index, coastline in enumerate(arboretum.coastlines):
            print(f'{index + 1}. Coastline {coastline.id}')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.coastlines[int(choice) - 1].add_animal(animal)
    if choice2 == "4":
        for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland {grassland.id}')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.grasslands[int(choice) - 1].add_animal(animal)
    if choice2 == "5":
        for index, mountain in enumerate(arboretum.mountains):
            print(f'{index + 1}. Mountain {mountain.id}')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.mountains[int(choice) - 1].add_animal(animal)
    if choice2 == "6":
        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {forest.id}')
        print("Release the animal into which biome?")
        choice = input("> ")
        arboretum.forests[int(choice) - 1].add_animal(animal)
    if choice2 == "7":
        pass
        # main_menu()
    if choice2 != "7":
        pass
 