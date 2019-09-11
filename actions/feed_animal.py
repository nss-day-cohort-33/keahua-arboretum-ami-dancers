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
    print("9. Back")

    choice = input("\nChoose species to feed > ")

    if choice == "1":
        show_species(arboretum, "River dolphin")
    elif choice == "2":
        show_species(arboretum, "Opeapea")
    elif choice == "3":
        show_species(arboretum, "Pueo")
    elif choice == "4":
        show_species(arboretum, "Gold Dust Day Gecko")
    elif choice == "5":
        show_species(arboretum, "'Ulae")
    elif choice == "6":
        show_species(arboretum, "Nene Goose")
    elif choice == "7":
        show_species(arboretum, "Kikakapu")
    elif choice == "8":
        show_species(arboretum, "Hawaiian Happy Face Spider")
    elif choice == "9":
        pass
    else:
        print('\nPlease select an animal species to feed\n')
        feed_animal(arboretum)


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
        print(f'\nThere are no {species}s in {arboretum.name}. Please pick a different species to feed.\n')
        feed_animal(arboretum)

    else:
        food_items = []
        true_index = []
        print("\n")
        for index, animal in enumerate(species_list):
            true_index.append(index+1)
            print(f'{index+1}. {animal.species} ({animal.id})')
        print(f'{index+2}. Go Back')



        choice2 = input(f'\nChoose which {species} to feed >')

        if int(choice2) <= len(true_index):
            print('\n')
            for index, food in enumerate(animal.prey):
                print(f'{index+1}. {food}')
                food_items.append(food)
                choice3 = input(f"\nChoose what to feed the {animal.species} >    ")
                if int(choice3) <= len(animal.prey):
                    animal.feed(food_items[int(choice3)-1])
                else:
                    print(f'That was not a valid food choice. Please choose what food to feed the {animal.species}.')
                    feed_animal(arboretum)
        elif int(choice2) == len(true_index)+1:
            feed_animal(arboretum)
        else:
            print(f"\nThat was not a valid choice. Try again.")
            show_species(arboretum, species)



        # choice3 = input(f"\nChoose what to feed the {animal.species} >    ")
        # if int(choice3) <= len(animal.prey):
        #     animal.feed(food_items[int(choice3)-1])
        # else:
        #     print(f'That was not a valid food choice. Please choose what food to feed the {animal.species}.')
        #     feed_animal(arboretum)









