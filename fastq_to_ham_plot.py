# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
from Bio import SeqIO
import sys

my_fastq = sys.argv[1]

from HTfunctions-2 import *
import numpy as np
import numpy as np


def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	sequences = {}
	for record in SeqIO.parse(fastq_file, "fastq"):
	    sequences[record.name] = record.seq
	return sequences


sequences = getSeqs(my_fastq)

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

#Make some kind of plot that contains the data you've calculated.

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

keys=list(sequences.keys())
names=list(sequences.values())
def plot(output_hamming,sequences):
	fig, ax = plt.subplots()
	im = ax.imshow(output_hamming)
	ax.set_xticks(range(0,len(keys)))
	ax.set_yticks(range(0,len(keys)))
	ax.set_xticklabels(names)
	ax.set_yticklabels(names)
	plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
# Loop over data dimensions and create text annotations.
	for i in range(len(output_hamming)):
		for j in range(len(output_hamming)):
			text = ax.text(j, i, output_hamming[i, j],ha="center", va="center", color="w")
			ax.set_title("Hamming distance")
			fig.tight_layout()
	plt.show()
plot(hamming,sequences)
