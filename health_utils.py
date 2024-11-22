def calculate_imc(taille, masse):
    """Calcul l'indice de masse corporelle (IMC).
    
    :param taille: Taille en mètres.
    :param masse: Masse en kilogrammes.
    :return: Valeur de l'IMC.
    """

    return masse / (taille ** 2)

def calculate_mb(taille, masse, age, genre):
    """Calcul le métabolisme de base (MB).
    
    Basé sur l'équation de Harris-Benedict révisée en 1984 par Roza et Shizgal.

    :param taille: Taille en centimètres.
    :param masse: Masse en kilogrammes.
    :param age: Age en années.
    :param genre: Genre ('homme' ou 'femme')
    :return: Valeur du MB (kcal/jour) ou message d'erreur si le genre est invalide.
    """

    if genre.lower() == 'homme':
        return 88.362 + (13.397 * masse) + (4.799 * taille) - (5.677 * age)
    elif genre.lower() == 'femme':
        return 447.593 + (9.247 * masse) + (3.098 * taille) - (4.330 * age)
    else:
        return 'Genre Invalide'