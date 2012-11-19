#!/usr/bin/env python

import sys
from pyfiglet import Figlet
from optparse import OptionParser

def draw_text(figlet, font, textlist): 
    figlet.setFont(font=font)
    for t in textlist:
        print figlet.renderText(t)

def list_fonts(figlet, count=10):
    fonts = figlet.getFonts()
    nrows = len(fonts)/count
    if len(fonts) % count != 0:
        nrows += 1

    print "Available fonts in the system"
    print
    for start in range(0, nrows):
        items = fonts[start*count:(start+1)*count]
        for item in items:
            print item + "\t",
        print
    
def main(args):
    usage = "Usage: %prog <options> <line 1> <line 2> ..."
    parser = OptionParser(usage)
    parser.add_option("-f", "--font", help="specify the font", 
                action="store", type="string", dest="font", default='clr8x8')
    parser.add_option("-l", "--list", help="list available fonts", 
                action="store_true", dest="listfonts", default=False)

    (options, args) = parser.parse_args()
    
    print "" 

    f = Figlet()
    if options.listfonts:
        list_fonts(f)
    else:   
        tlist = args
        draw_text(f, options.font, tlist)

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))

