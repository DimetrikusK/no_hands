import datetime
import os
from colorama import init,Fore

init(autoreset=True)
begin_time = datetime.datetime.now()


os.system('py chrome.py')
print(Fore.GREEN + "%-20s" % "Chrome32 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py chrome_64.py')
print(Fore.GREEN + "%-20s" % "Chrome64 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py ie.py')
print(Fore.GREEN + "%-20s" % "IE32 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py ie64.py')
print(Fore.GREEN + "%-20s" % "IE64 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py edge32.py')
print(Fore.GREEN + "%-20s" % "Edge32 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py edge64.py')
print(Fore.GREEN + "%-20s" % "Edge64 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))
os.system('py firefox64.py')
print(Fore.GREEN + "%-20s" % "Firefox64 Done!", Fore.CYAN + " Total Time: " + str(datetime.datetime.now() - begin_time))

print(Fore.YELLOW + """Не забудь запустить скрипт в папке Firefox32.
Надо перейти в папку 'cd Firefox32', 'py firefox32.py', он допишет в отчет.

На данный момент полностью не протестирован IE.
В местах, где надо игнорировать безопасность, надо проверить руками.""")

os.system('py kek.py')