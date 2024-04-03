# Trivia API

Documentation and API Reference

## Trivia App Introduction

The Trivia app used by Udacity is a team building application used as an icebreaker and create a positive environment for the teaching team and students.

## Author

Michael Lourens

## Acknowledgements

I acknowledge the contribution of the Udacity team that create the Full Stack Nanodegree and its content. The tools and knowledge provided will stay with many students.

## Basic Functionality - Trivia App

The app utilises CRUD opertations, python as a backend and react as a frontend.

## Functionality of the app:

Displays questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
Delete questions.
Add questions and require that they include question and answer text.
Search for questions based on a text query string.
Play the quiz game, randomizing either all questions or within a specific category.
Getting Started and Local development
Fork the project repository and clone your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository.

## Tech Stack

The tech stack has been outlined in the README in both frontend and backend folders.

## Backend

The backend directory contains all information and data required to set up and use FLASK for this app.

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

View the Backend README for TODOS tasks and in depth steps on creating and running the application as well as testing the endpoints.

### Tests

Create a test database using PostGres called trivia_test and follow backend README to populate. Ensure to also create a trivia database for the application.

Run the test_flaskr.py file in the terminal to get feedback of a successful or unsuccessful endpoint and unittest creation.

## Frontend

The frontend directory contains a React framework from node.js to communicate and display the backend data. It has all information and files required to use and connect to the newly created backend.

These are the files to look at to ensure endpoints are connected to the backend and to add any other optional functionality:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

View the Frontend README for TODO tasks and in depth steps to setup and run the react application

# API reference

## Base URL

You need to ensure that both the backend flask server and the react server are running else the application will not run.

The flask server runs on localhost: http://localhost:5000

The trivia app will be using the React server which is also run on localhost: http://localhost:3000

## Errors

Errors are returned in json format:

```json
{
  "success": false,
  "error": 404,
  "message": "Not found"
}
```

Trivia app returns the following error codes: 400, 404 and 422. The following is a list of the message ouput of the errors:

1. 400 'Bad Request'
2. 404 'Not Found'
3. 422 'Unprocessable'

## Resources and Endpoints

`GET '/categories'` USE: `curl http://127.0.0.1:5000/categories`

Fetches a dictionary of categories found in the PostGres Trivia database

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

Content :

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

`GET '/questions?page=${integer}'` USE: `curl -X GET http://127.0.0.1:5000/questions?page={integer}`

Fetches a page with a set of questions, shows total number of questions and all categories and which category each question is in.

- Fetches a paginated set of questions, a total number of questions and all categories.
- Request Arguments: `page` - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories

Content :

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
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
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
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
  "total_questions": 19
}
```

`GET '/categories/${id}/questions'` USE: `curl -X GET http://127.0.0.1:5000/categories/{id}/questions`

- Fetches questions for a cateogry specified by id request argument
- Request Arguments: `id` - integer
- Returns: An object with questions for the specified category, total questions, and current category string

Content :

```json
{
  "current_category": "Science",
  "questions": [
    {
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4
    },
    {
      "id": 21,
      "question": "Who discovered penicillin?",
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3
    },
    {
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "answer": "Blood",
      "category": 1,
      "difficulty": 4
    }
  ],
  "success": true,
  "total_questions": 3
}
```

`DELETE '/questions/${id}'` USE: `curl -X DELETE http://127.0.0.1:5000/questions/{id}`

- Deletes a specified question using the id of the question
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.

`POST '/quizzes'` USE: `curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"quiz_category": {"id":"{integer}"}, "previous_questions": []}'`

- Sends a post request in order to get the next question
- Request Body:

Content:

```json
{
  "quiz_category": { "id": "1" },
  "previous_questions": []
}
```

- Returns: a single new question object

```json
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
```

`POST '/questions/search'` USE: `curl -X POST http://127.0.0.1:5000/questions/search -H "Content-Type: application/json" -d '{"searchTerm": "{searchTerm}"}'`

- Sends a post request in order to search for a specific question by search term
- Request Body:

Content :

```json
{
  "searchTerm": "royal"
}
```

- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

```json
{
  "questions": [
    {
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3
    }
  ],
  "success": true,
  "total_questions": 1
}
```
