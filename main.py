from fun.user_terminal_interface import *
from fun.directory_analyser import *
from fun.file_renamer import *

list_original = get_files_in_directory('.')
list_modif = run_modules_on_list(list_original)
print(user_choice(list_modif, list_original))