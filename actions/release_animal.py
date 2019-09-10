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

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        animal = Opeapea()

    if choice == "3":
        animal = Pueo()

    if choice == "4":
        animal = Gecko()

    if choice == "5":
        animal = Ulae()

    if choice == "6":
        animal = Goose()

    if choice == "7":
        animal = Kikakapu()

    if choice == "8":
        animal = Spider()

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)


