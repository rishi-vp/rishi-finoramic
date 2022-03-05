def find_anagrams(A):
    """
    the function finds the anagrams from a given list of words and returns their indexes.
    :param A:
    :return: a list of lists containing the indexes of the anagrams.
    """
    count_vect = []
    for i in A:
        count_vect.append([0] * 26)
    k = 0
    for l in A:
        for i in l:
            count_vect[k][ord(i) - ord('a')] += 1
        k += 1
    # print(count_vect)
    out_vect = []
    out_set = set()

    for i in range(len(count_vect)):
        temp = set()
        if i in out_set:
            continue
        else:
            out_set.add(i)
            temp.add(i)
            for j in range(len(count_vect)):
                if i == j:
                    pass
                elif count_vect[i] == count_vect[j] and j not in temp:
                    out_set.add(j)
                    temp.add(j)
            if len(temp) != 0:
                temp = sorted(list(temp))
                out_vect.append(temp)

    # print(out_vect)
    # print(len(out_vect))
    # Figured that they are considering from 1 and not zero as deafault. So adding 1 to each element of the list.
    for i in range(len(out_vect)):
        for j in range(len(out_vect[i])):
            out_vect[i][j]+=1
    # out_vect=sorted(out_vect)
    return out_vect
    # print(out_vect)


A = [ "aababbaaaabaabbabaaaaabbbaaaabbaabbabbaaaaababaaabbaaabaaaabbbaaabbabaaababaa", "bbbbbbaaaabaababbbaaabbabaaabaabbbbaabababaaababababbaaabbaabaabbabbaaaabaaba", "abaaababbababbababababaabaababbababaabaabaaabbabbaabbaaabbbabbbbbbaabbbbbbabb", "aabbabbbbababbaaabbbaaaaaaaabaabbabbabbbbaabaaaaabaaabaabbaaabbbbaaababaaabbb", "ababaaabaabbbabaaaababbaababaabaabaaabbabbaaabbbbbbabbbbaababbbbaaaaaabababaa", "babbbabbabaaabaaaabbbabbabbbaaaaabbbbabaaaaababaababbbabaaaaabbbbbbbbaabbbabb", "bbaabaabbbbbbaabaabbabbbbabababaaabaabbbbbaaaabbbaaabbbbbaaaabbaaaabababbaaaa", "ababbaaaabababaababababbabbaaaabbbbababbbbabaaabbabbabbabbbbabaababbbabbbbbab", "aaaaabbaaabbbbaabaabbbaabaaabbbbaaaaaabaaaaaabaabbbaababaabaaaaabaabaaabbbabb", "abbaaababbbbbaabbaaaabbaaaabbbbbaabaabaaaabbbabbbbabababaaabbabbabbbabbababbb", "bbbbabbbbaabbbbababbbaaaabaaababbabbababbababbabaaabbbbaabababaaaaaabbbbaabab", "babaabbaaabbaabbaabaabaaaaabbabbabbbbbbaaaaaabbbbbabaaaaabbbabaabbbaaaabbbbaa" ]
out = find_anagrams(A)
print(out)
