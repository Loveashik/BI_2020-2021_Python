class Dna:
    def __init__(self, seq):
        self.seq = seq

    def __eq__(self, other):
        return self.seq == other.seq

    def __iter__(self):
        return iter(self.seq)

    def gc_content(self):
        return len([i for i in self.seq if i in "cgCG"]) * 100 / len(self.seq)

    def reverse_complement(self):
        complement_dna = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A', 'N': 'N',
                          'a': 't', 'g': 'c', 'c': 'g', 't': 'a'}
        return ''.join([complement_dna[i] for i in self.seq][::-1])

    def upper(self):
        upper_dna = {'a': 'A', 't': 'T', 'c': 'C', 'g': 'G', 'N': 'N',
                     'A': 'A', 'C': 'C', 'T': 'T', 'G': 'G'}
        return ''.join([upper_dna[i] for i in self.seq])

    def transcribe(self):
        transcribed = ''
        for i in self.seq:
            if i in 'acgACG':
                transcribed += i
            elif i == 't':
                transcribed += 'u'
            else:
                transcribed += 'U'
        return transcribed


class Rna:
    def __init__(self, seq):
        self.seq = seq

    def __eq__(self, other):
        return self.seq == other.seq

    def __iter__(self):
        return iter(self.seq)

    def upper(self):
        upper_rna = {'a': 'A', 'u': 'U', 'c': 'C', 'g': 'G', 'N': 'N',
                     'A': 'A', 'C': 'C', 'U': 'U', 'G': 'G'}
        return ''.join([upper_rna[i] for i in self.seq])

    def gc_content(self):
        return len([i for i in self.seq if i in "cgCG"]) * 100 / len(self.seq)

    def reverse_complement(self):
        complement_rna = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A', 'N': 'N',
                          'a': 'u', 'g': 'c', 'c': 'g', 'u': 'a'}
        return ''.join([complement_rna[i] for i in self.seq][::-1])


'''
функция определяет, объект какого класса будет создан, на основании его последовательности 
(если отсутствует Урацил, объект будет принадлежать классу ДНК)
'''


def create_seq(string):
    dnastr = 'ATGCNatgc'
    rnastr = 'AUGCNaugc'
    d = 0
    r = 0
    if len(string) == 0:
        print("последовательность пуста!")
        raise ValueError
    else:
        for nucleotide in string:
            if nucleotide not in dnastr:
                d += 1
            if nucleotide not in rnastr:
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
    seq1 = create_seq(input())
    print("сама последовательность: ", seq1.seq)
    print("в верхнем регистре: ", seq1.upper())
    print("CG состав последовательности: ", seq1.gc_content())
    print("Обратно комплиментарная последовательность: ", seq1.reverse_complement())
    if isinstance(seq1, Dna):
        print("транскрипт: ", seq1.transcribe())

    print("Создайте объект ДНК или РНК:")
    seq2 = create_seq(input())
    print("CG состав последовательности: ", seq2.gc_content())
    print("Обратно комплиментарная последовательность: ", seq2.reverse_complement())
    if isinstance(seq2, Dna):
        print("транскрипт: ", seq1.transcribe())
    if seq1 and seq2:
        print("\nравны ли введенные ранее последовательности? - ", "ДА" if seq1 == seq2 else "НЕТ")
