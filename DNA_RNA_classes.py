class Dna:
    def __init__(self, seq):
        self.seq = seq

    def __eq__(self, other):
        return self.seq == other.seq

    def __iter__(self):
        return iter(self.seq)

    def gc_content(self):
        return len([i for i in self.seq if i in "GCcg"]) * 100 / len(self.seq)

    def reverse_complement(self):
        complement_dna = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A', 'N': 'N',
                          'a': 't', 'g': 'c', 'c': 'g', 't': 'a'}
        return ''.join([complement_dna[i] for i in self.seq][::-1])

    def upper(self):
        upper_dna = {'a': 'A', 't': 'T', 'c': 'C', 'g': 'G'}
        return ''.join([upper_dna[i] for i in self.seq])

    def transcribe(self):
        return Rna(''.join([i if i in 'GCA' else 'U' for i in self.seq]))


class Rna:
    def __init__(self, seq):
        self.seq = seq

    def __eq__(self, other):
        return self.seq == other.seq

    def __iter__(self):
        return iter(self.seq)

    def upper(self):
        upper_rna = {'a': 'A', 'u': 'U', 'c': 'C', 'g': 'G'}
        return ''.join([upper_rna[i] for i in self.seq])

    def gc_content(self):
        return len([i for i in self.seq if i in "GCcg"]) * 100 / len(self.seq)

    def reverse_complement(self):
        complement_rna = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A', 'N': 'N',
                          'a': 'u', 'g': 'c', 'c': 'g', 'u': 'a'}
        return ''.join([complement_rna[i] for i in self.seq][::-1])


def create_seq(string):
    dnastr = 'ATGCNatgc'
    rnastr = 'AUGCNaugc'
    d = 0
    r = 0
    if len(string) == 0:
        print("последовательность пуста!")
        raise ValueError
    else:
        for nucl in string:
            if nucl not in dnastr:
                d += 1
            if nucl not in rnastr:
                r += 1
        if d == 0:
            print('Вы создали последовательность ДНК')
            return Dna(string)
        elif r == 0:
            print('Вы создали последовательность РНК')
            return Rna(string)
        else:
            print("Ваша последовательность не соответствует ДНК или РНК :(")
            raise ValueError

if __name__ == '__main__':
    '''
    Проверка работоспособности кода
    '''
    print("Создайте объект ДНК или РНК:")
    string = input()
    seq1 = create_seq(string)
    print(seq1.seq, " - сама последовательность")
    print(seq1.upper(), " - в верхнем регистре")
    print("CG состав последовательности: ", seq1.gc_content())
    print("Обратно комплиментарная последовательность: ", seq1.reverse_complement())

    print("Создайте объект ДНК или РНК:")
    string = input()
    seq2 = create_seq(string)
    print("CG состав последовательности: ", seq2.gc_content())
    print("Обратно комплиментарная последовательность: ", seq2.reverse_complement())
    if seq1 and seq2:
        print("\nравны ли введенные ранее последовательности? - ", seq1 == seq2)
