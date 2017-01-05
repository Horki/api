# Group Book endpoints

## Book [/book]
### Get all books [GET]
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
+ Response 200 (application/json)

        {
          "data": [
            {
              "id": 1,
              "title": "Ducimus sit ut repellendus.",
              "author": "Dragutin Dominković",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            },
            {
              "id": 2,
              "title": "Quis culpa delectus assumenda recusandae.",
              "author": "Vjekoslav Milotić",
              "user": {
                  "id": 2,
                  "username": "Other User",
                  "email": "other@test.com"
              }
            },
            ...
          ]
        }

## Book [/book/]
### Add book [POST]
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
    
    + Body

            {
                "title": "Test",
                "author": "test"
            }

    + Attributes
        + title: The Hitchhiker's Guide to the Galaxy (required, string)
        + author: Douglas Adams (required, string)
+ Response 201 (application/json)

        {
          "data": [
            {
              "id": 1,
              "title": "Ducimus sit ut repellendus.",
              "author": "Dragutin Dominković",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            },
            {
              "id": 2,
              "title": "Quis culpa delectus assumenda recusandae.",
              "author": "Vjekoslav Milotić",
              "user": {
                  "id": 2,
                  "username": "Other User",
                  "email": "other@test.com"
              }
            },
            ...
          ]
        }


## Get books by current user [/book/me]
### Get books by current user [GET]
Get current user via Flask JWT token
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
+ Response 200 (application/json)

        {
          "data": [
            {
              "id": 1,
              "title": "Ducimus sit ut repellendus.",
              "author": "Dragutin Dominković",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            },
            {
              "id": 4,
              "title": "Quos fugit molestiae sint soluta libero.",
              "author": "Ivica Tešija",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            },
            ...
          ]
        }


## Book by id [/book/{id}]
+ Parameters
    + id (required, integer, `1`)
### Get book by id [GET]
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
+ Response 200 (application/json)

        {
            "data": {
              "id": 1,
              "title": "Ducimus sit ut repellendus.",
              "author": "Dragutin Dominković",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            }
        }

### Edit book by id [PUT]
User can edit only his books
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token}

    + Attributes
        + title: Test (optional, string)
        + author: Test (optional, string)

+ Response 200 (application/json)

        {
            "data": {
              "id": 1,
              "title": "Ducimus sit ut repellendus.",
              "author": "Dragutin Dominković",
              "user": {
                  "id": 1,
                  "username": "Test User",
                  "email": "test@test.com"
              }
            }
        }

### Delete book by id [DELETE]
+ Request
    + Headers

            Content-Type: application/json
            Authorization: JWT {token} 
+ Response 200 (application/json)

        {
            "message": "Book id: 1 deleted"
        }