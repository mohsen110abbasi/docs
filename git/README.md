### Rename a Branch
#### Rename Local Branch
```bash
git branch -m master main
```

#### Rename Remote Branch
Remotely Create new branch and then Delete old one!
```bash
git push origin --set-upstream main
git push origin --delete master
```