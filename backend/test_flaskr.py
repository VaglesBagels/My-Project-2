import os
import unittest 
import json
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import patch, MagicMock

from flaskr import create_app
from models import setup_db, Question, Category
from dotenv import load_dotenv

# load .env file in backend dir using python-dotenv lib
load_dotenv()

database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
database_host = os.getenv("DB_HOST")
database_port = os.getenv("DB_PORT")


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia_test"
        self.database_path = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{self.database_name}"
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Success and error behaviour of GET Categories Endpoint
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
    
    def test_get_categories_error(self):
        with self.app.app_context():
            mock_query = MagicMock()
            mock_query.all.return_value = []

            with patch('flaskr.Category.query', return_value=mock_query):
                res = self.client().get('/categories')
                data = json.loads(res.data)
                
                self.assertEqual(res.status_code, 500)
                self.assertFalse(data['success'])
                self.assertEqual(data['message'], 'Internal Server Error')

    # Success and error behaviou of GET Questions endpoint
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    def test_get_questions_error(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)
        
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    # Success and error behaviour of POST Question endpoint
    def test_create_question(self):
        new_question = {
            'question': 'Is this a test',
            'answer': 'True',
            'category': 1,
            'difficulty': 1
        }

        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    def test_search_questions(self):
        search_term = 'test'

        res = self.client().post('/questions/search', json={'searchTerm': search_term})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    def test_get_questions_by_category(self):
        category_id = 1

        res = self.client().get(f'/categories/{category_id}/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    def test_play_quiz(self):
        quiz_data = {
            'previous_questions': [],
            'quiz_category': {'id': 1, 'type': 'Science'}
        }

        res = self.client().post('/quizzes', json=quiz_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

if __name__ == "__main__":
    unittest.main()