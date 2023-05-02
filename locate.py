################################
#------------LOCATE------------#
# Copyright 2022 Sourav Bishai #
################################
import os
from os import path
import sys
import click
import colorama
from colorama import Fore

colorama.init()

def banner():
    aboutxt = f"""
    {Fore.YELLOW+"Sourav Bishai"}
                                         
    this tool is used for find or locate your file or folder       
    using command line like linux locate command tool.
    {Fore.RED + "Warning: this tool work only windows platform"}:            

    """
    print(aboutxt)


@click.command()
@click.option("--d", help="set the drive name [ eg: --d e:/ or --d d:/subfolder/anotherfolder/ ]")
@click.option("--f", help="set the file/folder name you want to search")

def main(d, f):
    
    drive = d

    if path.isdir(drive):
        os.chdir(drive)
        file = f
        data = os.listdir()
        if d and f:
            # item mean file or folder
            for item in data:
                try:
                    if path.isdir(item):# if any item is folder so this code is run
                        """try deyar karon sob kechu folder hoy na
                        system volume information theke onnano kechu file o thake 
                        error na asar karone ata deya"""
                        try:
                            dirdata = os.listdir(item)
                        except:
                            pass
                        for diritem in dirdata:
                            data.append(f"{item}\\{diritem}")
                except KeyboardInterrupt:
                    print(Fore.YELLOW+"Bye...")
                    sys.exit(1)

                # set the file name with parent path 
                filepath = f"{os.getcwd()}\{item}"
                # split function return a tuple, --
                # first element file path and second file name
                getOnlyFile = path.split(filepath)

                if file.upper() in getOnlyFile[1].upper():
                    print(Fore.BLUE+filepath)
        else:
            print(Fore.RED + "[*] invalid argument")
    else:
        print(Fore.RED + "[*] Enter invalid drive name")


if __name__ == "__main__":
    banner()
    main()
    