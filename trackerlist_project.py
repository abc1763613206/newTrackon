from time import sleep

import requests

import trackon


def main():
    while True:
        tlist = requests.get(
            "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt"
        )
        trackon.enqueue_new_trackers(tlist.text)
        sleep(86400)
