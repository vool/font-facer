#!/usr/bin/env python


__author__ = "Keith o'Faolain"
__copyright__ = "Copyright 2012"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "keith@vool.ie"

# set the default dir to search, used if no directory arg is passed
defaultSearchPath = "."

# set the name of the demo file
demofilename = "font-facer.html"

import os.path
import sys

print("=============================================================")
if (len(sys.argv) > 1):
    if os.path.isdir(sys.argv[1]):
        print("Setting search path as: "+ sys.argv[1])
        searchdir = sys.argv[1]
    else:
        print("ERROR - The path: [ "+sys.argv[1]+" ] does not exist, falling back to default path: "+ defaultSearchPath)
        searchdir = defaultSearchPath

else:
    print("No search search passed falling back to default path: "+ defaultSearchPath)
    searchdir = defaultSearchPath
    
    
print("=============================================================")


ff = []


def getffs(dirpath):
        
    os.chdir(dirpath) 
    ffs = {}
    path = os.curdir
    for d in os.listdir(path):      
        
        if os.path.isdir(d):
            print(d)
            
            curpath = os.path.join(path, d)
            
            
            ffs[d] = [] # add directory with empty list
            demofile = os.path.join(curpath, 'stylesheet.css')
            
            if os.path.isfile(demofile):
                
                f = open(demofile, "r")
                for line in f:
                            #check for fonts in file
                            if "font-family:" in line:
                                    # strip all but name
                                    ffont = line.strip("font-family:\t'").strip("font-family: '").strip("';\n").strip(' ').strip('\t').strip('\n')
                                    #ffont = ffont.strip("font-family: '")
                                    #ffont = ffont.strip("';\n").strip(' ').strip('\t').strip('\n')
                                    #line = line.replace('\t',"")
                                    ffs[d].append(ffont)
                                    print '\t+ font-family - ' + ffont
                
                    #ffs[d].append(f) # add files to appropriate directory
            if len(ffs[d]) == 0:
                ffs.pop(d)
            
    return ffs  
        
ff = getffs(searchdir)



if(len(ff) > 0):
    
    FILE = open(os.path.join(searchdir, demofilename), "w")
    
    
    FILE.write("<!doctype html>\n\
    <html class=\"no-js\" lang=\"en\">\n\
    \t<head>\n\
    \t\t<meta charset=\"utf-8\">\n\
    \t\t<title>FFace Off | Quick and Durty Font Face Viewer</title>\n")
        
    # add the ff style sheets
    for dirs, files in ff.items():
        
    
        FILE.write('\t\t<link rel="stylesheet" href="' + dirs + '/stylesheet.css" >' + "\n")
        
        
    FILE.write('\t\t<style media="screen">' + '\n\
    \t\t\tbody{background-color:#e6e6e6; padding:10px;}\n\
    \t\t\tinput{font-size:20px; padding:5px; background-color:#ddd; }\n\
    \t\t\t.search{position:fixed; top:0; right:50px; z-index:50; padding: 5px 15px 10px 15px; background-color:#ccc; border:#ddd 1px solid; border-top:0; -webkit-border-bottom-right-radius: 10px; -webkit-border-bottom-left-radius: 10px; -moz-border-radius-bottomright: 10px; -moz-border-radius-bottomleft: 10px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; }\n\
    \t\t\th1{background-color:#ddd; padding:5px; margin:0;}\n\
    \t\t\th2{background-color:#ccc; font-size:13px; position:relative;  border:#ccc 1px solid; top:-5px; padding:2px 20px; margin:0; -moz-border-radius: 5px; -webkit-border-radius: 5px; border-radius: 5px;\
    }\n\
    \t\t\th2, input{font-family: "Lucida Sans Unicode", "Lucida Grande", "Lucida Sans", Verdana, Arial, sans-serif;}\n\
    \t\t\t.ffamily{border:#ccc 1px solid; margin-bottom:12px; background-color:#ddd; -webkit-border-bottom-right-radius: 5px; -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomright: 5px; -moz-border-radius-bottomleft: 5px; border-bottom-right-radius: 5px; border-bottom-left-radius: 5px;}\n\
    \t\t\t.ffamily span{position:absolute; left:-10px; top:-1px; display:block;  padding:1px; font-size:13px; color:#fff; font-weight:bold; border:#666 1px solid;  background-color:#666; width:18px; height:18px; -moz-border-radius: 50%; -webkit-border-radius: 50%; border-radius: 50%; text-align:center;}\n\
    \t\t\t.ffamily span:hover{background-color:#fff; color:#666; border-color:#fff;}\n\
    \t\t\th2.expand:hover{cursor:pointer; background-color:#aaa; color:#eee;}\n')
    
    for dirs, files in ff.items():
        
    
        for f in files:
    
            FILE.write("\t\t\th1." + f + " {font: 60px/68px \'" + f + "\', Arial, sans-serif;letter-spacing: 0;}\n")
                       
    # close head open body
    FILE.write('\t\t</style>\n\
    \t\t<script src="http://code.jquery.com/jquery-latest.js"></script>\n\
    \t</head>\n\
    \t<body>\n\
    \t\t<div class="search"><input type="text" value="In your (font) face !"/></div>')
    
    for dirs, files in ff.items():
                
            
        FILE.write('\t<div class="ffamily">\n')
        #check if more that one font in family
        familysize = str(len(files))
        
        
        if len(files) > 1:
            FILE.write('\t\t<h2 class="expand"><span class="tog">-</span>' + dirs + ' - ' + familysize + ' fonts</h2>\n')
        else:
            FILE.write('\t\t<h2>' + dirs + '</h2>\n')
            
    
        for f in files:
        
            FILE.write('\t\t<h1 class="' + f + '" title="' + f + '">' + f + '</h1>\n')
            
        FILE.write('\t</div>\n')
        
    FILE.write('\t<script>\n\
    \t\t$(function() {\n\
    \t\t\t$(".expand").click();\n\
    \t\t});\n\
    \t\t$("input").keyup(function () {\n\
    \t\t\tvar value = $(this).val();\n\
    \t\t\t$("h1").text(value);\n\
    \t\t\tif(value == ""){\n\
    \t\t\t\t$("h1").each(function(){\n\
    \t\t\t\t\t$(this).text($(this).attr("title"));\n\
    \t\t\t\t});\n\
    \t\t\t}\n\
    \t\t});\n\
    \t\t$("input").focus(function () {\n\
    \t\t\t\tif($(this).val() == "In your (font) face !"){\n\
    \t\t\t\t\t$(this).val("");\n\
    \t\t\t}\n\
    \t\t});\n\
    \t\t$(".expand").click(function () {\n\
    \t\t\t$(this).siblings(\'h1\').not(":first").toggle(\'slow\');\n\
    \t\t\t$(this).children(".tog").text($(this).children(".tog").text() == \'-\' ? \'+\' : \'-\');\n\
    \t\t});\n\
    \t</script>')

        
    # close html
    FILE.write("    </body>\n       </html>")
    
    print("All done !")
    FILE.close()
else:
    # no fonts found
    print("No font faces found in search path:" + searchdir)
