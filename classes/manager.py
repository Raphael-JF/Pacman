import importlib
import pygame
import sys
import os
import time

import assets
from classes.json_handler import JSON_handler

import elements.start_menu as start_menu
import elements.campagne as campagne
import elements.personnalise as personnalise
import elements.parameters as parameters
import elements.credits as credits
import elements.game as game


class Manager():
    """L'objet Manager gère le comportement du jeu à chaque image. Il redirige vers les instructions à exécuter en fonction des actions utilisateur."""

    def __init__(self):
        pygame.init()
        #variables
        self.fps = assets.START_GAME_FPS
        self.last_time = time.perf_counter()
        self.state = self.loop_start_menu
        
        #initialisation
        self.current_winsize = assets.INIT_WINSIZE
        self.win = pygame.display.set_mode(self.current_winsize)
        self.show_fps = False
        self.first_start = True
        self.clock = pygame.time.Clock()
        self.first_looping = True
        self.game_screen = None
        self.lvl_path = None

    
    def tick(self):
        """
        Gestion du temps. A chaque tour de boucle, l'attribut dt est affecté et contient la durée en ms depuis la dernière exécution de cete méthode.
        """

        self.dt = (time.perf_counter() - self.last_time)
        self.last_time = time.perf_counter()
        self.clock.tick(self.fps)
        

    def manage_state(self):
        """
        Redirection vers des instructions spécifiques en fonction de l'état actuel du jeu.
        """

        self.tick()
        self.state()
        

    def loop_start_menu(self):
        """
        Instructions du menu de lancement du jeu. action désigne l'action utilisateur (sur quel bouton il a apppuyé et dans quel menu doit il se rendre par conséquent)
        """
        
        action = start_menu.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps])
        if action == 0:
            importlib.reload(start_menu)
            self.state = self.loop_campagne
            self.first_looping = True
        if action == 1:
            importlib.reload(start_menu)
            self.state = self.loop_perso
            self.first_looping = True
        if action == 2:
            importlib.reload(start_menu)
            self.state = self.loop_parameters
            self.first_looping = True
        if action == 3:
            importlib.reload(start_menu)
            self.state = self.loop_credits
            self.first_looping = True
        if action == 4:
            pygame.quit()
            sys.exit()

    def loop_campagne(self):
        action = campagne.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps])
        if action == 0:
            importlib.reload(campagne)
            self.state = self.loop_start_menu
            self.first_looping = True
        elif action == 1:
            importlib.reload(campagne)
        elif type(action) is str:
            importlib.reload(campagne)
            self.lvl_path = os.path.join(os.getcwd(),
            "levels","lvl"+action+".json")
            self.state = self.loop_game
            self.first_looping = True

    def loop_perso(self):
        action = personnalise.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps],self.first_looping)
        self.first_looping = False
        if action == 0:
            importlib.reload(personnalise)
            self.state = self.loop_start_menu
            self.first_looping = True
        elif action == 1:
            importlib.reload(personnalise)
            self.lvl_path = ["map_editor","latest.json"]
            self.state = self.loop_game
            self.first_looping = True
        elif type(action) is str:
            self.lvl_path = action

    def loop_parameters(self):
        if self.first_looping:
            action = parameters.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps],True)
            self.first_looping = False
        else:
            action = parameters.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps],False)
        
        if action == 0:
            importlib.reload(parameters)
            self.state = self.loop_start_menu
            self.first_looping = True
            
        elif type(action) is dict :
            if self.current_winsize != action['resolution']:
                self.current_winsize = action['resolution']
                pygame.display.quit()
                self.win = pygame.display.set_mode(self.current_winsize)
            self.show_fps = action['montrer_fps']


    def loop_credits(self):
        action = credits.loop(self.win,self.current_winsize,self.dt,[self.fps,self.show_fps])
        if action == 0:
            importlib.reload(credits)
            self.state = self.loop_start_menu
            self.first_looping = True


    def loop_game(self):
        action = game.loop(self.win,self.current_winsize,self.dt,self.lvl_path,[self.fps,self.show_fps])
        if action == 0:
            importlib.reload(game)
            self.state = self.loop_start_menu
            self.lvl_path = None
            self.first_looping = True
        elif action == 1:
            importlib.reload(game)
            self.first_looping = True
        elif action == 10:
            for i in range(9):
                if self.lvl_path == os.path.join(os.getcwd(),
            "levels","lvl"+str(i+1)+".json"):
                    save_manager = JSON_handler(["progress.json"])
                    print(save_manager.data)
                    save_manager["lvl"+str(i+2)] = True
                    save_manager.save(["progress.json"])
                    importlib.reload(campagne)
                    break
