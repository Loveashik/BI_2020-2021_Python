from itertools import product

def generate_dna(max_N):
    '''
    generates seq of length <= input length
    '''
    nucls = 'ACTG'
    length = 1
    i=0
    while length <= max_N:
        generated_dna = product(nucls, repeat=length)
        while i < 4**length:
            yield ''.join(next(generated_dna))
            i+=1
        i=0
        length+= 1


print('enter the max length of seq to generate dna:\n')
n = int(input())
gen_next = generate_dna(n)      #to demonstrate iterations of generator
gen_list = generate_dna(n)      #to show the whole list of seqs
for _ in range(4**n):
    print(next(gen_next))

print("\nlist of all sequences:\n")
print(list(gen_list))

