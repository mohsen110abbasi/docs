```bash
rsync           -ahW       --inplace         --progress      $src       $dst 

rsync           -avhW     --inplace         --progress       --ignore-missing-args     --no-compress          $src            $dst 
```

### How to exclude a directory
```bash
nohup rsync --timeout=48000 --exclude=/minio/.minio.sys/ -azvP  ./minio root@<remote-ip>:/root/minio-storage/file/ >> ./rsync.log &
```

### Avoid broken pipe error
#### Exclude
```bash
rsync -e "ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=30" --timeout=48000 --exclude=/minio/.minio.sys/ -azhvPW --inplace  --progress  ./minio root@<remote-IP>:/root/minio-storage/minio-sina-backup/
rsync  -azhvPW --inplace  --progress dir1 dir2
```

#### Without Exclude
```bash
rsync -e "ssh -p 22 -o StrictHostKeyChecking=no -o ServerAliveInterval=30" --timeout=48000 -azhvPW --inplace  --progress dir1 dir2
```


### Force rsync not see on timestamp but lookup only file sizes
```bash
rsync -vrtP --size-only --progress -rsh=ssh ./bitbucket root@5.5.5.5:/volume/
```
