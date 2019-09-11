from animals import RiverDolphin
from animals import Opeapea
from animals import Pueo
from animals import Gecko
from animals import Ulae
from animals import Goose
from animals import Kikakapu
from animals import Spider

def feed_animal(arboretum):

    print("\n1. River Dolphin")
    print("2. Opeapea")
    print("3. Pueo")
    print("4. Gold Dust Day Gecko")
    print("5. Ulae")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Hawaiian Happy Face Spider")

    choice = input("\nChoose species to feed > ")


    if choice == "1":
        show_species(arboretum, "River dolphin")
    if choice == "2":
        show_species(arboretum, "Opeapea")
    if choice == "3":
        show_species(arboretum, "Pueo")
    if choice == "4":
        show_species(arboretum, "Gold Dust Day Gecko")
    if choice == "5":
        show_species(arboretum, "'Ulae")
    if choice == "6":
        show_species(arboretum, "Nene Goose")
    if choice == "7":
        show_species(arboretum, "Kikakapu")
    if choice == "8":
        show_species(arboretum, "Hawaiian Happy Face Spider")

def show_species(arboretum, species):
    species_list = []
    for river in arboretum.rivers:
        for animal in river.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    for mountain in arboretum.mountains:
        for animal in mountain.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    for grassland in arboretum.grasslands:
        for animal in grassland.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    for forest in arboretum.forests:
        for animal in forest.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    for swamp in arboretum.swamps:
        for animal in swamp.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    for coastline in arboretum.coastlines:
        for animal in coastline.contains_animals:
            if animal.species == species:
                species_list.append(animal)
    if len(species_list) == 0:
        print(f'There are no {animal.species} in {arboretum.name}. Please pick a different species to feed.\n')

    else:
        food_items = []
        for index, animal in enumerate(species_list):
            print(f'\n{index+1}. {animal.species} ({animal.id})')

        choice2 = input(f'\nChoose which {species} to feed >')

        if choice2 == choice2:
            for index, food in enumerate(animal.prey):
                print(f'\n{index+1}. {food}')
                food_items.append(food)

        choice3 = input(f"\nChoose what to feed the {animal.species} >    ")

        if choice3 == choice3:
            animal.feed(food_items[int(choice3)-1])









