import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def populate_test_data(self):
        """Populates the database with test data"""
        # Insert categories
        category1 = Category(type='Science')
        category2 = Category(type='History')
        self.db.session.add_all([category1, category2])
        self.db.session.commit()

        # Insert questions
        question1 = Question(question='What is the capital of France?', answer='Paris', category=1, difficulty=2)
        question2 = Question(question='Who invented the telephone?', answer='Alexander Graham Bell', category=1, difficulty=3)
        self.db.session.add_all([question1, question2])
        self.db.session.commit()

    def test_get_categories(self):
        """Test GET /categories"""
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['categories']) > 0)

    def test_get_questions(self):
        """Test GET /questions"""
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['questions']) > 0)
        self.assertTrue(data['total_questions'] > 0)
        self.assertTrue(len(data['categories']) > 0)

    def test_404_get_questions_invalid_page(self):
        """Test GET /questions with invalid page"""
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_question(self):
        """Test DELETE /questions/<question_id>"""
        question_id = 1
        res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], question_id)

    def test_404_delete_question_not_found(self):
        """Test DELETE /questions/<question_id> with question not found"""
        question_id = 1000
        res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()