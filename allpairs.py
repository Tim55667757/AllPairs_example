# -*- coding: utf-8 -*-
#
# (c) Gilmullin Timur Mansurovich,  2013.

# Using AllPairs by MetaCommunications Engineering example.

from ext.metacomm.combinatorics import all_pairs2 as ap

def Generator(parameters):
    """
    Use generator which work on AllPairs-algorithm.
    Input:
    parameters - list of list of different parameters, that looks like this:
    [ [par1_val_1, par1_val_2, ...],
      [par2_val_1, par2_val_2, ...], ... ]
    Output:
    list of enumerate possible unique combinations, that looks like this:
    [ (0, [par1_val_1, ..., parK_val_K]), ...
      (N, [parX_val_X, ..., parY_val_Y]), ...]
    """
    combinations = list(enumerate(ap.all_pairs2(parameters)))
    return combinations


if __name__ == '__main__':
    # define list of list of different parameters:
    inputData = [
        ['Windows XP SP 3', 'Windows 7 SP 1', 'Debian 7.1', 'Ubuntu 12.04'],
        ['x86', 'x64'],
        ['chrome', 'firefox', 'safari']
        ]
    outputData = Generator(inputData)
    with open('output.txt', 'w') as fH:
        for line in outputData:
            stringData = 'Combination {}:\t{}'.format(str(line[0]), str(line[1]))
            print(stringData)
            fH.write(stringData + '\n')