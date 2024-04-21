import os
import re

def printReg(file_name,encoding_type):
          pattern=input("Enter pattern or press ENTER to exit: ")
          if(len(pattern)<1):
              return
          try:
              with open(file_name,'r',encoding=encoding_type) as file:
                  file_content=file.read()
                  print(re.findall(pattern,file_content))
                  return True;
          except FileNotFoundError:
              raise ValueError(f'The file {file_name} does not exits.')
    

def main():
   while(True):
    file_name=str(input("Enter file name: "))
    if os.path.exists(file_name):
        encoding_type=input("Enter character encoding or press ENTER for default (utf-8): ")
        if encoding_type.strip():
           while(printReg(file_name,encoding_type)):
               printReg(file_name,encoding_type)
        else:
            encoding_type="utf-8"  
            while(printReg(file_name,encoding_type)):
                printReg(file_name,encoding_type)
                
            
    else:
       raise ValueError(f"{file_name} is not a file")


main()
