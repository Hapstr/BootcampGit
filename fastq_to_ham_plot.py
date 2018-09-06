# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
from Bio import SeqIO
import sys

my_fastq = sys.argv[1]

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
plt.show()
