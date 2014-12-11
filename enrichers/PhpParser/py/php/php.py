#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function
import sys
import os
sys.path.append( "/home/yash/Projects/qt/kiwi/Build/debug/resources/enrichers/PhpParser/py/php" )

from PythonQt import *
from PythonQt.editor import BaseEditor


from arpeggio.cleanpeg import ParserPEG
from arpeggio import visit_parse_tree
from visitor import Visitor


grammar_filename = "grammar.peg"

class Php(object):

    def __init__(self, debug=False):
        f = open(grammar_filename, "r")
        self.grammar = f.read()
        self.debug = debug
        
    
    #Used finder.py module to recursively finding php tokens    
    def parse(self, filename):
    
        with open(filename) as file:
            contents = file.read()
  
        parser = ParserPEG(self.grammar, "start", True)
        parse_tree = parser.parse(contents)
        visitor = Visitor(debug=self.debug)
        
        result = visit_parse_tree(parse_tree, visitor )
        
        #Try to get if we found anything or not        
        if ( visitor.functions or visitor.classes):
            pass
#            print (visitor.namespace )
        
#            return visitor
            
        print ("Empty")
        
        return None
        
#Below code just to dev used and testing
def showMe(debug=False):

    filename = api.filepath();
#    filename = workspaces.getBaseEditor.featuresManager;
    
        
    #filename = sys.argv[1]
#    filename = "/home/yash/Projects/qt/kiwi/Build/debug/resources/enrichers/PhpParser/py/test/Application.php"
#    filename = "/var/www/html/webbase/fuel/app/tasks/robots.php"
    #debug = bool(sys.argv[2])

    with open(filename) as file:
        contents = file.read()
    #print (contents)
#    # An expression we want to evaluate
#    input_expr = """public function emergency($message, $context = array() ){"""
#    input_expr = "($message, $context=array() )"
    
#    input_expr = "$context = array()"
#    input_expr = "jjj()" 
#    input_expr = "array(ddd)" 
     
#    input_expr = input
    input_expr = contents
    
    if not input_expr:
        return None

    #grammar_filename = "%s/grammar.peg" % os.getcwd()
    grammar_filename = "resources/enrichers/PhpParser/py/php/grammar.peg"
    
    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of PEG notation therefore we
    # are using ParserPEG class. Root rule name (parsing expression) is "calc".
    
    f = open(grammar_filename, "r")
    grammar = f.read()
        
    parser = ParserPEG(grammar, "start", True) #whitespace last param


    # Then parse tree is created out of the input_expr expression.
    parse_tree = parser.parse(input_expr)

    visitor = Visitor(debug=debug,api=api)
    result = visit_parse_tree(parse_tree, visitor )
    
    print (visitor.namespace )
#    print (visitor.classes )
#    print (visitor.functions )

#    analyseASG( parser, input, Visitor(), True, False )


    # Then parse tree is created out of the input_expr expression.
    #parse_tree = parser.parse(input_expr)
    #result = parser.getASG(sem_actions)

    #print( parse_tree )
    #print( result )
    if debug:
        # getASG will start semantic analysis.
        # In this case semantic analysis will evaluate expression and
        # returned value will be evaluated result of the input_expr expression.
        # Semantic actions are supplied to the getASG function.
        print("{} = {}".format(input_expr, result))

if __name__ == "__main__":
    # In debug mode dot (graphviz) files for parser model
    # and parse tree will be created for visualization.
    # Checkout current folder for .dot files.
    #main(debug=False)
    pass
