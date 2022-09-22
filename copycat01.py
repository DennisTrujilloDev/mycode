#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

#import code
import shutil 
import os 

def main():
    #move into working dir
    os.chdir("/home/student/mycode/")
    
    #copy one file to another 
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    #copy directory A to directory B 
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


