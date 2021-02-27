from Bio.Seq import Seq

path = '/home/asha/ИБ/python/Generator/test.fa'


def generate_translated_fa(file, alp):
    with open(file) as in_file:

        seq_name = ''

        for line in range(sum(1 for l in in_file)):
            if in_file[line].startswith('>'):
                seq_name = in_file[line].strip()
                translated_seq = ''
            else:
                x = in_file.readline()
                while not next(x).startswith('>') or in_file.readline():
                    translated_seq += Seq(line.strip()).translate(alp)
                yield seq_name + '\n' + str(translated_seq)






        # for i,line in enumerate(in_file):
        #     print(i)
        #     if i == 300:
        #         yield describer + '\n' + str(translated_seq)
        #         break
        #     elif line[i+1].startswith('>'):
        #         translated_seq += Seq(line).strip('\n').translate(alp)
        #         describer = ''
        #         y=1
        #     elif not line.startswith('>'):
        #         translated_seq += Seq(line).strip('\n').translate(alp)
        #     else:
        #         describer += str(line).strip()
        #     if y == 1:
        #         y = 0
        #         yield describer + '\n' + str(translated_seq)


print('enter a number corresponding to codon table code:')
codon_table = int(input())
gener = generate_translated_fa(path, codon_table)
# tests
for i in range(8):
    print(next(gener))
print(list(gener))  # list of seqs with names
