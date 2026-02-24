### SSL Cert
#### DNS Challenge
To issue SSL cert of a domain:

```bash
docker run -it -v $PWD/volumes/certbot:/etc/letsencrypt --rm certbot/certbot certonly --manual --preferred-challenges=dns --email <your-email-address> --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.example.ir -d example.ir
```

#### HTTP Challenge
In Nginx reverse proxy:
```bash
server {
.........
...
............
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
..........
....
.............
}
```

After it, do:
```bash
docker run -it --rm   -v /root/certbot/volumes/letsencrypt:/etc/letsencrypt   -v /var/www/certbot:/var/www/certbot   repo.ghadirhub.ir/docker/certbot/certbot certonly   --webroot   -w /var/www/certbot   --email <your-email-address>  --agree-tos -d example.ir   --staging   --debug-challenges   --preferred-challenges http-01   --http-01-port 80 -v
```

### Important Note:
```bash
fullchain.pem = cert.pem + chain.pem
```


Let's Encrypt client and ACME library written in Go.

   https://go-acme.github.io/lego/usage/cli/obtain-a-certificate/index.html

   https://github.com/go-acme/lego
