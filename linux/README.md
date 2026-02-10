### ISSUE
#### mdadm: No arrays found ...
mdadm: No arrays found in config file or automatically

```bash
update-initramfs -u
```

### Schedule Shutdown

#### Shutdown after `n` minutes
 To shutdow System at 45 mins later:
```bash
sudo shutdown -P +45
```
#### Shutdown at specific time
To shutdown at 1 AM:
```bash
sudo shutdown -P 1:00
```

#### shutdown now
```bash
sudo shutdown -P now
```

##### Note
A message is broadcast to all terminals to warn about the shutdown.

### Cancel a pending shutdown
After, starting a shutdown, if the time argument is not "+0" or "now", you can use:
```bash
sudo shutdown -c 
```

### List Schedulled shutdowns
```bash
date --date @$(head -1 /run/systemd/shutdown/scheduled |cut -c6-15)
```
