#########################################################################
# AUTHOR NAME   : R.K.Rao Chigurupati
# CREATION DATE : Wednesday, 09-DEC-2020
# Copying ALL the required Project Files into Run_Folder
# C:\rkBuildCompile\calculator_repo\run_folder
# To Build & Compile them
#
#########################################################################

if not exist "C:\rkBuildCompile\calculator\run_folder" mkdir C:\rkBuildCompile\calculator\run_folder

copy C:\rkGits\PythonPractice\calculator_repo\libs\* C:\rkBuildCompile\calculator\run_folder
copy C:\rkGits\PythonPractice\calculator_repo\src\* C:\rkBuildCompile\calculator\run_folder

python C:\rkBuildCompile\calculator\run_folder\main.py
