
# OAuth 2 Client Credentials Grant



Documentation for accessing and setting credentials for BearerAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `o_auth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `o_auth_client_secret` |
| OAuthToken | `OAuthToken` | Object for storing information about the OAuth token | `o_auth_token` |



**Note:** Auth credentials can be set using `ClientCredentialsAuthCredentials` object, passed in as named parameter `client_credentials_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must initialize the client with *OAuth 2.0 Client Credentials Grant* credentials as shown in the following code snippet.

```python
client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    )
)
```



Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Client Credentials Grant*. This authorization includes the following steps.

The `fetch_token()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

```python
try:
    token = client.bearer_auth.fetch_token()
    client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(o_auth_token=token)
    config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
    client = ShellevClient(config)
except OAuthProviderException as ex:
    # handle exception
    pass
except APIException as ex:
    # handle exception
    pass
```

The client can now make authorized endpoint calls.

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.client_credentials_auth_credentials.o_auth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_token=load_token_from_database()
    )
)
```

### Complete example



```python
from shellev.shellev_client import ShellevClient
from shellev.exceptions.o_auth_provider_exception import OAuthProviderException

from shellev.exceptions.api_exception import APIException

client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    )
)
# function for storing token to database
def save_token_to_database(o_auth_token):
    # code to save the token to database
    pass

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(o_auth_token=previous_token)
    config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
    client = ShellevClient(config)
else:
    # obtain new access token
    try:
        token = client.bearer_auth.fetch_token()
        save_token_to_database(token)
        client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(o_auth_token=token)
        config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
        client = ShellevClient(config)
    except OAuthProviderException as ex:
        # handle exception
        pass
    except APIException as ex:
        # handle exception
        pass

# the client is now authorized and you can use controllers to make endpoint calls
```


