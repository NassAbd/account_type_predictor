import re

def clean_label(label):
    """
    Nettoie un texte donné en supprimant les caractères non alphanumériques
    et en le convertissant en minuscule.
    """
    label = label.lower()
    label = re.sub(r'[^a-z0-9\s]', '', label)
    return label
