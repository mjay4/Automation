# Automation
Automating file transfer using python.

1. mapit.py :
  This takes the name of a place to seach from the clipboard or from the command line and use google maps to search the place. We only need to press search once this process is done. 
  
  
2. Separate_Based_On_Initil_Letters.py:
   This is just a model program, it takes the initial letters and then search the folder in which it is placed to locate the files starting with that initial pattern. For now the input is hardcoded to search only "harward" in the folder and then move all those files to another folder. TODO: Make it event based execution and take values from clipboard or commandline.
   

3. ExtentionBasedSeparation.py : 
   This sepearates the files in different folders based on their extensions. Only thing that we need to do is, improve the code to make it event based. i.e, whenever a file enters the folder it will automatically go to the desired folder.


4. FlipkartPrice.py : 
    The purpose of this program is to search the css style in the page and then output the price of the item after parsing. We can improve the code by using loop to run through thousands of urls and automate it further by storing it in a text file for future reference.

5. Facebook_login.py: 
   It opens the facebook page and logs you in directly after one time setup. We can further optimise it by creating a .bat file and running it from command line.
