### Rename a Branch

###### Branches
```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```


#### Rename Local Branch
```bash
git branch -m master main
```

###### Branches
```
* main
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```


#### Rename Remote Branch
Remotely Create new branch:
```bash
git push origin --set-upstream main
```

###### Branches
```
* main
  remotes/origin/HEAD -> origin/master
  remotes/origin/main
  remotes/origin/master
```


Delete old remote one!
```bash
git push origin --delete master
```

###### Branches:
```
* main
  remotes/origin/main
```
