int minAddToMakeValid(char* S) {
    int slen = strlen(S);
    
    int left = 0;
    int ret = 0;
    
    for (int i = 0; i < slen; i++) {
        if (S[i] == '(') {
            left++;
        }
        else {
            if (left > 0) {
                left--;
            }
            else {
                ret++;
            }
        }
    }
    
    ret += left;
    
    return ret;
}
