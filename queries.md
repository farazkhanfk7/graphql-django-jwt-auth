# Query Examples

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

> Register : To register user using GraphQL_auth and jwt
```
mutation {
  register(
    email: "new_user@email.com",
    username: "new_user",
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