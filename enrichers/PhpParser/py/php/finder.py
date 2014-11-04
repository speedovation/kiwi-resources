#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import fnmatch
import os, sys
import json
from php import Php
 
rootPath = '/home/yash/Projects/php'
#rootPath = '/home/yash/Projects/php/laravel/app/controllers'
pattern = '*.php'

def callParsing():
    
    p = Php(False)

    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename) )
            
            # filename 
            #Debug to false
            full_filename = os.path.join(root, filename) 

            d = p.parse( full_filename )
    #        print ( type(d) )
    #        print (json.dump(d.namespace), file = 'waste/%s' % filename)
    #        with open( 'waste/%s' % filename, 'w') as fp:
    #            json.dump(d.namespace, fp)
            
            if d:
                f = '../dumps/%s' % filename
                d.namespace["path"] = os.path.relpath(full_filename, rootPath)
                outputFile = open( f , "w")
                json.dump(d.namespace, outputFile, sort_keys = False, indent = 4)
                outputFile.close()  
   

if __name__ == "__main__":
    # In debug mode dot (graphviz) files for parser model
    # and parse tree will be created for visualization.
    # Checkout current folder for .dot files.
    if (len(sys.argv) >= 2) :  
        rootPath = sys.argv[1]
        
    callParsing()    
