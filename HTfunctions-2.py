def importFASTA(filename):
    f = open(filename , 'r')
    
    linesList = f.readlines()
    sequenceList = []

    for index,line in enumerate(linesList):
        strippedLine = line.strip()
        if strippedLine.startswith('>'):
            sequenceList.append('')
        else:
            sequenceList[-1] = sequenceList[-1] + strippedLine
    return sequenceList


def importFASTAzip(filename):
    f = open(filename , 'r')
    
    linesList = f.readlines()
    sequenceList = []
    rosalist = []
    d = {}

    for index,line in enumerate(linesList):
        strippedLine = line.strip()
        if strippedLine.startswith('>'):
            rosalist.append(strippedLine[1:])
            sequenceList.append('')
        else:
            sequenceList[-1] = sequenceList[-1] + strippedLine
    zippedList = zip(rosalist,sequenceList)
    return zippedList

        
def ReverseCompliment(s):
    string = ''
    for letter in s:
        if letter is 'A':
            string = string + 'T'
        if letter is 'T':
            string = string + 'A'
        if letter is 'C':
            string = string + 'G'
        if letter is 'G':
            string = string + 'C'
    return string[:: -1]

def HammingDistance(a,b):
    HD = 0
    zippedSeq = zip(a,b)
    for a1,b1 in zippedSeq:
        if a1 != b1 or a1 == 'N' or b1 == 'N':
            HD = HD + 1
    return HD


def Translation(RNA):
    newString = ''
    for index, letter in enumerate(RNA):
        if index % 3 == 0:
            newString = newString + ' '
        newString = newString + letter
    StrippedNewString = newString.strip()
          
    codons = StrippedNewString.split()
    proteinSequence = ''  


    d = {}

    d['F'] = ['UUU','UUC']
    d['L'] = ['UUA','UUG','CUU','CUC','CUA','CUG']
    d['S'] = ['UCU','UCC','UCA','UCG','AGU','AGC']
    d['Y'] = ['UAU','UAC']
    d[''] = ['UAA','UAG','UGA']
    d['C'] = ['UGU','UGC']
    d['W'] = ['UGG']
    d['P'] = ['CCU','CCC','CCA','CCG']
    d['H'] = ['CAU','CAC']
    d['Q'] = ['CAA','CAG']
    d['R'] = ['CGU','CGC','CGA','CGG','AGA','AGG']
    d['I'] = ['AUU','AUC','AUA']
    d['M'] = ['AUG']
    d['T'] = ['ACU','ACC','ACA','ACG']
    d['N'] = ['AAU','AAC']
    d['K'] = ['AAA','AAG']
    d['V'] = ['GUU','GUC','GUA','GUG']
    d['A'] = ['GCU','GCC','GCG','GCA']
    d['D'] = ['GAU','GAC']
    d['E'] = ['GAA','GAG']
    d['G'] = ['GGU','GGC','GGA','GGG']

    for codon in codons:
        for key in d:
            if codon in d[key]:
                proteinSequence = proteinSequence + key
    return proteinSequence

def Transcription(DNAstring):
    RNAstring = ''
    for letter in DNAstring:
        if letter is "T":
            RNAstring = RNAstring + "U"
        else:
            RNAstring = RNAstring + letter
    return RNAstring

    

