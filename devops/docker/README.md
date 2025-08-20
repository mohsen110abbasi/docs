## Remove multiple Docker Volumes
To remove multiple volumes:
```
docker volume ls -q | grep '^stage_' | xargs docker volume rm
```
