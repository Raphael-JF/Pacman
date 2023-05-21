class Timer():
    """Timer est un objet assez simple permettant de renvoyer un signal quand une durée est écoulée"""


    def __init__(self,seconds:int,callback=lambda *args:None,*infos):
        """
        seconds -> la durée en seconde avant laquelle le Timer arrive à sa fin.
        callback -> Une fonction appelée à la fin du timer et prenant en argument tout argument renseigné en trop dans le __init__() (même ordre)
        infos -> les arguments transmis à callback
        """

        if seconds < 0:
            seconds = 0

        self.callback = callback
        self.infos = infos
        self.seconds = seconds
        self.elapsed = 0
        self.finished = False
        self.frozen = False

    def pass_time(self,time):
        """Ajoute `time` au temps écoulé du Timer. si le temps écoulé dépasse la durée initalement renseignée, alors cette méthode appelle la fonction associée à l'objet"""

        if self.frozen:
            return

        self.elapsed += time

        if self.elapsed >= self.seconds:
            self.finished = True
            self.callback(*self.infos)
            

    def pause(self):
        """Met en pause le Timer ou le remet en marche si il l'est déjà. En pause, le timer ne passe plus son temps."""

        self.frozen = not(self.frozen)