# Group Data Testing public endpoints

## Get basic output [/data/test]
### Get basic output [GET]
+ Response 200 (application/json)

        {
            "test": "test"
        }

## Get value from redis db [/data/cache]
### Get value from redis db [GET]
Add a record to redis database key=foo, value=bar and retrieve it.

+ Response 200 (application/json)

        {
            "redis": "bar"
        }

## Get empty output [/data/empty]
### Get empty output [GET]
+ Response 204 (application/json)


## Post some dummy data [/data/add]
### Post some dummy data [POST]
This endpoint is for testing purpose only, response is same as output, anything goes

+ Request (application/json)

        {
            "test": "test"
        }

+ Response 201 (application/json)

        {
            "test": "test"
        }

