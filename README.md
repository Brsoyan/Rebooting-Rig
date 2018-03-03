# Rebooting-Rig
Script for rebooting pc, when hashrate is low for all pools in nanopool.


First we need [python 3](https://www.python.org)

This script work for all pools in nanopool `ETH`, `ETC`, `SIA`, `ZEC`, `XMR`, `PASC`, `ETN`.
Change url with your hash rate history url. More info https://etc.nanopool.org/api#api-Miner-HashrateHistory.

Also install [sched](https://github.com/dbader/schedule) and [requests](http://docs.python-requests.org/en/master/)

Last step add this script in startup.

__ Windows __
To add or remove an app from the Startup tab, press the Windows Logo Key + R, type shell:startup, and then select OK. This opens the Startup folder. Select Start. Find the app you're looking to add or remove, and press and hold (or right-click) it. Select More > Open File Location. In the file location folder, press and hold (or right-click) the app and select Copy. Paste the shortcut to your app into the Startup folder to have it run at startup.

__ Linux __
Please check link how add script in startup for [Linux](https://stackoverflow.com/questions/12973777/how-to-run-a-shell-script-at-startup)
