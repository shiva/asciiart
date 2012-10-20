#!/usr/bin/env python

import sys
from pyfiglet import Figlet
from optparse import OptionParser

def draw_text(f, font, text): 
    f.setFont(font=font)
    print f.renderText(text)

def main(args):
    parser = OptionParser()
    parser.add_option("-f", "--font", help="specify the font", 
                action="store", type="string", dest="font", default='clr8x8')
    parser.add_option("-l", "--list", help="list available fonts", 
                action="store_true", dest="listfonts", default=False)

    (options, args) = parser.parse_args()
    
    print "" 

    f = Figlet()
    if options.listfonts:
        for font in f.getFonts():
            print font
    else:   
        draw_text(f, options.font, 'Thanks Levi & Andras')
        draw_text(f, options.font, 'for the cards !!!') 

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))

