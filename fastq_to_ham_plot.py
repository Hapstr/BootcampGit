# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import numpy as np
#f = open(CTGATC.fastq.txt)

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

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
