### View cert info

```bash
openssl x509 -in ./ssl_cert.crt -noout -text
```
### Generate SSL Certs
```bash
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -subj "/C=CN/ST=GD/L=SZ/O=Acme, Inc./CN=Acme Root CA" -out ca.crt
openssl req -newkey rsa:2048 -nodes -keyout priv.key -subj "/C=CN/ST=GD/L=SZ/O=Acme, Inc./CN=*.example.com" -out cert.crt
openssl x509 -req -extfile <(printf "subjectAltName=DNS:example.com,DNS:www.example.com,DNS:*.example.com") -days 365 -in cert.crt -CA ca.crt -CAkey ca.key -CAcreateserial -out cert.crt
```

Then In Nginx config, locate `ssl_certificate` & `ssl_certificate_key` as below:
```bash
server {
    listen 80;
    listen [::]:80;
    server_name erp.example.com;

    location / {
        return 301 https://$host$request_uri;
    }
}

upstream erpcom {
  server 127.0.0.1:8069;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;

    server_name erp.example.com;

    ssl_certificate /var/www/certs/ssl/example.com/cert.crt;
    ssl_certificate_key /var/www/certs/ssl/example.com/priv.key;

    location / {
      proxy_pass http://erpcom;
    }


}

```
