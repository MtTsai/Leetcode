class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        trie_root = {}

        repeat_pat = set([])

        for i in range(len(s) - 9):
            pat = s[i:i+10]

            trie = trie_root
            for c in pat:
                if c not in trie.keys():
                    trie[c] = {}

                trie = trie[c]
            if '_' in trie.keys():
                repeat_pat.add(pat)
            else:
                trie['_'] = 'pattern'

        return list(repeat_pat)

    def _findRepeatedDnaSequences(self, s):

        pattern_dist = {}

        repeat_pat = set([])

        for i in range(len(s) - 9):
            pat = s[i:i+10]
            if pat not in pattern_dist.keys():
                pattern_dist[pat] = 0
            else:
                repeat_pat.add(pat)

        return list(repeat_pat)

if __name__ == "__main__":
    data = [(["AAAAACCCCC", "CCCCCAAAAA"], "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
            (["AAAAAAAAAA"],               "AAAAAAAAAAAA"),
            (['AAGCAGGCGC', 'CGTCTCCCAA',
              'GTCTCCCAAG', 'CTTTAATCCA',
              'CCTAGACAAT', 'AATCGGTCTC',
              'CCCTCTGCAA', 'CTGTTTGGAT',
              'CCAGAAAGTG', 'TGCTTACGAG',
              'CCGAGGTATA', 'GGATTGGAGC',
              'TTTAATCCAA', 'TTAATCCAAT',
              'ATCGGTCTCC', 'CAATCGGTCT',
              'CTCGCTTGAG', 'AGCAGGCGCT',
              'CTAGACAATT', 'GCTGTGATGA'], 
                                           "CCTATTTAAGGGAATCGCGGTCAACTATGTTGCCAGAATATAGGATGGAA"
                                           "AGCAGACTCGCCGGCAGACGCTCTGAGATTCTCTGTAATCGATCTGAGTT"
                                           "CATAAGCGACTCATAGACACCGTAGGCCATGACGGGGGAGGTGCGGGTAG"
                                           "TCGCAAAAAAAATGTGGCCTGCGTTCCGAAAGTTAATCGTAAGGACCTCT"
                                           "TAAGGTCAATTTCCGTAGTGATATAACGGACGCGACTTTAGGATACTATA"
                                           "TTGCCCCACATTAACTCCCTTCCCTCTGCAATCGGCATGTGCTCCCGAGG"
                                           "TATACTGTCTTCGGAACAAACTGAATCCATACACCTCTTATCGACCCAGC"
                                           "ACCTCCGAAAAGGAAATCGACGCCCCAACATTATACGCCTAGACAATTGC"
                                           "AACATAGAGCGAGACGTAGCGATCCAAACGAGCTAACAGCTCGAGATAAC"
                                           "GAGTGCCTACGGCGATCGATGTCAAACGTCCAAGTGCATACTCGCTAGGA"
                                           "CATTGGCTCATCAGGACTCAACTTAGTAGCTGATGCTGCTAGTTTAACGT"
                                           "CTTGTAATCAATATAGAGCATTGCACGGACACCAGCGCTCAACCTGGAGA"
                                           "TGCCTTGTCTCGGAAAAACTGCATTCTGTAATAACCACGGGGTGCCACAT"
                                           "TCCGGAACCGGGATCCGTCAAGCATGCCTTTCCGATTCATCGCGGGGTAC"
                                           "CTCTGGCTTCCTTGAACCTGGGTGGGTATAAAATAACCGGTTTTAAGTGG"
                                           "CTCGACAGAGCGGGAAGCAGGCGCTATCATCAGGTTTTTACGGATTTATA"
                                           "GAGACCTCTTGTGCAGCAATACCTCTTTAATCCAATGTGGGCGCCCCCTT"
                                           "CATAGGGTCACGTCAGCATGATTCGTCGGGCCGAGGGACATGACTGACGA"
                                           "CCGTTGGCAATACCCCGACCTCTAAAATTGTCCAACAGTGTGGTAGGTTA"
                                           "TCCTGGTGACGCGGTATGACGGTCGATGCGAGCGTGTAGAAAGATGACGA"
                                           "GAGAGTCATCTCACAACATTGCGTGCTGTTTGGATCATACACCCCTGTGG"
                                           "AGGGCTTACCAGAAAGTGGACGCAGAAAGCCACCAAAAGTGTCATGCCAG"
                                           "ATACCTGGCCTCCTTCGCCGCCGCGACTGAAGACCTTCCTTTAATTCCGT"
                                           "TATCCTACTTACGACCGAGAGTCAGATCTGTCAGTAAAGATCGGTCTGTT"
                                           "GCTTTCCACGGACTGTGAAGAATCCGCTGTTCTAACCAGCCAGCCCATTA"
                                           "TACGGATCGATTTTGAAGTAACCTAGTAGGCGAATCAGCGGCCGGGCCTG"
                                           "ATGCTAGACTCCCTAGACAATTTCCTCTCCACGGAAGGTTCCTAATCCCT"
                                           "GGGAATTTGGCTTATACGGGCCTTGGACACTGTTAAACTTCAGAGTGATA"
                                           "ATTTAATGGCGAAGCTCTACGCCAGCGACCGCCGAAGCTCGCACCTTTAG"
                                           "CCCCCCTGAGTGAAGAACACTCGGGAATCTGCTCTCCTTGCAACCAAGCA"
                                           "ACGGCGGGGTAGATATGGTGGGTTTCATGACGGCCCGGGAAGCTCTGGTC"
                                           "ATAGCAATACTTGGGTAGCTGTGATGAGGGTCCAAAACTTTTTGGGCCAA"
                                           "GGTTCGGACGACACCGTCCGATCGACTGCCTAACTACCTGTTCACCCCAT"
                                           "CGATAGAGTACAGTCGAGGCCCCGCCCGACCCATACGTCAAGACAGTGAC"
                                           "AATAGGTGCTTACGAGTTTCTATAATAAATTGTCGGGACGATGTCTGCCC"
                                           "GCCTACCTGAGTGCGTGCCCGATATGGGGCTTGCGGAAAACTATGAAATA"
                                           "TTAGTATTGCCCGGGGGACTCAGTCGAGTATTTGTGGAGACTCCCATTGC"
                                           "ACTACTACAGCACCATATTAAGCTTACTCAGATACGTTAGAACAATAGGG"
                                           "GATCCACTTAAAACATTACAGATCCCAATCGGTCTCCTTGTTAAGGAAAA"
                                           "GCGTTAACAGGTGTGGTGGCAGTTATATTTGTAATAGACTTATAATAGGG"
                                           "TATTCCAAGTTTATTGTGGATAACGTCTCAAACCTGTTCCACACCACGAG"
                                           "TGTGGGCAATGAGATCCTATTGGCACGTCGTTATAGTCTCAGTGCCTGAA"
                                           "GACACCTGAAAGCAGGCGCTGTGACGTGTACCCAGTGCCCTCTGCAACCG"
                                           "GGAACTAGGGTTACAGAGGGGAAACAAAAATGATCGCACGCTTTAATCCA"
                                           "ATACCGTTTCCCGTCTCCCAAGGTGAGACACTCCGGGGTATAAGTCCAGC"
                                           "CTCTTGTACGGTCACGATTAGGCGAAAATCTACTGTCTACCTTCGGTGTG"
                                           "CATTGTCTTAGCGTCTTATCCAGAGAGGAATGGCTTTCGTCGTCGTCGCT"
                                           "AGTTTCGCTCGCTTGAGGTATAGTTAATAGCAAGACTACGAGTCCACTGC"
                                           "TTCATGTCTAATTCATCGGCAGCCCTGTTTGGATTGGAGCGTAGCTAGGA"
                                           "CCCCCGAACCAGCCTTAACTATGAACGTTTGTCTTCAAATCTGGGCGCAC"
                                           "GTACTTCGTAGGCTGGATATGCAGAATCTCGCCGTCGTGACGACGATCCG"
                                           "TTGTAGACGGCACAGCGTCTCTGACCGGCTTGAACTAATGCTGACAATTC"
                                           "TGACATAAGGTCTACGCATCCAGAAAGTGTAATGCATGTATGTATGCAGC"
                                           "CAAACGATAGTAGAGCCCTATCTCGCTTGAGAGGCACTTCCCTGTATGCA"
                                           "AATACCGATGTTTCTCCGCTTCATGTACTAAAACCCTGTGACCGACTAGT"
                                           "TGCACCTACGATTGTATGACACGACGGCCTTAGAGGCAGCAACGCGTGGT"
                                           "AGGCCGTTATGCGAGGAATTCTACTACAGTCGGGAGCCGCAGCGGAAGCA"
                                           "ATTTTTTTACTCACGTTCCAGCATGCTGCAAACGGAAGCTGACACGGAGT"
                                           "CAATCGGGTAAATTTTGAGCAAATAAATCGCGACAACTAGTCCCGACTAC"
                                           "GCTTTCGACACTGTCCGGCAGATTCCGTGCATCAATTAAACGTCATCAAT"
                                           "CAATTACTGGCACGACTGTAGACGGGTGTACTCTTTTATAGACTCAGCAG"
                                           "TAGGACCTATGTGGAGCGGTCTACACATTGACGCAAGACACAAGAACTAG"
                                           "CGCGGATTGTTTGATTCGGTGACCTCTGAGGGTCGCTAAGCGACACCACA"
                                           "ATGCGTTAGTGCTAACGTAAGAGAGCTCGATTGCTATATAGATGTCGGTA"
                                           "TTCTTCAATGCATTTGCTTACTAGCAGCGTCGGATACTCTTGGCCGGGAC"
                                           "CTTCTTATTAGTCAATTACAGAAACAGTTGAAAGCCCCACCAGTTGCATA"
                                           "TACTACTGCCTCCATTGTTGATGACCTCAACTTGCCTACCAGGATTGGAG"
                                           "CACCGATGTTATTTCCTCCGAGGTATAACCGAGCGTCATAACTTGGATGT"
                                           "ATCCAGACTCGCTTATCCCCTCGCTGAGCATATCCTAGTCTGGATGACTT"
                                           "CAGAGAGCCTTTCTGGTCCGTAATATCCCAGTAGACTGGAGTTGTAGCAA"
                                           "ATCGACCCTTGGGTGACTGCCTCACCCTGAAGTGATGTCTCTTCTTTACC"
                                           "ATGCAGGCACTGGTCTAGCCGCCGAGTATCTTCTGATCCTTCTAAGGGCT"
                                           "TATTCGAAACAGCTTAACAAATGACAGGCTGTGATGATATATTACGTTGA"
                                           "CGCTACGGGGACAGCGCCTATGTCGGCCACTAGGGCTTCATCCGTTACTC"
                                           "AGGGTCAAATGGGGATTTCATATTGCGGGATCGATTGAAGATAGCATCAC"
                                           "ACGTCTCCCAAGATACGTCCCACTTTGGTTTTGGTCACTCCTTATTCCGC"
                                           "GACGGTAGTCCCGCGCTGTTGCAAACTCGTTTGAAGACGCCTAGTCAAGA"
                                           "TTCACTTCGCGGATCCGGCATCTTCGAATGGTTGGGATCCAGACGAGCGT"
                                           "GGGCGTACTGCTTACGAGAACGACTCGGCAGTGTTAGAGTGTTATCTGAA"
                                           "GGAGATGCTAGTAACATAATATACAAATCTTTATGTTAGTAGACTGCACA"
                                           "AGTCAATATGGATACATAGGTCCATGGAAGAATGTTCACGCGTTACTTGT"
                                           "GTCTCGCCACGCGAGTGCATCTCCATAGAGCCTTCCTGTATCGTCACTTT"
                                           "CTCTCGATGGTCAGCGTTTCAATAATTCGCGAGCAACAACGTCGATCTCC"
                                           "GGGATATACGATCAGCCCAGAGTACAAGACCCGATATGCACGGCATGCAA"
                                           "TATCCAGAGTCGGGCATACTTTATTGGACTGGTAAGTCTCTCCTGTCCAC"
                                           "GCTGACTACAACTGAAGTAGTGTGACCTGACTGGCGCCTTCTACCACCCA"
                                           "TGTCTCCAGCAATTGTCGCATCATACAGGTTCCCAGCGTAGCGTCGCCCC"
                                           "TTTGGCGCTTTCCTGCGGTATCGATATAATGAAATTTTCACCAACGTTGC"
                                           "GCTTATTCGCAAGGTGGCGAGATTGTATTATGCCACACAGCCTCCTAGAA"
                                           "TATCCTAAGGCAGAGTTCGGTGACTTTTGCCGCTTTAGGCAGGACAGAGC"
                                           "TGTCCTTATCTTGGGACAGCACGTGCTTCGATATACTGCCCGCGCTTTCT"
                                           "CTGGGGACGCTTTAAGGTCTTTTTGCTGCGATTGCGCTATCCGAGCCACT"
                                           "GTATCTTATACCGACGTATCTCGGCCTCGTTACATAGAAAATACTGTCAG"
                                           "CGCTTGTAGCGAGACCACGCGATAGTGACCGGAGTTGGTTCCTCCGTCCT"
                                           "TTTTGTATTCCCCGTTGCGACTGATTCACGTGACCACATAGTCATAAGAC"
                                           "ACTGAAACAAAGCTTACTTTGGCGAGTAGGATGTGTTAATAACTTCTGGC"
                                           "AGCACATAGAATTGGTCCGTGGTCCTCCTTTGCGGCCACTACTGAACGTA"
                                           "CCAATGAGTACGTATTGACCTCTTACTGAGTGTAGTAAGGGAGCATCAAT"
                                           "CGGTCTCCGGGTTTTTGATTCATGAGTCATGCATCAGTGGTTCATCCCTT"
                                           "GCGTGTTATTCTCTTGATACGGTTGACTAAGCAATGAGTTAGTCGAGCTA")]
    for ans, dna in data:
        out = Solution().findRepeatedDnaSequences(dna)
        if sorted(ans) != sorted(out):
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
