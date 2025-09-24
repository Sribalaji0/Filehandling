import os

class Filehandler:
   
    def creating_file(self, filename):
        f = open(filename, "w")
        f.close()
        print(f"{filename} created successfully.")
       
    def write_file(self, filename, text):
        f = open(filename, "w")
        f.write(text)
        f.close()
        print("File overwritten successfull.")

    def append_file(self, filename, text):
        f = open(filename, "a")
        f.write("\n" + text)
        f.close()
        print("Text Appended successfull.")

    def read_file(self, filename):
        try:
            f = open(filename, "r")
            print("File Content")
            print(f.read())
            f.close()
        except Exception as e:
            print(" File not found!.. ",e)

    def replace_text(self, filename, old_text, new_text):
        try:
            f = open(filename, "r")
            data = f.read()
            f.close()
            data = data.replace(old_text, new_text)
            f = open(filename, "w")
            f.write(data)
            f.close()
            print("Content replaced.")
        except Exception as e:
            print("File not found!.. ",e)
            
    def get_cwd(self):
        print("Current working directory: ", os.getcwd())

    def change_directory(self, path):
        os.chdir(path)
        print("Directory changed to: ", os.getcwd())

    def rename_file(self, old_name, new_name):
        os.rename(old_name, new_name)
        print(f" {old_name} was changed to {new_name}")

    def delete_file(self, filename):
        try:
            os.unlink(filename)
            print("File was deleted successfully..")
        except Exception as e:
            print("File not found!.. ",e)

            
def main():
    fh = Filehandler()
    while True:
        print("\n----FILE HANDLING MENUS----")
        print("1. Creating a file")
        print("2. Write to a file")
        print("3. Append to a file")
        print("4. Read a file")
        print("5. Replace a text")
        print("6. Get Working Directory")
        print("7. Change Directory")
        print("8. Rename a file")
        print("9. Deleting a file")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except Exception as e:
            print("Invalid input. Please enter a number.",e)
            continue

        if choice == 1:
            name = input("Enter the file name: ")
            fh.creating_file(name)

        elif choice == 2:
            name = input("Enter the file name: ")
            text = input("Enter the text: ")
            fh.write_file(name, text)

        elif choice == 3:
            name = input("Enter the file name: ")
            text = input("Enter the text: ")
            fh.append_file(name, text)

        elif choice == 4:
            name = input("Enter the file name: ")
            fh.read_file(name)

        elif choice == 5:
            name = input("Enter the file name: ")
            old_text = input("Text you want to replace: ")
            new_text = input("Text to replaced: ")
            fh.replace_text(name, old_text, new_text)

        elif choice == 6:
            fh.get_cwd()

        elif choice == 7:
            path = input("Enter the path to change directory: ")
            fh.change_directory(path)

        elif choice == 8:
            old_name = input("Enter the old file name: ")
            new_name = input("Enter the new name for file: ")
            fh.rename_file(old_name, new_name)

        elif choice == 9:
            name = input("Enter the file name to delete: ")
            fh.delete_file(name)

        elif choice == 10:
            print("Thank you.. Exiting.. Goodbye!!..")
            break
        
        else:
            print("Invalid choice, Please Try Again.")

if __name__ == "__main__":
    main()
