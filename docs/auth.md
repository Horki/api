# Group Authorization endpoints

## Get all active users [/auth/all]
### Get all active users [GET]
+ Response 200 (application/json)

        {
          "data": [
            {
              "id": 1,
              "username": "Test User",
              "email": "test@test.com"
            },
            {
              "id": 2,
              "username": "Other User",
              "email": "other@test.com"
            },
            ...
          ]
        }

## Register a new user [/auth/register]
### Register a new user [POST]
After creating record in users table, send email to user via [Redis Queue](http://python-rq.org/).

+ Request
    + Headers

            Content-Type: application/json

    + Attributes
        + username: Test User (required, string)
        + email: test@test.com (required, string)
        + password: 123456 (required, string)


+ Response 201 (application/json)

        {
            "message": "Hej Test User, please check your email: test@test.com."
        }

## Activate new user [/auth/activate/{token}]
+ Parameters
    + token (required, string, `bec250b15ea84a769d4143c9e267f349`)
### Activate new user [GET]
Activation link send in user's email via [Flask Mail](https://pythonhosted.org/Flask-Mail/).

+ Response 200 (application/json)

        {
            "message": "User 'Test User' is activated"
        }

## Login [/auth]
### Login [POST]
Token is valid for next 10 minutes [Flask JWT](https://pythonhosted.org/Flask-JWT/).

+ Request
    + Headers

            Content-Type: application/json

    + Attributes
        + email: test@test.com (required, string)
        + password: 123456 (required, string)

+ Response 200 (application/json)

        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwibmJmIjoxNDgzNDYxMjI0LCJpYXQiOjE0ODM0NjEyMjQsImV4cCI6MTQ4MzQ2MTgyNH0.o-F616aK3aOOLD1QgzNaObctfIZULWH2FFdtUmgF5dQ"
        }


## Get current user [/auth/me]
### Get current user [GET]
Get current user via Flask JWT token
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
+ Response 200 (application/json)

        {
          "data": {
              "id": 1,
              "username": "Test User",
              "email": "test@test.com"
            }
        }
