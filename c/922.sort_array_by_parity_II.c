/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParityII(int* A, int ASize, int* returnSize) {
    *returnSize = ASize;
    int *ret = (int *)malloc(sizeof(int) * (*returnSize));
    int odd = 1, even = 0;
    for (int i = 0; i < ASize; i++) {
        if (A[i] % 2) {
            // even
            ret[odd] = A[i];
            odd += 2;
        }
        else {
            ret[even] = A[i];
            even += 2;
        }
    }
    return ret;
}
