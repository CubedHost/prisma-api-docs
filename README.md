# Prisma API
Prisma is a unified game server management suite developed by CubedHost to provide unparalleled control over and insight into your game servers. Through the public REST API, you can easily interact with and control your servers from anywhere within any application or script.

Client libraries will also be made available for JS/Node and other languages.

## Authentication
All API calls must be authenticated using a valid API key. Passing your key to the API is as simple as including it in an `X-API-KEY` header with all requests. In addition, you'll also need to include your Prisma account email address via the `X-API-USER` header.

### Example
```
POST /server/1234/restart
Content-Type: application/json
X-Api-Key: <key>
X-Api-User: justin@cubedhost.com
```

## Endpoints
Base API URL: `https://prisma.cubedhost.com/api/`

| Path                     | Method | Description | Request Body
| :----------------------- | :----: | :---------: | :-----
| /user                    | GET    | Get your user account
| /user                    | POST   | Update your user account
| /user/profile            | GET    | Get your user profile
| /user/profile            | POST   | Update your user profile
| /servers                 | GET    | List all of your servers
| /server/:id              | GET    | Get server config
| /server/:id              | POST   | Update server config
| /server/:id/start        | POST   | Start server
| /server/:id/stop         | POST   | Stop server
| /server/:id/restart      | POST   | Restart server
| /server/:id/users        | GET    | List users with access to server
| /server/:id/users        | PUT    | Give user access to server
| /server/:id/users/:email | DELETE | Remove user's access to server
| /server/:id/type         | POST   | Change server type
| /server/:id/database     | GET    | Get server's database info
| /server/:id/database     | PUT    | Create server's database
| /server/:id/database     | DELETE | Delete server's database
| /server/:id/console      | POST   | Send console command | `{ "command": "example" }`
| /server/:id/players      | GET    | Get all players

## Examples
You can find sample code under the `examples` folder of this repo.
