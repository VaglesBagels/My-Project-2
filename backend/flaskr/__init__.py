import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy import not_

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)

    """
    @TODO: Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    """
    # CORS(app)
    CORS(app, resources={"/": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():
        try:
            data = Category.query.all()
            categories = {}
            for category in data:
                categories[category.id] = category.type

            if len(data) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'categories': categories
            })
        except Exception as e:
            # print(e)
            abort(500)

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination
    at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions', methods=['GET'])
    def get_questions():
        try:
            page = request.args.get('page', 1, type=int)

            pagination = Question.query.paginate(
                page=page,
                per_page=QUESTIONS_PER_PAGE
                )

            current_questions = pagination.items
            total_questions = pagination.total

            if len(current_questions) == 0:
                raise ValueError

            formatted_questions = [
                question.format()
                for question in current_questions]

            categories = Category.query.all()
            formatted_categories = {
                                    category.id: category.type
                                    for category in categories}

            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': total_questions,
                'categories': formatted_categories
            })
        except Exception as e:
            # print(e)
            abort(404)

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question,
    the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:qid>', methods=['DELETE'])
    def delete_question(qid):
        try:
            question = Question.query.filter(Question.id == qid).one_or_none()

            if question is None:
                raise ValueError

            question.delete()

            return jsonify(
                {
                    'success': True,
                    'deleted': qid
                }
            )
        except Exception as e:
            # print(e)
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear
    at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()

            if len(body) != 4:
                raise ValueError

            new_question = body.get('question')
            new_answer = body.get('answer')
            new_category = body.get('category')
            new_difficulty = body.get('difficulty')

            question = Question(
                                question=new_question,
                                answer=new_answer,
                                category=new_category,
                                difficulty=new_difficulty)
            question.insert()

            return jsonify({
                'success': True,
                'created': question.id,
            })
        except Exception as e:
            # print(e)
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        try:
            body = request.get_json()

            search_term = body.get('searchTerm')

            questions = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')
                ).all()

            formatted_questions = [question.format() for question in questions]

            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(formatted_questions)
            })
        except Exception as e:
            # print(e)
            abort(400)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions_by_category(category_id):
        try:
            category = Category.query.filter(
                Category.id == category_id
                ).one_or_none()

            if category is None:
                raise ValueError

            questions = Question.query.filter(
                Question.category == category_id
                ).all()

            formatted_questions = [question.format() for question in questions]

            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(formatted_questions),
                'current_category': category.type
            })
        except Exception as e:
            # print(e)
            abort(404)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()

            previous_questions = body.get('previous_questions')
            quiz_category = body.get('quiz_category')

            category_id = quiz_category['id']

            if category_id == 0:
                quiz_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)
                    ).all()
            else:
                quiz_questions = Question.query.filter(
                    Question.category == category_id,
                    Question.id.notin_(previous_questions)
                    ).all()

            if (quiz_questions):
                question = random.choice(quiz_questions).format()
            else:
                question = None

            return jsonify({
                'success': True,
                'question': question,
                })

        except Exception as e:
            # print(e)
            abort(400)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app
