# Rebooting-Rig
Script for rebooting pc, when hashrate is low for all pools in nanopool.


First we need [python 3](https://www.python.org)

This script work for all pools in nanopool `ETH`, `ETC`, `SIA`, `ZEC`, `XMR`, `PASC`, `ETN`.
Put your account in `zec_account` or `etc_account` etc..

Also install [sched](https://github.com/dbader/schedule) and [requests](http://docs.python-requests.org/en/master/)

Last step add this script in startup.

__Windows__

To add or remove an app from the Startup tab, press the Windows Logo Key + R, type shell:startup, and then select OK. This opens the Startup folder. Select Start. Find the app you're looking to add or remove, and press and hold (or right-click) it. Select More > Open File Location. In the file location folder, press and hold (or right-click) the app and select Copy. Paste the shortcut to your app into the Startup folder to have it run at startup.

Also windows user can use [Batch file](https://en.wikipedia.org/wiki/Batch_file) file for runing script.
```python C:\PATH-TO-SCRIPT\reboot-ZEC.py```

__Linux__

Please check link how add script in startup for [Linux](https://stackoverflow.com/questions/12973777/how-to-run-a-shell-script-at-startup)
