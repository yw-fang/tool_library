#DELET DIRECTORY is the purpose of this script
#Author: Y.-W. FANG
#Date: 18th Jan. 2018 creted
# I found linux shell is quite slow in some cluster when deleting directory cotnaining thouansands of files, that's why use this alternative way by python
import shutil as st
print('Please make sure you '
      'are in the folder which contains the directory you '
      'want to delete')
dele_dir = input('please input the directory you wnat to delete: ')
st.rmtree(dele_dir)
