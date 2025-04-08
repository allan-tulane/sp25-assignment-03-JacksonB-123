import math
import queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions\
    if S == "":
         return len(T)
    elif T == "":
            return len(S)
    else:
        if S[0] == T[0]:
            return MED(S[1:], T[1:])
        else:
            return 1 + min(MED(S, T[1:]), MED(S[1:], T)) #professor said to not use subsitutions for this problem when I asked him after class so I am not including it


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
        MED[key] = 1 + min(insert, delete)
    return MED[key]
    
def fast_align_MED(S, T, MED={}): 
    # TODO - keep track of alignment
    key = (S, T)
    if key in MED:
        return MED[key][1], MED[key][2]

    if S == "":
        aligned_S = "-" * len(T)
        aligned_T = T
        MED[key] = (len(T), aligned_S, aligned_T)
        return aligned_S, aligned_T

    if T == "":
        aligned_S = S
        aligned_T = "-" * len(S)
        MED[key] = (len(S), aligned_S, aligned_T)
        return aligned_S, aligned_T

    if S[0] == T[0]:
        sub_S, sub_T = fast_align_MED(S[1:], T[1:], MED)
        aligned_S = S[0] + sub_S
        aligned_T = T[0] + sub_T
        MED[key] = (fast_MED(S[1:], T[1:]), aligned_S, aligned_T)
        return aligned_S, aligned_T
    else:
        ins_S, ins_T = fast_align_MED(S, T[1:], MED)
        ins_cost = 1 + fast_MED(S, T[1:])
        ins_result = (ins_cost, '-' + ins_S, T[0] + ins_T)

        del_S, del_T = fast_align_MED(S[1:], T, MED)
        del_cost = 1 + fast_MED(S[1:], T)
        del_result = (del_cost, S[0] + del_S, '-' + del_T)
#This is where I am stuck. for kookaburra' I am getting an assertion error.
#'kook-ab-ur-ra' == 'kook-ab-urr-a'. Iam trying to implement a tie breaker to get the correct alignment.
#I can not figure out how to do this. I have tried to implement a tie breaker but it is not working.
#I can get the edit distance to be correct but the alignment is not.
# i removed the the substitution aspect of the code like professor advised in class but i still cant solve the alignment problem. I have spent countless hours on this part and this is the closest I have gotten to solving it.
        if ins_cost < del_cost:
            best = ins_result
        elif del_cost < ins_cost:
            best = del_result
        else:
            if ins_result[1].count('-') < del_result[1].count('-'):
                best = ins_result
            elif del_result[1].count('-') < ins_result[1].count('-'):
                best = del_result
            else:
                best = min([ins_result, del_result], key=lambda x: (x[1], x[2]))

        MED[key] = best
        return best[1], best[2]
    # this is the best I can do. I am stuck on this part. I have tried to implement a tie breaker but it is not working.

