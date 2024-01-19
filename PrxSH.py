import os
import subprocess
import shutil
from colorama import init, Fore
import socket
import random
import requests
from requests.structures import CaseInsensitiveDict
from clint.textui import progress
import fnmatch
import glob
from bs4 import BeautifulSoup as bs
import platform

from urllib.request import urlopen
import re as r
import json

# IP address to test

def getIP():
    d = str(urlopen('http://checkip.dyndns.com/')
            .read())
 
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

# IP address to test



init()
os.system("title PrxSH")
os.system("cls")
print(f"""
{Fore.RED}||======||                 {Fore.BLUE}   ||==========||  ||             ||
{Fore.RED}||      ||                 {Fore.BLUE}   ||              ||             ||
{Fore.RED}||======|| ||  //          {Fore.BLUE}   ||              ||             ||
{Fore.RED}||         || //  \\\    // {Fore.BLUE}   ||              ||             ||
{Fore.RED}||         ||//    \\\  //  {Fore.BLUE}   ||==========||  ||====PrxSH====|| 
{Fore.RED}||         ||/      \\\//   {Fore.BLUE}               ||  ||             ||
{Fore.RED}||         ||       //\\\   {Fore.BLUE}               ||  ||             ||
{Fore.RED}||         ||      //  \\\  {Fore.BLUE}               ||  ||             ||
{Fore.RED}||         ||     //    \\\ {Fore.BLUE}   ||==========||  ||             ||
""")
print("\n")
print("\n")
print(f"{Fore.BLUE}[Version] {Fore.GREEN}1.0.0")
path, filename = os.path.split(os.getcwd())
print(f"{Fore.BLUE}[Working Path] {Fore.GREEN}{path}")
print(f"{Fore.BLUE}[Working Directory] {Fore.GREEN}{filename}")
im = os.getlogin()
print(f"{Fore.BLUE}[User] {Fore.GREEN}{im}")
print(f"{Fore.BLUE}[OS] {Fore.GREEN}{platform.system()} {platform.release()}")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"{Fore.BLUE}[Computer IP Address] {Fore.GREEN}{ip_address}")
print(f"{Fore.BLUE}[Router IP Address] {Fore.GREEN}{getIP()}")
print("")
while 1:
    me = os.getlogin()
    path, filename = os.path.split(os.getcwd())
    prx = input(f"{Fore.RED}({me} PrxSH)-{Fore.BLUE}[~/{filename}]{Fore.GREEN}-$ ")
    def pingf(url):
        os.system("ping {}".format(url))
    def helpf():
        print("""
                help    show this page
                ping    ping a website
                cd      change a directory
                whereami    help you to know your exact location in your computer
                clear   clear all terminal texts
                whoami  help you to know your exact account & computer
                mkdir   create a directory
                rmdir   remove a directory
                ls      list all directories in your exact location
                start   start a file
                echo    echo a command/text
                prx localhost    create a localhost with a optional port
                ipconfig    the information about your network
                prx myip    know your exact host & IP address
                prx crawl   basic crawl of a website
                shell   write a command in your machine main Terminal
                locate  locate a file
                prx geoip   find the location of an ip address
                prx connect@    connect to a exact website and scrap information & data from the website
            """)
    def exitf():
        exit() 
    try:
        if prx == "help":
            helpf()
        if prx.startswith("prx geoip"):
            try:
                jn = prx.split(" ")
                request_url = 'https://geolocation-db.com/jsonp/' + jn[2]
                response = requests.get(request_url)
                result = response.content.decode()
                result = result.split("(")[1].strip(")")
                result  = json.loads(result)
                print(result)
            except:
                jn = input("IP ADDRESS ==>> ")
                request_url = 'https://geolocation-db.com/jsonp/' + jn
                response = requests.get(request_url)
                result = response.content.decode()
                result = result.split("(")[1].strip(")")
                result  = json.loads(result)
                print(result)
        if prx.startswith("ping") == True:
            try:
                urli = prx.split(" ")
                pingf(urli[1])
            except:
                urli = input("URL/IP ==>> ")
                urli = str(urli)
                pingf(urli)
        if prx.startswith("cd") == True:
            try:
                path = prx.split(" ")
                os.chdir(path[1])
            except:
                path = input("PATH ==>> ")
                os.chdir(path)
        if prx == "whereami":
            print(os.getcwd())
        elif prx == "whoami":
            os.system("whoami")
        elif prx == "clear":
            os.system("cls")
        elif prx.startswith("mkdir") == True:
            try:
                name = prx.split(" ")
                os.mkdir(name[1])
                print(f"Folder Creates In {os.getcwd()} With Name {name[1]}")
            except:
                name = input("FOLDER NAME ==>> ")
                os.mkdir(name)
                print(f"Folder Creates In {os.getcwd()} With Name {name}")
        elif prx == "ls":
            for i in os.listdir():
                print(i)
        elif prx.startswith("start") == True:
            try:
                prog = prx.split(" ")
                os.system(f"start {prog[1]}")
            except:
                prog = input("FILE NAME ==>> ")
                os.system(f"start {prog}")
        elif prx.startswith("rmdir") == True:
            try:
                name = prx.split(" ")
                shutil.rmtree(name[1])
                print(f"Folder Deleted From {os.getcwd()} With Name {name[1]}")
            except:
                name = input("FOLDER/FILE NAME ==>> ")
                shutil.rmtree(name)
                print(f"Folder Deleted From {os.getcwd()} With Name {name[1]}")
        elif prx.startswith("echo") == True:
            try:
                prx = prx.replace("echo ", "")
                f = prx.split(" > ")
                os.system(f"echo {f[0]} > {f[1]}")
            except:
                path = prx.split(" ")
                print(path[1]) 
        elif prx.startswith("prx localhost") == True:
            try:
                srvr = prx.split(" ")
                os.system(f"python -m http.server {srvr[2]}")
            except:
                srvr = input("PORT ==>> ")
                os.system(f"python -m http.server {srvr}")
        elif prx.startswith("ipconfig") == True:
            try:
                r = prx.split(" ")
                os.system(f"ipconfig {r[1]}")
            except:
                os.system("ipconfig")
        elif prx == "prx myip":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Hostname: {hostname}")
            print(f"Computer IP Address: {ip_address}")
            print(f"Router IP Address: {getIP()}")
        elif prx.startswith("prx crawl") == True:
            try:
                url = prx.split(" ")
                resp = requests.get(url[1])
                if resp.status_code == 200:
                    path = f'Crawled {random.random()}.html'
                    with open(path, 'wb') as f:
                        total_length = int(resp.headers.get('content-length'))
                        for chunk in progress.bar(resp.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                            if chunk:
                                f.write(chunk)
                                f.flush()
            except:
                url = input("URL ==>> ")
                resp = requests.get(url)
                if resp.status_code == 200:
                    path = f'Crawled {random.random()}.html'
                    with open(path, 'wb') as f:
                        total_length = int(resp.headers.get('content-length'))
                        for chunk in progress.bar(resp.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                            if chunk:
                                f.write(chunk)
                                f.flush()
        elif prx == "shell":
            cmnd = input("COMMAND ==>> ")
            os.system(cmnd)
        elif prx.startswith("locate") == True:
            try:
                f = prx.split(" ")
                def find(pattern, path):
                    result = []
                    for root, dirs, files in os.walk(path):
                        for name in files:
                            if fnmatch.fnmatch(name, pattern):
                                result.append(os.path.join(root, name))
                    return result

                print(find(f'{f[1]}', f'{f[2]}'))
            except:
                f = input("FILENAME ==>> ")
                h = input("HARDDRIVE ==>> ")
                def find(pattern, path):
                    result = []
                    for root, dirs, files in os.walk(path):
                        for name in files:
                            if fnmatch.fnmatch(name, pattern):
                                result.append(os.path.join(root, name))
                    return result

                print(find(f, h))
        if prx.startswith("prx connect"):
            prx = prx.replace("prx connect@", "")
            page = requests.get(prx)
            html = page.content
            soup = bs(html, "html.parser")
            while 1:
                root = input(f"{Fore.RED}(PrxSH)-{Fore.BLUE}[URL/{prx}]{Fore.GREEN}-$ ")
                if root == "exit":
                    break
                if root == "":
                    pass
                if root == "do loop":
                    tag = input("TAG ==>> ")
                    tag = soup.find_all(tag)
                    sp = input("SPECIFIC ==>> ")
                    for fi in tag:
                        f = fi.get(sp)
                        print(f)
                if root == "find tag":
                    tag = input("TAG ==>> ")
                    tag = soup.find_all(tag)
                    for i in tag:
                        print(i)
                if root.startswith("prx dcrawl") == True:
                    url = root.split(" ")
                    resp = requests.get(f"{prx}/{url[1]}")
                    if resp.status_code == 200:
                        path = f'{url[1]}'
                        with open(path, 'wb') as f:
                            total_length = int(resp.headers.get('content-length'))
                            for chunk in progress.bar(resp.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                                if chunk:
                                    f.write(chunk)
                                    f.flush()
                if root == "download all":
                    try:
                        tag = input("TAG ==>> ")
                        tag = soup.find_all(tag)
                        sp = input("SPECIFIC ==>> ")
                        g = input("FORMAT ==>> ")
                        for fi in tag:
                            f = fi.get(sp)
                            print(f)
                            resp = requests.get(f"{prx}/{f}")
                            if resp.status_code == 200:
                                path = f'{random.random()}.{g}'
                                with open(path, 'wb') as f:
                                    total_length = int(resp.headers.get('content-length'))
                                    for chunk in progress.bar(resp.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                                        if chunk:
                                            f.write(chunk)
                                            f.flush()
                    except IndexError:
                        pass
                try:
                    b = "soup." + root
                    print(eval(b))
                except:
                    pass
                if root == "clear":
                    os.system("cls")
    except:
        print("Invalid Syntax")
    if prx == "exit":
        exitf()
