#!/usr/bin/python3
###################################################
# 2017-10-01 - Stephen Camera-Murray              #
# cleanse_srt.py - function to cleanse .srt files #
#                  into .txt files, one row per   #
#                  subtitle.                      #
###################################################

#import libraries
from bs4 import BeautifulSoup
import gzip
import warnings
import os

# do not display warnings
warnings.filterwarnings('ignore')

# cleanse_srt ( fin, fout ) - function to cleanse an .srt file
#   parameters:
#     fin  - input filename
#     fout - output filename
#   returns:
#
#   example: cleanse_srt ( fin, fout )
#

def cleanse_srt ( fin, fout ):

    # reset vars
    subtitle_lines = False
    subtitle = ''
    
    # open output file for writing
    outfile = gzip.open(fout, 'wt')

    # open input file and loop
    with gzip.open(fin,'rt') as f:
        for line in f:

            # check to see if we're on the lines with the subtitle, if not check to see if we are
            # subtitles immediately follow the time range and end with a blank line
            if (not subtitle_lines):
                subtitle_lines = ('-->' in line)
            else:

                # check for a blank line, if not strip out HTML and append to full_subtitle
                subtitle_lines = (line.strip() != '')
                if subtitle_lines:
                    soup = BeautifulSoup(line)
                    text = soup.get_text()
                    subtitle += ' ' + text.strip()
            
                # at the end of the subtitle, write it out
                else:
                    outfile.writelines ( subtitle.strip() + '\n' )
                    subtitle = ''
                    
    # close the output file
    outfile.close()
    
    return

#####################################################################
## Main - loop through currect directory and cleanse all .srt files #
#####################################################################

def main():
    
    # loop through the data directory and cleanse each .srt file
    for fin in os.listdir():
        if ( '.srt' in fin ):
            cleanse_srt (fin, fin.replace('.srt','.txt'))
##

if __name__ == "__main__":
    main()
