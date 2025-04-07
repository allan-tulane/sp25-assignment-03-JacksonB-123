import math
import queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions\
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return 1 + min (MED(S, T[1:]),MED(S[1:], T),MED(S[1:], T[1:]))


def fast_MED(S, T, MED={}): 
    # TODO -  implement top-down memoization
    key = (S, T)
    if key in MED:
        return MED[key]
    if S == "":
        MED[key] = len(T)
    elif T == "":
        MED[key] = len(S)
    elif S[0] == T[0]:
        MED[key] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        substitute = fast_MED(S[1:], T[1:], MED)
        MED[key] = 1 + min(insert, delete, substitute)
    return MED[key]
    

def fast_align_MED(S, T, MED={}): 
    # TODO - keep track of alignment
    key = (S, T)
    if key in MED:
        return MED[key]  # Return the entire tuple: (distance, align_S, align_T)
    if S == "":
        MED[key] = (len(T), '-' * len(T), T)
    elif T == "":
        MED[key] = (len(S), S, '-' * len(S))
    elif S[0] == T[0]: 
        dist, align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[key] = (dist, S[0] + align_S, T[0] + align_T)
    else:
        # insert
        ins_dist, ins_S, ins_T = fast_align_MED(S, T[1:], MED)
        ins_result = (1 + ins_dist, '-' + ins_S, T[0] + ins_T)
        # delete
        del_dist, del_S, del_T = fast_align_MED(S[1:], T, MED)
        del_result = (1 + del_dist, S[0] + del_S, '-' + del_T)
        # substitute
        sub_dist, sub_S, sub_T = fast_align_MED(S[1:], T[1:], MED)
        sub_result = (2 + sub_dist, S[0] + sub_S, T[0] + sub_T)  # substitution cost = 2
        # consistent tie-breaking: prefer insert > delete > substitute, then lexicographically
        choices = [ins_result, del_result, sub_result]
        choices.sort(key=lambda x: (x[0], x[1], x[2]))
        MED[key] = choices[0]
    return MED[key]