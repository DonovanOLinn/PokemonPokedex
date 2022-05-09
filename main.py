import pip._vendor.requests as r
import pprint
pp = pprint.PrettyPrinter(depth=4)
    
    
#offset API might be good to look up to help with efficiency of API calls

class Pokedex:
    #This is the init
    def __init__(self, revealed_pokemon=[]):
        self.revealed_pokemon = revealed_pokemon
           
    #This is the function that searches for all types of a specific pokemon
    def type_Pokemon(self):
        my_type = input("What type of pokemon would you like to look for?: An example would be 'grass'\nYou can also type 'quit' to quit ")
        if my_type == 'quit':
            my_pokedex.Screen()
        #my_region = input("And is there a region you want to search in? If not, type 'no': ")
        my_pokemon = r.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=898')        
        if my_pokemon.status_code == 200:
            my_pokemon = my_pokemon.json()
        for pokemon in range(len(my_pokemon['results'])):
            x = my_pokemon['results'][pokemon]['name']
            y = my_pokemon['results'][pokemon]['url']
            this_pokemon = r.get(y)
            if this_pokemon.status_code == 200:
                this_pokemon = this_pokemon.json()
                if this_pokemon['types'][0]['type']['name'] == my_type:
                    print(x)
        print(f"This is a list of all the {my_type} type Pokemon")
        my_pokedex.search_Pokemon()

        
    #This is what searches for a pokemon and adds it to your revealed Pokemon
    def search_Pokemon(self):
        while True:
            find = input('What pokemon would you like to add?\n').lower()
            name = find
            data = r.get(f'https://pokeapi.co/api/v2/pokemon/{find}')
            if data.status_code == 200:
                data = data.json()
            else:
                print(data.status_code)
                print("ERROR ERROR ERROR, much like Lugia, the pokemon you entered does not exist. Check your spelling and try again")
                continue
            self.revealed_pokemon.append(Pokemon(data))
            #self.revealed_pokemon
            another = input(f"Wonderful! {name} has been added. Would you like to add another? Type y/n\n")
            if another == 'y':
                continue
            elif another == 'n':
                break     
            else:
                print("Sorry we don't recognize that command. We will put you back in the main search screen.")
                continue
        my_pokedex.Screen()
            
            
    def create(self):
        my_name = input("What would you like to name this Pokemon? ")
        my_base_experience = input(f"How much experience does {my_name} have? ")
        my_weight = input(f"What is {my_name}s weight in pounds? ")
        my_height = input(f"What is {my_name}s height in inches? ")
        my_id = input(f"What is {my_name}s ID number? ")
        my_types = input(f"What type is {my_name}? ")
        my_abilities = []
        while True:
            ind_abilities = input(f"What abilities does {my_name} have?\n Type 'done' when you're ready to headback\n ")
            if ind_abilities == 'done':
                break
            my_abilities.append(ind_abilities)        
        my_pokemon = MyPokemon(my_name, my_types, my_height, my_weight, my_base_experience, my_id, my_abilities)
        self.revealed_pokemon.append(my_pokemon)
        my_pokedex.Screen()
            
        
    def display_Pokemon(self):
        if self.revealed_pokemon == []:
            print("Looks like you haven't added any Pokemon yet. Why don't you do that first!")
            my_pokedex.search_Pokemon()
        for poke in self.revealed_pokemon:
            print(poke.name)
        stats = input("To inspect your Pokemon, type 'inspect'\nYou can also sort by type if you type 'sort'\nIf not, type 'quit'\n")
        if stats == 'quit':
            my_pokedex.Screen()
        elif stats == 'inspect':
            print("In inspect")
            choose = input("Which pokemon do you want to inspect? Just type their name: \n")
            for poke in self.revealed_pokemon:
                if choose == poke.name:
                    print(f"{poke.name} is the name of your Pokemon")
                    print(f"{poke.name} is a {poke.types} type ")
                    print(f" Your {poke.name} is {poke.height} inches ")
                    print(f" Your {poke.name} weighs {poke.weight}lbs")
                    print(f" When you got your {poke.name} it had {poke.base_experience} experience")
                    print(f" This is your {poke.name} identity tag: {poke.ident}")
                    print(f" Your {poke.name} has these abilities: {poke.abilities}")
                    done = input("Type done when done ")
                    if done == 'done':
                        my_pokedex.display_Pokemon()
        elif stats == 'sort':
            sorting_dictionary = {}
            sorting_list = []
            for poke in self.revealed_pokemon:
                if poke.types not in sorting_dictionary:
                    sorting_dictionary[poke.types] = []
                if poke.types in sorting_dictionary:
                    sorting_dictionary[poke.types].append(poke.name)


            pp.pprint(sorting_dictionary)
            exit = input("When done, type 'back' to go back\n")
            if exit == 'back':
                my_pokedex.display_Pokemon()
            
                    
    def Screen(self):
        print("Hello! Welcome to your pokedex. I am your UI. What would you like to do?")
        direction = input("Type 'search' to find pokemon to add\nType 'display' to show your pokemon\nType 'create' to make your own\nType 'type' to search by type of Pokemon\nType 'region' to search by region\nType 'quit' to exit. \n")
        if direction == 'search':
            my_pokedex.search_Pokemon()
        elif direction == 'display':
            my_pokedex.display_Pokemon()
        elif direction == 'create':
            my_pokedex.create()
        elif direction == 'quit':
            pass
        elif direction == 'type':
            my_pokedex.type_Pokemon()
        elif direction == 'region':
            my_pokedex.Region()
        else:
            print("Sorry, we don't recoginize that command. How about we try this again?")
            my_pokedex.Screen()
   

    def edgecase_grabs(self):
        for poke in self.bad_pokemon:
            alt_poke_grab = r.get(f'https://pokeapi.co/api/v2/pokemon/{poke}/')
            if alt_poke_grab.status_code == 200:
                alt_poke_grab = alt_poke_grab.json()
            self.revealed_pokemon.append(Pokemon(alt_poke_grab))
        pass

    def Region(self):
        self.bad_pokemon = []
        region_input = input("So you want to add by region huh? Your choices are: \nkanto\njohto\nhoenn\nsinnoh\nunova\nkalos\nalola\ngalar\n")
        top_layer = r.get('https://pokeapi.co/api/v2/generation/')
        if top_layer.status_code == 200:
            top_layer = top_layer.json()
        for layer1 in range(len(top_layer['results'])):
            middle_layer = r.get(top_layer['results'][layer1]['url'])
            if middle_layer.status_code == 200:
                middle_layer = middle_layer.json()

            if middle_layer['main_region']['name'] == region_input:    
                for layer2 in range(len(middle_layer['pokemon_species'])):
                    try:
                        bottom_layer = middle_layer['pokemon_species'][layer2]['name']
                        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{bottom_layer}')
                        if data.status_code == 200:
                            data = data.json()
                        self.revealed_pokemon.append(Pokemon(data))
                        print(f'{Pokemon(data).name} is here!')
                    except TypeError:
                        url_bottom_layer = middle_layer['pokemon_species'][layer2]['url']
                        id_layer = r.get(url_bottom_layer)
                        if id_layer.status_code == 200:
                            id_layer = id_layer.json()
                        find_id = id_layer['id']
                        self.bad_pokemon.append(find_id)
                        continue
        if self.bad_pokemon != []:
            my_pokedex.edgecase_grabs()

        print(f'You have grabbed all of the {region_input} region pokemon!')
        my_pokedex.Screen()



class Pokemon:
    def __init__(self, data,):
        self.name = data['name']
        self.types = data['types'][0]['type']['name']
        self.height = data['height']
        self.weight = data['weight']
        self.base_experience = data['base_experience']
        self.ident = data['id']
        self.abilities = [v['ability']['name'] for v in data['abilities']]

class MyPokemon:
    def __init__(self, name, types, height, weight, base_experience, ident, abilities):
        self.name = name
        self.types = types
        self.height = height
        self.weight = weight
        self.base_experience = base_experience
        self.ident = ident
        self.abilities =  abilities  
        
my_pokedex = Pokedex()
my_pokedex.Screen()
        
        





