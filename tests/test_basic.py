from DNA_RNA_classes import create_seq, Dna, Rna


def test_creation():

    # -------------------------------------------------------------------
    # DNA sequence
    # -------------------------------------------------------------------

    seq = 'AGGTTGaCATTA'
    processed_seq = create_seq(seq)
    assert isinstance(processed_seq, Dna)

    # -------------------------------------------------------------------
    # RNA sequence
    # -------------------------------------------------------------------

    seq = 'aGCGuUGaCAuuA'
    processed_seq = create_seq(seq)
    assert isinstance(processed_seq, Rna)


def test_transcribe():

    seq = 'AGGTtGaCATTA'
    processed_seq = create_seq(seq)
    transcribed_seq = processed_seq.transcribe().seq
    assert transcribed_seq == 'AGGUuGaCAUUA'


def test_gc_content():

    seq = 'AGgTtGaCATTAtAaT'
    processed_seq = create_seq(seq)
    gc_content = processed_seq.gc_content()
    assert gc_content == 25

    seq = 'ATtaATTAtAaT'
    processed_seq = create_seq(seq)
    gc_content = processed_seq.gc_content()
    assert gc_content == 0


def test_reverse_complement():

    seq = 'aGCtA'
    processed_seq = create_seq(seq)
    rev_compl = processed_seq.reverse_complement().seq

    assert rev_compl == 'TaGCt'
