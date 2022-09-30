class PokemonListView(AbstractView):
    def __init__(self):
        # Définition d'une variable qui va stocker notre ou nos interactions

        self.questions = inquirer.selct(# Pour dire que la question va permettre de sélectionner un choix
            message=f'Bonjour {Session().user_name}. Tu peux voir 30 Pokemons sommairement.' #Un message à afficher avant de proposer les choix. cela peut être une question
            , choices=[
                Choice('Voir 30 Pokemon') #choix 1
                ,Choice('Revenir à l''accueil') #choix 2
                , Choice('Au revoir') #choix 3
            ])
    
    def display_info(self):
        """Permet d'afficher des infos en console. On va mettre ici la partie non interactive de la page
        """
        
        def make_choice(self):
            """Affiche la partie interactive de notre page
            """
            #On affiche le menu
            reponse = self.__questions.execute()
            #En fonction de la réponse on va retourner des pages différentes
            if reponse == 'Voir 30 Pokemon'
                #Si la réponse à la question est 'Voir 30 Pokemon' 
                print(get_pokemon_from_webservice(limit = 30))
                


                next_view = PokemonDetailsView()
            elif reponse == 'Revenir à l''accueil':
                #Si la réponse à la question est 'Revenir à l''accueil' on va à l'accueil.
                next_view = WelcomeView()
            

