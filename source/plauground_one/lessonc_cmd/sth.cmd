@echo off
echo My comment.

if exist %CD%\..\some_file_in_parent_folder.txt (
    echo First file exists.
)

if not exist %CD%\..\some_file_NOT_in_parent_folder.txt (
	echo Second file doesn't exist.
) 


pause
