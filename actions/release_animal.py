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

    print("\nplease enter the animal you want to release\n")
    print("1. River Dolphin")
    print("2. Opeapea")
    print("3. Peuo")
    print("4. Gold Dust Day Gecko")
    print("5. Ulae")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Hawaiian Happy Face Spider")
    print("9. back")

    choice1 = input("Choose animal to release > ")

    if choice1 == "1":
        animal = RiverDolphin()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "2":
        animal = Opeapea()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "3":
        animal = Pueo()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "4":
        animal = Gecko()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "5":
        animal = Ulae()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "6":
        animal = Goose()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "7":
        animal = Kikakapu()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "8":
        animal = Spider()
        release_into_enviroment(animal, arboretum)

    elif choice1 == "9":
        pass

    else:
        print("\nplease enter number listed\n\n")
        release_animal(arboretum)


def release_into_enviroment(animal, arboretum):

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
        if len(arboretum.rivers) == 0:
            print("\nthere are no rivers. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, river in enumerate(arboretum.rivers):
                print(f'{index + 1}. River {river.id}\n')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.rivers[int(choice) - 1].add_animal(animal)

    if choice2 == "2":
        if len(arboretum.swamps) == 0:
            print("\nthere are no swamps. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. Swamp {swamp.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.swamps[int(choice) - 1].add_animal(animal)
    if choice2 == "3":
        if len(arboretum.coastlines) == 0:
            print("\nthere are no coastlines. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. Coastline {coastline.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.coastlines[int(choice) - 1].add_animal(animal)
    if choice2 == "4":
        if len(arboretum.grasslands) == 0:
            print("\nthere are no grasslands. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland {grassland.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.grasslands[int(choice) - 1].add_animal(animal)
    if choice2 == "5":
        if len(arboretum.mountains) == 0:
            print("\nthere are no mountains. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, mountain in enumerate(arboretum.mountains):
                print(f'{index + 1}. Mountain {mountain.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.mountains[int(choice) - 1].add_animal(animal)
    if choice2 == "6":
        if len(arboretum.forests) == 0:
            print("\nthere are no forests. please select your animal and try again")
            release_animal(arboretum)
        else:
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest {forest.id}')
            print("Release the animal into which biome?")
            choice = input("> ")
            arboretum.forests[int(choice) - 1].add_animal(animal)
    if choice2 == "7":
        release_animal(arboretum)
        # main_menu()
    if choice2 != "7":
        pass