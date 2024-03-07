#ref: https://forums.linuxmint.com/viewtopic.php?t=338648
# purpose: clean the / folder in linux mint
sudo apt autoclean
sudo apt autoremove --purge
sudo find /tmp -type f -delete
dpkg -l | grep '^rc' | awk '{print $2}' | sudo xargs dpkg --purge
rm -v -f ~/.cache/thumbnails/*/*.png ~/.thumbnails/*/*.png
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s


