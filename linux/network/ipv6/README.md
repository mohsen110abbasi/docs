To Disable IP v6:

اول دستورات زیر را بزنید:

```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```

خوب دستور زیر را بزنید تا باز شود:

```bash
nano /etc/sysctl.conf
```

داخل آن کد های زیر را قرار دهید و ctrl+x و y را بزنید تا ذخیره شود:

```bash
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1
```

برای اعمال تغییرات دستور زیر را بزنید:

```bash
sudo sysctl -p
```

باید فایل /etc/rc.local را (با دسترسی روت) ایجاد کنید:

```bash
nano /etc/rc.local
```

و آن را با موارد زیر پر کنید:

```bash
#!/bin/bash
# /etc/rc.local
/etc/sysctl.d
/etc/init.d/procps restart
exit 0
```

حالا از دستور chmod برای اجرایی کردن فایل استفاده کنید:

```bash
sudo chmod 755 /etc/rc.local
```
تمام حالا در صورت ریستارت شدن سرور هم تغییرات ذخیره خواهند ماند.

یرای فعال کردن مجدد ipv6 کافیست برعکس مراحل زیر را انجام دهید یعنی آن سه خط کد را از فایل sysctl.conf حذف کنید.

