# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import Biopython
from HTfunctions import *
import numpy as np
f = open(CTGATC.fastq)

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def HD(sequences):
	n = len(sequences)
	L = []
	for seq1 in sequences:
		for seq2 in sequences:
			distance = HammingDistance(sequences[seq1],sequences[seq2])
			L.append(distance)
	finalList = np.reshape(L,(n,n))
	return finalList

#Make some kind of plot that contains the data you've calculated.
plt.show()
