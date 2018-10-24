char* customSortString(char* S, char* T) {
    int tlen = strlen(T);
    int slen = strlen(S);
    char *ret = (char *)malloc((sizeof(char) * tlen) + 1);
    char ch_nums[26] = {0};
    
    for (int i = 0; i < tlen; i++) {
        ch_nums[T[i] - 'a'] ++;
    }
    
    int ridx = 0;
    for (int i = 0; i < slen; i++) {
        char c = S[i];
        for (int j = 0; j < ch_nums[c - 'a']; j++) {
            ret[ridx++] = c;
        }
        ch_nums[c - 'a'] = 0;
    }
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < ch_nums[i]; j++) {
            ret[ridx++] = i + 'a';
        }
    }
    ret[tlen] = 0;
    
    return ret;
}
