import assets

def transition(valdebut:float,valfin:float,duree:int,ease_mode:str,avancement:int=None) -> float or list:
    """Calcul de la fonction d'accélaration cubique d'une valeur à une autre.
    - valdebut est la valeur de début
    - valfin est la valeur de fin
    - duree est le nombre de cases du tableau renvoyé
    - ease_mode est le mode de transition ('in','out','inout','linear')
    - si avancement est renseigné, renvoie la valeur d'index avancement, sinon renvoie toutes les valeurs dans un tableau"""

    if duree == 0:
        return valfin if avancement==None else [valfin]

    if avancement == None:
        sortie = []
        for avancement in range(1,duree):
            evolution = avancement / duree
            if ease_mode == "in":
                valeur = evolution**3
                sortie.append(valfin*valeur + valdebut*(1-valeur))
            elif ease_mode == "out":
                valeur = (evolution - 1)**3 + 1
                sortie.append(valfin*valeur + valdebut*(1-valeur))
            elif ease_mode == "inout":
                if evolution < 0.5:
                    valeur = 4 * evolution**3
                    sortie.append(valfin*valeur + valdebut*(1-valeur))
                else:
                    valeur = 0.5*(2*evolution - 2)**3 + 1
                    sortie.append(valfin*valeur + valdebut*(1-valeur))
            elif ease_mode == "linear":
                valeur = (valfin-valdebut) / duree
                sortie.append(valdebut + valeur*avancement)
            else:
                raise ValueError("ease_mode doit être dans ['in','inout','out','linear']")
        return sortie + [valfin]
    else:
        avancement+=1
        if avancement > duree:
            raise ValueError("avancement ne peut être supérieur ou égal à duree")
        if avancement == duree : 
            return float(valfin)
        evolution = avancement / duree
        if ease_mode == "in":
            valeur = evolution**3
            return valfin*valeur + valdebut*(1-valeur)
        elif ease_mode == "out":
            valeur = (evolution - 1)**3 + 1
            return valfin*valeur + valdebut*(1-valeur)
        elif ease_mode == "inout":
            if evolution < 0.5:
                valeur = 4 * evolution**3
                return valfin*valeur + valdebut*(1-valeur)
            else:
                valeur = 0.5*(2*evolution - 2)**3 + 1
                return valfin*valeur + valdebut*(1-valeur)
        elif ease_mode == "linear":
                valeur = (valfin-valdebut) / duree
                return valdebut + valeur*avancement
        else:
            raise ValueError(f"ease_mode:{ease_mode} doit être dans ['in','inout','out','linear']")


def transition_many_values(values:list,durees:list,ease_modes:str,avancement:int=None):
    """
    values -> les valeurs que prendra la valeur à modifier
    durees -> les durées respectives à chaque transition
    ease_mode -> le mode de transformation : soit 'linear', soit 'inout' ('out' et 'in' autorisés pour 3 valeurs au plus)
    """
    
    if len(values) != len(durees)+1 != len(ease_modes)+1:
        raise ValueError("len(values), len(duree)+1 and len(ease_modes)+1 must be equal")

    if avancement == None:
        val_debut = values.pop(0)
        sortie = []

        for value,duree,ease_mode in zip(values,durees,ease_modes):
            sortie += transition(val_debut,value,duree,ease_mode)
            val_debut = value
        return sortie

    else:
        for i,duree in enumerate(durees):
            if avancement-duree > 0:
                avancement -= duree
            else:
                break
        return transition(values[i],values[i+1],duree,ease_modes[i],avancement-1)


class Transition():
    """Cette classe implémente la gestion de l'animation. Pour n'importe quelles valeurs étapes, seront calculées les valeurs intermédiaires, pour une durée donnée, pour allonger l'évolution d'une variable.
    exemple : pour passer de 0 à 500 avec une durée de 10 et un mode de transition 'in' (lent au début et croît de plus en plus vite): 
    [0.5, 4, 13.5, 32, 62.5, 108, 171.5, 256, 364.5, 500]"""


    def __init__(self,values:list[int|float|list[int|float]],ease_seconds:list[int],ease_modes:list[str]):
        """
        values -> les valeurs étapes (taille n). valeurs peut contenir des tableaux à une dimension (pratique pour les transitions de couleurs entre autres).
        nb_frames -> les durées de transition entre chaque paire de valeurs (taille n-1 par conséquent)
        ease_modes -> les modes de transition entre chaque paire de valeurs (taille n-1 par conséquent)

        """

        self.nb_frames = []
        for ease_second in ease_seconds:
            self.nb_frames.append(round(ease_second*assets.TIME_TICKING))
        self.ease_modes = ease_modes
        self.values = values
        self.index = 0


    def generer_frame(self,index:int) -> float|list[float]:
        """
        génère la valeur d'index donné
        """

        for i,seconds in enumerate(self.nb_frames) :
                if seconds == 0:
                    return self.values[i+1]

        if type(self.values[0]) in [float,int]:

            return transition_many_values(self.values,self.nb_frames,self.ease_modes,index)
       
        else:
            sortie = []
            for value_steps in zip(*self.values):
                sortie.append(transition_many_values(value_steps,self.nb_frames,self.ease_modes,index))

            return sortie


    def set_step_values(self,values,ease_seconds=None,ease_modes=None):
        """
        Réaffectation des valeurs de l'instance Transition.
        """

        if ease_seconds:
            self.nb_frames = []
            for ease_second in ease_seconds:
                self.nb_frames.append(round(ease_second*assets.TIME_TICKING))

        if ease_modes:
            self.ease_modes = ease_modes 

        self.values = values
        self.index = 0


    def resize_extremums(self,ratio):
        """
        Actualisation des valeurs en cas de changement de résolution.
        """

        if type(self.values[0]) in [float,int]:
            for i,value in enumerate(self.values):
                self.values[i] = value*ratio
            
        else:

            for i,step_values in enumerate(self.values):
                self.values[i] = list(step_values)

                for j, value in enumerate(step_values):
                    self.values[i][j] = value*ratio
            


    def change_index(self,dt:float,cur_val:float|list):
        """
        dt -> le temps écoulé depuis la dernière image
        """

        self.index += dt * assets.TIME_TICKING
        
        if self.index < 0:
            self.index = 0
        if self.index > sum(self.nb_frames)-1:
            self.index = sum(self.nb_frames)-1

        frame = self.generer_frame(round(self.index))

        return frame,frame != cur_val,self.index == sum(self.nb_frames)-1
    
    def get_list_of_values(self):
        """
        Renvoie une liste de toutes les valeurs successives. Pratique pour tester.
        """
        sortie = []
        for i in range(sum(self.nb_frames)):
            temp = self.generer_frame(i)
            if type (temp) in [int,float]:
                sortie.append(round(temp))
            else:
                temp = [round(i) for i in temp]
                sortie.append(temp)
        return sortie


    def reset_index(self):

        self.index = 0

        