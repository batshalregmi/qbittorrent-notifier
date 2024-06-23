# qbittorrent-notifier

This project is a simple notification tool for qBittorrent. It sends notifications to [Pushover](https://pushover.net/) whenever a torrent download completes or is added. 

## Installation

1. Download qbittorrent_notifier.py from the repo.
2. Edit the variables at the top of the file to your pushover user key and application key.
3. In qBittorrent, go to Tools > Options > Downloads and check one or both of the boxes under "Run external program on torrent completion". Enter the path to the qbittorrent_notifier.py file and whatever other arguments you want. For example, inputting: ``python "location_to_your_file\qbittorrent_notifier.py" "Torrent: %N has finished downloading."`` would send a notification like "Torrent: archlinux-2024.06.01-x86_64.iso has finished downloading."
