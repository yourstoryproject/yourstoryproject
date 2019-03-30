# Account API

### Base URL: `/api/v1/accounts`

| Action | HTTP Verb | URL Path | Description
|---|---|---|---|
| Read | GET | /get_accounts | Fetch all accounts |
| Read | GET | /get_accounts | Fetch single account matching query parameter: \<account_id> |
| Create | POST | /create_account | Create an account. Expects query parameters: \<email>, \<password>
