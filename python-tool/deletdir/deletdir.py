import shutil as st
print('Please make sure you '
      'are in the folder which contains the directory you '
      'want to delete')
dele_dir = input('please input the directory you wnat to delete: ')
st.rmtree(dele_dir)