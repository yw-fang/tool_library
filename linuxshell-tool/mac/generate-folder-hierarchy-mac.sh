find ~/. -print | sed -e 's;[^/]*/;|--->;g;s;--->|; |;g' > ~/hierarchy.txt
