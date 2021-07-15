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