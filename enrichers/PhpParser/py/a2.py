#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals, print_function

from arpeggio.cleanpeg import ParserPEG
import sys

# Semantic actions
from calc import to_floatSA, factorSA, termSA, exprSA

# Grammar is defined using textual specification based on PEG language.
calc_grammar = """

#comment

    document   =  (doctype / text / tag)*
    tag        =  open_tag (text / tag)* close_tag
    
    open_tag   =  "<"  tag_name ">"
    close_tag  =  "</" tag_name ">"
    
    doctype    =  "<!DOCTYPE " tag_name ">"
    
    tag_name   =  r'[0-9a-zA-Z-]+'
    text       =  r'[^<]+'

"""

# Rules are mapped to semantic actions
sem_actions = {
    "number" : to_floatSA,
    "factor" : factorSA,
    "term"   : termSA,
    "expression" : exprSA,
}

def main(debug=False):

    # First we will make a parser - an instance of the calc parser model.
    # Parser model is given in the form of PEG notation therefore we
    # are using ParserPEG class. Root rule name (parsing expression) is "calc".
    parser = ParserPEG(calc_grammar, "document", debug=debug)


    filename = sys.argv[1]
    with open(filename) as file:
        contents = file.read()
    
    # An expression we want to evaluate
    input_expr = "<tag>dgdg</tag>"
    input_expr = contents

    # Then parse tree is created out of the input_expr expression.
    parse_tree = parser.parse(input_expr)

    #result = parser.getASG(sem_actions)

    #print( result )
    print( parse_tree )
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
    main(debug=False)

