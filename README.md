## Brute_pass
_How long your computer takes to find out a password ?_
```    ____             __                                  
   / __ )_______  __/ /____        ____  ____ ___________
  / __  / ___/ / / / __/ _ \      / __ \/ __ `/ ___/ ___/
 / /_/ / /  / /_/ / /_/  __/     / /_/ / /_/ (__  |__  ) 
/_____/_/   \__,_/\__/\___/_____/ .___/\__,_/____/____/  
                         /_____/_/                       
```

### SUMMARY
Brute_pass uses brute force computing to find out any password; the time to find it out will depend on your computer power. 

### FEATURES
The chosen password can be composed of:

| PASSWORD         |       YES       |       NO      |
|:-----------------|:---------------:| -------------:|
| letters_min_MAJ  |        V        |               |
| digits           |        V        |               |
| special_char     |        V        |               |

There is no limit for the password length but WATCH OUT, it might take an eternity according to your computer power.

### SCREENSHOTS
**_Script launched in Visual Studio Code_** 

![Screenshot](https://github.com/gelndjj/Brute_pass/blob/main/img/screen1.png)

**_Script launched in Terminal_ **

![Screenshot](https://github.com/gelndjj/Brute_pass/blob/main/img/screen2.png)

**_Log file you get once the password has been found out_ **

![Screenshot](https://github.com/gelndjj/Brute_pass/blob/main/img/screen3.png)

**_Log file keeping a history of what you looked for_**
![Screenshot](https://github.com/gelndjj/Brute_pass/blob/main/img/screen4.png)


### HOW IT WORKS - CLI
* Double click on the program.
* A window shows up asking to type a password.
* Once typed, the program attempts to find out the password.
* The program gets started again indefinitely till you either close it or type Ctrl + C
* Once finished, you'll be shown how long it took to find out the password, how many combinations have been analyzed.
* These informations will be saved automatically into a log file called "results_log.txt". It will be located where the program is.
* The log file will keeep informations even if the program is closed and started again.

### WHAT IF... you type a password that takes hours,  weeks, months or maybe more to be found out.
* Close the soft by pressing Ctrl + C after having seen how long it might take to find out the password.

### REQUIREMENTS
Librairies require to run Brute_pass.py

```
pip3 install tqdm
pip3 install itertools
pip3 install datetime

```
