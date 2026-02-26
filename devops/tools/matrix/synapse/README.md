## Admin API

### Turn Server
Get ACCESS TOKEN:

```bash
curl -X POST https://matrix.sample.ir/_matrix/client/v3/login   -H "Content-Type: application/json"   -d '{"type": "m.login.password", "identifier": {"type": "m.id.user", "user": "admin"}, "password": "ADMIN_PASS"}'
```

Get Turn Server config by ACCESS TOKEN above:

```bash
curl https://matrix.managap.ir/_matrix/client/v3/voip/turnServer   -H "Authorization: Bearer ACCESS_TOKEN"
```
