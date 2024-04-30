import os
import datetime
import sys
import tkinter as tk
import shutil
from tkinter import filedialog


title = """ 
          _____                    _____                   _______                   _____                    _____          
         /\    \                  /\    \                 /::\    \                 /\    \                  /\    \         
        /::\    \                /::\    \               /::::\    \               /::\____\                /::\    \        
       /::::\    \              /::::\    \             /::::::\    \             /:::/    /               /::::\    \       
      /::::::\    \            /::::::\    \           /::::::::\    \           /:::/    /               /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/    /               /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \     /:::/    /               /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   /:::/    /      _____    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /:::/____/      /\    \  /:::/\:::\   \:::\____\ 
/:::/____/  ___\:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    ||:::|    /      /::\____\/:::/  \:::\   \:::|    |
\:::\    \ /\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / |:::|____\     /:::/    /\::/    \:::\  /:::|____|
 \:::\    /::\ \::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /   \:::\    \   /:::/    /  \/_____/\:::\/:::/    / 
  \:::\   \:::\ \/____/         |:::::::::/    /     \:::\    /:::/    /     \:::\    \ /:::/    /            \::::::/    /  
   \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /       \:::\    /:::/    /              \::::/    /   
    \:::\  /:::/    /           |::| \::/____/         \::::::::/    /         \:::\__/:::/    /                \::/____/    
     \:::\/:::/    /            |::|  ~|                \::::::/    /           \::::::::/    /                  ~~          
      \::::::/    /             |::|   |                 \::::/    /             \::::::/    /                               
       \::::/    /              \::|   |                  \::/____/               \::::/    /                                
        \::/____/                \:|   |                   ~~                      \::/____/                                 
                                  \|___|                                            ~~           

      ,----,                                                  
    .'   .' \                                                 
  ,----,'    |                                                
  |    :  .  ;                                                
  ;    |.'  /                                                 
  `----'/  ;                                                  
    /  ;  /                                                   
   ;  /  /-,                                                  
  /  /  /.`|                                                  
./__;      :                                                  
|   :    .'                                                   
;   | .'                                                      
`---'                                                         

"""
print(title)
while True:

    # Get user input
    user_input = input("Group_2_OS>")

    # Split user input into command and arguments
    command_args = user_input.split()

    # Execute command
    command = command_args[0]

    if command == "ls":
        # List files in current directory
        print(os.listdir(os.getcwd()))

    elif command == "cd":
        # Change directory path
        def change_directory(directory_path):
            os.chdir(directory_path)

        if __name__ == "__main__":
            directory_path = input("Enter the path to the directory you want to change to: ")
            if os.path.exists(directory_path):
                print(f"Changed directory to: {directory_path}")
                change_directory(directory_path)
            else:
                    print(f"Error: Directory {directory_path} does not exist.")

    elif command == "help":
        print("ls              Display list files in current directory.")
        print("cd              Change the current directory path.")
        print("help            Provides Help information for Windows commands.")
        print("disd            Displays the name of or changes the current directory.")
        print("backd           Go back the Directory path.")
        print("folder          Create a new folder.")
        print("editF           Edit the folder name.")
        print("deleteF         Delete a folder.")
        print("create          Create a new file.")
        print("delete          Delete a file.")
        print("view            View the content of the file.")
        print("date            Display the current date.")
        print("edit            Edit the file.")
        print("rename          Edit the name of the file.")
        print("exit            Quits the CMD.EXE program (command interpreter).")
    elif command =="disd":
        #Display the current Directory path
        def display_directory():
            print(os.getcwd())
        if __name__ == "__main__":
            display_directory()
    elif command == "backd":
        def go_back_directory():
        #Go back the Directory path
            os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
        if __name__ == "__main__":
         go_back_directory()
    elif command == "folder":
        #Create new folder
        folder_name = input("Enter name of Folder: ")

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder {folder_name} created successfully.")
        else:
            print(f"Error: Folder {folder_name} already exists.")
    elif command == "editF":
        # edit folder name
        def edit_folder_name(): 
            current_folder_path = os.getcwd()
            print(f"Current Directory: {current_folder_path}")
            
            folder_to_rename = input("Enter the name of the folder you want to rename: ")
            new_folder_name = input("Enter the new name for the folder: ")

            if os.path.exists(folder_to_rename):
                try: 
                    os.rename(folder_to_rename, new_folder_name)
                    print(f"Folder '{folder_to_rename}' renamed to '{new_folder_name}' successfully.")
                except OSError as e:
                    print(f"Error: Renaming failed. {e}")
            else: 
                print(f"Error: Folder '{folder_to_rename}' does not exist.")
        if __name__ == "__main__":
            edit_folder_name()
    elif command == "deleteF":
        def delete_folder():
            folder_name = input("Enter the name of the folder you want to delete: ")

            if os.path.exists(folder_name):
                try: 
                    os.rmdir(folder_name)
                    print(f"Folder '{folder_name}' deleted successfully.")
                except OSError as e:
                    print(f"Error: Deletion of folder '{folder_name}' failed. {e}")
            else: 
                print(f"Error: Folder '{folder_name}' does not exist.")
        if __name__ == "__main__":
            delete_folder()

    elif command == "cat":
        # Print contents of file
        try:
            with open(command_args[1]) as file:
                print(file.read())
        except IndexError:
            print("cat: missing operand")
        except FileNotFoundError:
            print(f"cat: {command_args[1]}: No such file or directory")
    elif command == "create":
        #Create a file
        def create_file():
            filename = input("Enter the name of the file to create: ")
            with open(filename, 'w') as file:
                file.write("This is the content of the file.")
            print(f"{filename} has been created successfully.")
        if __name__ == "__main__":
            create_file()
    elif command =="select":
        #select File
        def select_file():
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            print(f"You selected: {file_path}")
        if __name__ == "__main__":
            select_file()
    elif command =="delete":
        #delete File
        def delete_file():
            filename = input("Enter the name of the file to delete: ")
            if os.path.exists(filename):
                os.remove(filename)
                print(f"{filename} has been deleted successfully.")
            else:
                print(f"{filename} does not exist.")
        if __name__ == "__main__":
            delete_file()
    elif command =="view":
        #View File
        def view_file():
            filename = input("Enter the name of the file to view: ")
            try:
                with open(filename, 'r') as file:
                    contents = file.read()
                    print(f"The contents of {filename} are:\n{contents}")
            except FileNotFoundError:
                print(f"{filename} does not exist.")
        if __name__ == "__main__":
            view_file()
    elif command =="date":
        #dispaly the current date
        def display_date():
            today = datetime.date.today()
            print(f"Today's date is {today}")
        if __name__ == "__main__":
            display_date()
    elif command == "copy":
        #Copy File Program
        def copy_file():
            src_file = input("Enter name of the file to copy: ")
            dest_file = input("Enter the path of the destination file: ")
            shutil.copy(src_file, dest_file)
            print(f"{src_file} has been copied to {dest_file}")
        if __name__ == "__main__":
            copy_file()
    elif command == "move":
        #Move File Program
        def move_file():
            file_path = input("Enter name of the file to move: ")
            if os.path.exists(file_path):
                dest_file = input("Enter the path of the destination file: ")
                shutil.move(file_path, dest_file)
                print(f"{file_path} has been moved to {dest_file}")
            else:
                print(f"Error: File {file_path} does not exist.")


        if __name__ == "__main__":
            move_file()
    elif command =="rename":
        #Rename the File
        def rename_file(file_path, new_name):
            os.rename(file_path, new_name)

        if __name__ == "__main__":
            file_path = input("Enter the old file name: ")
            if os.path.exists(file_path):
                new_name = input("Enter the new file name: ")
                rename_file(file_path, new_name)
            else:
                print(f"Error: File {file_path} does not exist.")
    elif command =="clear":
        #Clear the console
        def clear_console():
            os.system('cls' if os.name=='nt' else 'clear')

        if __name__ == "__main__":
            clear_console()
    elif command =="edit":
        def edit_file(file_path):
            with open(file_path, 'r+') as file:
                file_content = input("Enter a characters: ")
                # Modify the file content as desired
                file.seek(0)
                file.write(file_content)
                file.truncate()

        if __name__ == "__main__":
            file_path = input("Enter the path to the file you want to edit: ")
            if os.path.exists(file_path):
                edit_file(file_path)
            else:
                # File doesn't exist, so write an error message to the console
                print(f"Error: File {file_path} does not exist.")
    elif command == "open":
        #Open the File
        def open_file(file_path):
            os.startfile(file_path)

        if __name__ == "__main__":
            file_path = input("Enter the path to the text file you want to open: ")
            if os.path.exists(file_path):
                open_file(file_path)
            else:
                # File doesn't exist, so write an error message to the console
                print(f"Error: File {file_path} does not exist.")

    elif command == "exit":
        # Exit program
        sys.exit()

    else:
        # Handle invalid command
        print(f"{command}: command not found")
