import os

def install():
    print("Installing packages...")
    os.system("pip install ")
    os.system("pip install beautifulsoup4")
    os.system("pip install lxml")
    print("Packages installed successfully!")

def would_you_like_to_install():
    print("this program requires the following packages to be installed:")
    print("we will install a python script")
    print("you need to have the python executable in your PATH")
    yes_no1 = input("Would you like to install the packages? (y/n): ")
    if yes_no1 == "y":
        