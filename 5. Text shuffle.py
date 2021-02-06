from random import shuffle

def shuffle_letters(text):
    '''
    функция для каждого слова длиннее 2х букв вынимает все буквы кроме первой и последней,
    перемешивает их и склеивает с первой и последней заново, собирает новый текст
    '''
    words = text.split()
    shuffled_words = []
    for w in words:
        if len(w) > 2:
            chars_to_shuffle = list(w[1:-1])
            shuffle(chars_to_shuffle)
            shuffled_words.append(w[0] + ''.join(chars_to_shuffle) + w[-1])
        else:
            shuffled_words.append(w)
    shuffled_text = ' '.join(shuffled_words)
    return shuffled_text


print(shuffle_letters(str(input())))

