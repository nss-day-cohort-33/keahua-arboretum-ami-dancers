def build_facility_report(arboretum):
    for river in arboretum.rivers:
        id = str(river.id)[0:8]
        print(f'\nRiver [{id}]')
        for animal in river.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in river.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    for coastline in arboretum.coastlines:
        id = str(coastline.id)[0:8]
        print(f'\nCoastline [{id}]')
        for animal in coastline.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in coastline.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    for swamp in arboretum.swamps:
        id = str(swamp.id)[0:8]
        print(f'\nSwamp [{id}]')
        for animal in swamp.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in swamp.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    for mountain in arboretum.mountains:
        id = str(mountain.id)[0:8]
        print(f'\nMountain [{id}]')
        for animal in mountain.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in mountain.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    for forest in arboretum.forests:
        id = str(forest.id)[0:8]
        print(f'\nForest [{id}]')
        for animal in forest.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in forest.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    for grassland in arboretum.grasslands:
        id = str(grassland.id)[0:8]
        print(f'\nGrassland [{id}]')
        for animal in grassland.contains_animals:
            id = str(animal.id)[0:8]
            print(f'{animal.species} ({id})')
        for plant in grassland.contains_plants:
            id = str(plant.id)[0:8]
            print(f'{plant.species} ({id})')

    input("\n\nPress any key to continue...")

