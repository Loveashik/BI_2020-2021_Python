from Bio import SeqIO


'''
CODON DECODER:
1. The Standard Code
2. The Vertebrate Mitochondrial Code
3. The Yeast Mitochondrial Code
4. The Mold, Protozoan, and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code
5. The Invertebrate Mitochondrial Code
6. The Ciliate, Dasycladacean and Hexamita Nuclear Code
9. The Echinoderm and Flatworm Mitochondrial Code
10. The Euplotid Nuclear Code
11. The Bacterial, Archaeal and Plant Plastid Code
12. The Alternative Yeast Nuclear Code
13. The Ascidian Mitochondrial Code
14. The Alternative Flatworm Mitochondrial Code
16. Chlorophycean Mitochondrial Code
21. Trematode Mitochondrial Code
22. Scenedesmus obliquus Mitochondrial Code
23. Thraustochytrium Mitochondrial Code
24. Rhabdopleuridae Mitochondrial Code
25. Candidate Division SR1 and Gracilibacteria Code
26. Pachysolen tannophilus Nuclear Code
27. Karyorelict Nuclear Code
28. Condylostoma Nuclear Code
29. Mesodinium Nuclear Code
30. Peritrich Nuclear Code
31. Blastocrithidia Nuclear Code
33. Cephalodiscidae Mitochondrial UAA-Tyr Code
'''

path = '/home/asha/ИБ/python/Generator/test.fa'


def generate_translated_fa(file: str, alp: int):
    with open(file) as in_file:
        for cur_seq in SeqIO.parse(in_file, "fasta"):
            translated_seq = cur_seq.seq.translate(alp)
            yield translated_seq


print('enter a number corresponding to codon table code:')
codon_table = int(input())

# tests
next_fasta_generator = generate_translated_fa(path, codon_table)
list_fasta_generator = generate_translated_fa(path, codon_table)
for i in range(10):
    print(next(next_fasta_generator))
print(list(list_fasta_generator))  # list of seqs
