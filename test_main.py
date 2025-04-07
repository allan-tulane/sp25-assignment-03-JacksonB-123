from main import fast_MED, MED, fast_align_MED, test_cases, alignments

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert align_S == alignments[i][0] and align_T == alignments[i][1]

if __name__ == "__main__":
    test_MED()
    print("MED tests passed.")

    test_align()
    print("Alignment tests passed.")
