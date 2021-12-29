# Family-Tree

Simform Assignment

## API Endpoints

| Method              | Endpoint                 | Description                                      |
| ------------------- | ------------------------ | ------------------------------------------------ |
| POST                | /users                   | Creates a new user                               |
| POST                | /authenticate            | Authenticates a user and returns a JWT           |
| PATCH, GET, DELETE  | /users/{id}              | Updates or deletes a user                        |
| PATCH, POST, DELETE | /relations/parents       | Adds, updates or removes a parent to a user      |
| PATCH, POST, DELETE | /relations/siblings      | Adds, updates or removes a sibling to a user     |
| GET                 | /users/{id}/grandparents | Returns a list of all the grandparents of a user |
| GET                 | /users/{id}/children     | Returns a list of all the children of a user     |
| GET                 | /users/{id}/siblings     | Returns a list of all the siblings of a user     |
| GET                 | /users/{id}/parents      | Returns a list of all the parents of a user      |
