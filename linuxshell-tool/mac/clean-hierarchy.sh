# This shell remove some lines containing specifc
# patterns for the higrarchy.txt generated by generate-folder-hierarchy-mac.sh
# For Mac OS
sed -i '' '/.html/d' ./hierarchy.txt
sed -i '' '/.pdf/d' ./hierarchy.txt
sed -i '' '/.en.srt/d' ./hierarchy.txt
sed -i '' '/.en.txt/d' ./hierarchy.txt

# For Linux
# sed -i '/.pdf/d' hierarchy.txt
# sed -i '/.en.srt/d' hierarchy.txt
# sed -i '/.en.txt/d' hierarchy.txt
