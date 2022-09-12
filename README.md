# ENotify

Simple package to make notification on compilation end via telegram bot

## Problem

Some operations like building cpp projects may take some time. It may be tidious to wait until completion sitting behind monitor.   
With this untility you can switch to other things and be informed right in time when command ends. 

## Installation
```
git clone https://github.com/D-Tretyakov/compilation_notifier.git
cd compilation_notifier
python setup.py install
```
or
```
pip install git+https://github.com/D-Tretyakov/compilation_notifier.git
```

## Usage
To use this utility just add `enotify` at the end of main command with ; (or & on Windows)

For example:
```
cmake . ; enotify
```

After execution of cmake the next command will be executed that will trigger bot to send message

## Setup
To use enotify you need to [create telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)  
Then run:
```
enotify -t YOUR_TOKEN
```
If you don't know your telegram id you can get it with:
```
enotify -g @your_user_name
```
Alternatively
```
enotify -i YOUR_ID
```
Anfter these steps enotify is ready to use.