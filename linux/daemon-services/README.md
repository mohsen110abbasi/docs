### SystemCtl inotify watch limit reached
If the restart command below:
```bash
systemctl restart <service>
```

HAS an error like:
```bash
Failed to add a watch for /run/systemd/ask-password: inotify watch limit reached
```

So in order to temporarily increase the limit:

```bash
sysctl fs.inotify.max_user_watches=524288
systemctl daemon-reexec
```
