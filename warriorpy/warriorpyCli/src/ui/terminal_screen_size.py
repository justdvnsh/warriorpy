"""
 * Returns the size of the screen.
 *
 * @returns {number[]} The size of the screen as an array of [width, height].
"""

import os

def screenSize():
    ts = os.get_terminal_size()

    return [ ts.columns, ts.lines ]

print(screenSize())