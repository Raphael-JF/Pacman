"""Ce module gère la boucle principale du jeu. C'est ce fichier qu'il faut exécuter pour lancer le jeu. """


if __name__ == "__main__":
    from classes.manager import Manager
    MAIN = Manager()
    while True:
        MAIN.manage_state()

#faut s'occuper de pouvoir changer de direction