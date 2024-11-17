import unittest
from account_type_predictor.account_type_predictor import AccountTypePredictor

class TestAccountTypePredictor(unittest.TestCase):
    def setUp(self):
        # Initialisez le prédicteur avant chaque test
        self.predictor = AccountTypePredictor()

    def test_prediction(self):
        labels = ["Compte PEA", "Livret A", "RES Multisupport"]
        predictions = self.predictor.predict(labels)
        self.assertEqual(len(predictions), 3)  # Vérifie qu'il y a 3 prédictions
        print("Test successful: ", predictions)

if __name__ == "__main__":
    unittest.main()
