# DELET DIRECTORY is the purpose of this script
# Author: Y.-W. FANG
# Date: 18th Jan. 2018 created
# Linux shell is quite slow in some clusters when deleting directory
# containing thouansands of files, that's why I use python.
import shutil as st
import time
start_time = time.time()
print('Please make sure you '
      'are in the folder which contains the directory you '
      'want to delete')
dele_dir = input('please input the directory you wnat to delete: ')
st.rmtree(dele_dir)
print("--- %s seconds ---" % (time.time() - start_time))
