import unittest
from unittest.mock import patch, MagicMock
from OpenAi.Atelier1.main import get_function_source, generate_docstring

class TestDocstringGenerator(unittest.TestCase):

    def test_get_function_source(self):
        """Teste la récupération de code source via inspect."""

        # La fonction locale doit être indentée correctement sous la méthode de test
        def sample():
            """Une fonction simple pour le test."""
            return 42
        
        # NOTE : Le code source retourné par inspect inclut la docstring et l'indentation
        code = get_function_source(sample)
        self.assertIn("def sample():", code)
        self.assertIn('"""Une fonction simple pour le test."""', code)

    @patch('openai.OpenAI')
    def test_generate_docstring(self, MockOpenAIClient):
        """Teste la génération de docstring avec l'API mockée."""
        
        # 1. Configuration de la réponse mockée
        expected_docstring = '"""Docstring générée par le test"""'
        
        # Simuler l'objet réponse de l'API OpenAI
        mock_response = MagicMock()
        mock_response.choices[0].message.content = expected_docstring
        
        # Configuration du mock pour que create() retourne la réponse simulée
        # Le premier argument du patch est l'objet à mocker
        MockOpenAIClient.return_value.chat.completions.create.return_value = mock_response

        # 2. Exécution de la fonction à tester
        # On utilise l'instance mockée du client (MockOpenAIClient.return_value)
        client_instance = MockOpenAIClient.return_value
        result = generate_docstring(client_instance, "def test_function(): pass")

        # 3. Assertions
        self.assertIsNotNone(result)
        self.assertEqual(expected_docstring, result)
        
        # Vérifier que l'API a été appelée
        client_instance.chat.completions.create.assert_called_once()


        