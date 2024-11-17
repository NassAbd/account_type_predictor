import joblib
from .preprocess import clean_label

class AccountTypePredictor:
    def __init__(self, model_path='account_type_predictor/account_type_predictor/account_type_model.pkl'):
        """
        Initialise le prédicteur en chargeant le modèle préentraîné.
        """
        self.model = joblib.load(model_path)

    def predict(self, labels):
        """
        Prédit le type de compte pour une liste de libellés donnés.

        :param labels: Liste de chaînes de caractères.
        :return: Liste des prédictions.
        """
        cleaned_labels = [clean_label(label) for label in labels]
        return self.model.predict(cleaned_labels)
