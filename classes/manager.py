import importlib
import pygame
import sys
import itertools

import assets
import elements.start_menu as start_menu
import elements.campagne as campagne
import elements.options as options
import elements.credits as credits
class Manager():
    """L'objet Manager gère le comportement du jeu à chaque image. Il redirige vers les instructions à exécuter en fonction des actions utilisateur."""

    def __init__(self):
        pygame.init()
        #variables
        self.fps = assets.START_GAME_FPS
        self.last_time = pygame.time.get_ticks()/1000
        self.state = self.loop_start_menu
        self.screen_size=itertools.cycle([
            [1280,720],
            [1600,900],
            
            [960,540],
            [1920,1080],
            [800,450],
            
            [1920,1080],
            [480,270],
            ])
        
        #initialisation
        self.current_winsize = next(self.screen_size) 
        self.win = pygame.display.set_mode(self.current_winsize)
        self.first_start = True
        self.clock = pygame.time.Clock()
        self.first_looping = True
        self.game_screen = None

    
    def tick(self):
        """
        Gestion du temps. A chaque tour de boucle, l'attribut dt est affecté et contient la durée en ms depuis la dernière exécution de cete méthode.
        """

        self.dt = (pygame.time.get_ticks()/1000 - self.last_time)
        self.last_time = pygame.time.get_ticks()/1000
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
        
        action = start_menu.loop(self.win,self.current_winsize,self.dt,self.fps)
        if action == 1:
            importlib.reload(start_menu)
            self.state = self.loop_campagne
        if action == 2:
            pass
        if action == 3:
            pass
        if action == 4:
            pass
        if action == 5:
            pygame.quit()
            sys.exit()

    def loop_campagne(self):
        action = campagne.loop(self.win,self.current_winsize,self.dt,self.fps)
        if action == 1:
            importlib.reload(start_menu)
            self.state = self.loop_start_menu
        if action == 2:
            pass
        if action == 3:
            pass
        if action == 4:
            pass
        if action == 5:
            pygame.quit()
            sys.exit()

    def loop_options(self):
        action = options.loop(self.win,self.current_winsize,self.dt,self.fps)
        if action == 1:
            importlib.reload(start_menu)
            self.state = self.loop_start_menu


    def loop_credits(self):
        action = credits.loop(self.win,self.current_winsize,self.dt,self.fps)
        if action == 1:
            importlib.reload(start_menu)
            self.state = self.loop_start_menu
        if action == 2:
            pass
        if action == 3:
            pass
        if action == 4:
            pass
        if action == 5:
            pygame.quit()
            sys.exit()
