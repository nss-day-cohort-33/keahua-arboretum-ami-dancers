from animals import RiverDolphin
from animals import Opeapea
from animals import Pueo
from animals import Gecko
from animals import Ulae
from animals import Goose
from animals import Kikakapu
from animals import Spider

def feed_animal(arboretum):

    print("1. River Dolphin")
    print("2. Opeapea")
    print("3. Pueo")
    print("4. Gold Dust Day Gecko")
    print("5. Ulae")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Hawaiian Happy Face Spider")

    choice = input("Choose species to feed > ")


    if choice == "1":
        show_species("River dolphin")
    if choice == "2":
        show_species("Opeapea")
    if choice == "3":
        show_species("Pueo")
    if choice == "4":
        show_species("Gold Dust Day Gecko")
    if choice == "5":
        show_species("'Ulae")
    if choice == "6":
        show_species("Nene Goose")
    if choice == "7":
        show_species("Kikakapu")
    if choice == "8":
        show_species("Hawaiian Happy Face Spider")

def show_species(arboretum, species):
    species_list = []
    for animal in arboretum.contains_animals:
        if animal.species is species:
            species_list.append[animal]
    for index, animal in enumerate(species_list):
        if len(species_list) > 0:
            print(f'{index+1} {animal.species} ({animal.id})')
        else:
            print(f'There are no {animal.species} in {arboretum.name}. Please pick a different species to feed.')
            # feed_animal(keahua)







