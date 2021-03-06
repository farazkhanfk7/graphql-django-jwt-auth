# GraphQL-Django-JWT-Authentication

![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue) 
> JWT Authentication in Django using GraphQl. Used graphene, django-graphql-jwt and django-graphql-auth

<a href="https://ibb.co/1MHvnWt"><img src="https://i.ibb.co/Lr4kP7X/Screenshot-from-2021-07-17-18-08-15.png" alt="Screenshot-from-2021-07-17-18-08-15" border="0"></a>

## Query Examples

> UserQuery : To get user data ( when using `graphql_auth` and `UserQuery` to build schema)

```
query{
  users{
    edges{
      node{
        username
        email
      }
    }
  }
}
```
<br>

> MeQuery : To get user data ( when using `graphql_auth` and `MeQuery` to build schema)

```
query{
  me {
    username
    email
    isStaff
  }
}
```
<br>

>  Register : To register user using GraphQL_auth and jwt

```
mutation {
  register(
    email: "batman@gmail.com",
    username: "batman",
    password1: "killshot69",
    password2: "killshot69",
  ) {
    success,
    errors,
    token,
    refreshToken
  }
}
```
<br>

>  Verify Account :

A URL like this will be returned in terminal if you're using EMAIL_BACKENDS in settings.py

```
http://127.0.0.1:8000/activate/eyJ1c2VybmFtZSI6Im5ld191c2VyIiwiYW
```
This token can be used to send a mutation query from frontend to verify the user. 
( Also check `userstatus` table)

Mutation Query : 

```
mutation {
  verifyAccount(token: "eyJ1c2VybmFtZSI6Im5ld191c2VyIiwiYW") {
    success,
    errors
  }
}
```

<br>

> Login : 

```
mutation {
  tokenAuth(username: "batman", password: "killshot69") {
    success,
    errors,
    unarchiving,
    token,
    refreshToken,
    unarchiving,
    user {
      id,
      username,
    }
  }
}
```
<br>

> Update Account : 

This time we'll have to add Authorization tokens to tell which user we want to update.
Use any API testing client that supports GraphQL like **Insomnia** or **Postman**.

* Login first and copy the token from Response.
* Make mutation but add token in Authorization header as well :

`AUTHORIZATION` : `JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJI.....`

```
mutation {
  updateAccount(
    firstName: "Faraz"
  ) {
    success,
    errors
  }
}
```
<br>

**Forgot Password ?**

> Send Password Reset Email

```
mutation {
  sendPasswordResetEmail(
    email: "batman@email.com"
  ) {
    success,
    errors
  }
}
```

And copy the url token from terminal. 

> Password Reset 

```
mutation {
  passwordReset(
    token: "1eyJ1c2VybmFtZSI6InNreX...",
    newPassword1: "deadshot69",
    newPassword2: "deadshot69"
  ) {
    success,
    errors
  }
}
```