### SSL Cert
To issue SSL cert of a domain:

```bash
docker run -it -v $PWD/volumes/certbot:/etc/letsencrypt --rm certbot/certbot certonly --manual --preferred-challenges=dns --email <your-email-address> --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.example.ir -d example.ir
```

### Important Note:
```bash
fullchain.pem = cert.pem + chain.pem
```


Let's Encrypt client and ACME library written in Go.

   https://go-acme.github.io/lego/usage/cli/obtain-a-certificate/index.html

   https://github.com/go-acme/lego
