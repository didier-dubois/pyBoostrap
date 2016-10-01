# pyBootstrap
## Introduction
This a  very simple web app template allowing you to start developping Python web based applications quickly!

## Dependencies
 * web.py
 * pygal
 * Bootstrap.js
 * jQuery

## How to 
You can test your application, by running the `./runserver.sh` application and develop locally. The beauty of Web.py is that you can edit your pages, python files and just reload the Web pag. The change is taken automatically. This allows for a fast developpment cycle.

In order to run your application permanently, you can add a new user and launch the server at startup.
```bash
# ---- User creation and code checkout
$ sudo useradd -m pybo
$ sudo su - pybo
$ git clone https://github.com/didier-dubois/pyBoostrap.git

# ---- Start at reboot and let root receive notifications 
$ echo '@reboot   /home/pybo/pyBoostrap/runserver.sh'  > crontab
$ crontab crontab 
$ echo root > .forward

# ---- Removing your user from the login prompt (Ubuntu)
$ sudo echo '[User] >   /var/lib/AccountsService/users/pybo
$ sudo echo 'SystemAccount=true' >> /var/lib/AccountsService/users/pybo

```

## Contact
python at didier-dubois.ch. [Homepage](http://didier-dubois.ch)


# License
See [Licence](LICENSE.md)
