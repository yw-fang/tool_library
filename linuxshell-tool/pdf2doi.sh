extract () {
  printf "%s" "$1"
  text=`pdftotext -f 1 -l 1 -raw "$2" - 2>/dev/null | grep '\<10\.'`
  echo $text | perl -pe 's@.*[ /:]10\.@10\.@ ; s@[ \t].*@@ ; s@[.,;]$@@'
}


if [ $# -eq 1 ]; then
  extract "" "$1"
else
  for i in "$@" ; do
    extract "$i: " "$i"
  done
fi
