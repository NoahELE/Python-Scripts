import os
import threading

import requests
from lxml import etree

from PIL import Image


def is_valid_image(image_path):
    try:
       Image.open(image_path).verify()
       return True
    except:
       return False


def get_image_urls(url):
    image_urls = []
    r = requests.get(url, proxies=proxies)
    if r.status_code != 200:
        print("Failed")
        return

    html = etree.HTML(r.text)

    page_number = int(html.xpath(
        "/html/body/div[1]/div/div/main/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/text()")[0][:-1])

    for i in range(page_number):
        path = str(html.xpath(
            "/html/body/div[1]/div/div/main/div[2]/div/div[5]/noscript["+str(i+1)+"]/img//@src")[0])
        image_urls.append(path)

    print(image_urls)
    return image_urls


def get_image(image_url):
    index = int(image_url.split("/")[-1].split(".")[0])

    print("Started...", image_url)
    r = requests.get(image_url, proxies=proxies)
    if r.status_code != 200:
        ext = str(image_url.split("/")[-1].split(".")[1])
        if ext == "png":
            print("Failed to get png, try jpg")
            r = requests.get(image_url[:-3]+"jpg")
        elif ext == "jpg":
            print("Failed to get jpg, try png")
            r = requests.get(image_url[:-3]+"png")
    target = os.path.join(".\\"+title, image_url.split("/")[-1])
    with open(target, "wb") as f:
        f.write(r.content)
    if is_valid_image(target):
        print("Picture "+str(index)+" Finished...")
    else:
        get_image(image_url)


url = input("Input the URL: ")

proxies = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}
r = requests.get(url, proxies=proxies)
html = etree.HTML(r.text)
title = str(html.xpath(
    "/html/body/div[1]/div/div/main/div[2]/div/h1/text()")[0])
target = os.path.join(os.path.abspath("."), title)
if not os.path.isdir(target):
    os.mkdir(target)

image_urls = get_image_urls(url)
print(image_urls)

thread_pool = []
for i in image_urls:
    t = threading.Thread(target=get_image, args=(i,))
    thread_pool.append(t)
    t.start()

for t in thread_pool:
    t.join()

print("All Finished...")

'''
urls_to_download = [
    "https://zh.erocool.co/detail/1164224o219234.html",
    "https://zh.erocool.co/detail/1271332o242889.html",
    "https://zh.erocool.co/detail/1270851o242750.html",
    "https://zh.erocool.co/detail/1343216o259128.html",
    "https://zh.erocool.co/detail/1406370o270513.html",
    "https://zh.erocool.co/detail/1544096o295660.html"
]
'''