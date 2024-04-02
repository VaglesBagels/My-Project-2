Trivia API
Documentation and API Reference

Trivia App Introduction
The Trivia app used by Udacity is a team building application used as an icebreaker and create a positive environment for the teaching team and students.

Author
Michael Lourens

Acknowledgements
I acknowledge the contribution of the Udacity team that create the Full Stack Nanodegree and its content. The tools and knowledge provided will stay with many students.

Basic Functionality - Trivia App
The app utilises CRUD opertations, python as a backend and react as a frontend.

Functionality of the app:
Displays questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
Delete questions.
Add questions and require that they include question and answer text.
Search for questions based on a text query string.
Play the quiz game, randomizing either all questions or within a specific category.
Getting Started and Local development
Fork the project repository and clone your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository.

Tech Stack
The tech stack has been outlined in the README in both frontend and backend folders.

Backend
The backend directory contains all information and data required to set up and use FLASK for this app.

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

View the Backend README for TODOS tasks and in depth steps on creating and running the application as well as testing the endpoints.

Tests
Create a test database using PostGres called trivia_test and follow backend README to populate. Ensure to also create a trivia database for the application.

Run the test_flaskr.py file in the terminal to get feedback of a successful or unsuccessful endpoint and unittest creation.

Frontend
The frontend directory contains a React framework from node.js to communicate and display the backend data. It has all information and files required to use and connect to the newly created backend.

These are the files to look at to ensure endpoints are connected to the backend and to add any other optional functionality:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

View the Frontend README for TODO tasks and in depth steps to setup and run the react application

API reference
Base URL
You need to ensure that both the backend flask server and the react server are running else the application will not run.

The flask server runs on localhost: http://localhost:5000

The trivia app will be using the React server which is also run on localhost: http://localhost:3000

Errors
Errors are returned in json format:

{
"success": False,
"error": 404,
"message": "Not found"
}

Trivia app returns the following error codes: 400, 404 and 422. The following is a list of the message ouput of the errors:

1. 400 'Bad Request'
2. 404 'Not Found'
3. 422 'Unprocessable'

Resources and Endpoints

GET /categories use curl http://127.0.0.1:5000/categories

General
Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
Request Arguments: None
Response
status: 200
Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.
{
"categories": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
}
}
GET /questions curl -X GET http://127.0.0.1:5000/questions?page=1

General:
Fetches a paginated set of questions, a total number of questions, all categories and current category string.
Request Arguments: page - integer
Response:
status: 200
Returns: An object with 10 questions a page, total questions-int, object including all categories, and current category for each question-string.
{"categories": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
},
"questions": [
{
"answer": "Apollo 13",
"category": 5,
"difficulty": 4,
"id": 2,
"question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
},
{
"answer": "Tom Cruise",
"category": 5,
"difficulty": 4,
"id": 4,
"question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
},
{
"answer": "Maya Angelou",
"category": 4,
"difficulty": 2,
"id": 5,
"question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
},
{
"answer": "Edward Scissorhands",
"category": 5,
"difficulty": 3,
"id": 6,
"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
},
{
"answer": "Muhammad Ali",
"category": 4,
"difficulty": 1,
"id": 9,
"question": "What boxer's original name is Cassius Clay?"
},
{
"answer": "Brazil",
"category": 6,
"difficulty": 3,
"id": 10,
"question": "Which is the only team to play in every soccer World Cup tournament?"
},
{
"answer": "Uruguay",
"category": 6,
"difficulty": 4,
"id": 11,
"question": "Which country won the first ever soccer World Cup in 1930?"
},
{
"answer": "George Washington Carver",
"category": 4,
"difficulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
},
{
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
},
{
"answer": "The Palace of Versailles",
"category": 3,
"difficulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
}
],
"success": true,
"total_questions": 20
}
POST /questions curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question":"When was REACT first released", "answer":"look up in Google", "difficulty":"1", "category":"1"}'

General
Request body
sends a create question operation to the backend
Request args: question, answer - string, difficulty - integer
Response:
Status: 200
Returns: An object with question id- integer, success - boolean
{
"created": 24,
"success": true
}
GET /categories/${id}/questions curl -X GET http://127.0.0.1:5000/categories/1/questions

General:
Fetches questions for a cateogry specified by id request argument
Request Arguments: category id - integer
Response: http status code 200
Returns: An object with questions for the specified category, total questions, and current category for the questions
{
"current_category": "Science",
"questions": [
{
"answer": "The Liver",
"category": 1,
"difficulty": 4,
"id": 20,
"question": "What is the heaviest organ in the human body?"
},
{
"answer": "Alexander Fleming",
"category": 1,
"difficulty": 3,
"id": 21,
"question": "Who discovered penicillin?"
},
{
"answer": "Blood",
"category": 1,
"difficulty": 4,
"id": 22,
"question": "Hematology is a branch of medicine involving the study of what?"
},
{
"answer": "look up in Google",
"category": 1,
"difficulty": 1,
"id": 24,
"question": "When was REACT first released"
}
],
"success": true,
"total_questions": 4
}
DELETE '/questions/${id}' curl -X DELETE http://127.0.0.1:5000/questions/27

General:
Deletes a specified question using the id of the question
Request Arguments: id - integer
Response: http - status 200
Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.
{
"deleted": 27,
"success": true
}
POST '/quizzes' curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"quiz_category": {"id":"1"}, "previous_questions": []}'

General:
Sends a post request in order to get the next question
Request Body: args - quiz_category-id integer, or string, previous_questions- list:
{
"quiz_category": {"id":"1"}, "previous_questions": []
}
Response: status OK
Returns: a single new question object
{
"question": {
"answer": "Blood",
"category": 1,
"difficulty": 4,
"id": 22,
"question": "Hematology is a branch of medicine involving the study of what?"
},
"success": true
}
POST '/questions/search' curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "title"}'

General:
Sends a post request in order to search for a specific question by search term: searchTerm - string
Request Body:
{
"searchTerm": "title"
}
Response: status 200
Returns: any array of questions, a number of total_questions that met the search term and the current category string
{
"questions": [
{
"answer": "Maya Angelou",
"category": 4,
"difficulty": 2,
"id": 5,
"question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
},
{
"answer": "Edward Scissorhands",
"category": 5,
"difficulty": 3,
"id": 6,
"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
}
],
"success": true,
"total_questions": 2
}
