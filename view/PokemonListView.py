"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from PyInquirer import prompt, Separator

from examples import custom_style_2
from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session
from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        
        liste_pokemons = get_pokemon_from_webservice(limit = 30)
        self.__questions = [
            {
                'type': 'checkbox',
                'qmark': '🐹',
                'message': 'Sélectionne un Pokemon à détailler',
                'name': 'pokemons',
                'choices': [
                    {'name':liste_pokemons[0]}
                    ,{'name':liste_pokemons[1]}
                    ,{'name':liste_pokemons[2]}
                    ,{'name':liste_pokemons[3]}
                    ,{'name': 'Revenir à l''accueil'}
                ]
            }
        ]
    
    def display_info(self):
        """Permet d'afficher des infos en console. On va mettre ici la partie non interactive de la page
        """
        print(f"Hello {Session().user_name}, regarde en détail un Pokemon ou reviens à l'accueil.")
        
    def make_choice(self):
        """Affiche la partie interactive de notre page
        """
        #On affiche le menu
        reponse = self.__questions.execute()
        if reponse == 'Revenir à l''accueil':
            #Si la réponse à la question est 'Revenir à l''accueil' on va à l'accueil.
            next_view = StartView()
        else:
            #On détaille le Pokemon sélectionné
            next_view = PokemonDetailsView()
        
        

