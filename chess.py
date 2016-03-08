# -*- coding: utf8 -*-

def generate_empty_chessboard():
    """ Function that generates a clean chessboard without pieces or labelling."""
    return "".join("".join( "\u25a0" if ( bool(row % 2) == bool(column % 2) ) else "\u25a1" for row in range(0,8)) + "\n" for column in range(0,8))

print generate_empty_chessboard()
