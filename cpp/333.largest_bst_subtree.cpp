/* Tree node structure  used in the program
 struct Node
 {
     int data;
     struct Node* left, *right;
};*/
/*You are required to complete this method */

typedef struct {
    bool is_BST;
    int min;
    int max;
    int size;
} result_t;

result_t findLargestBst(Node *ptr)
{
    result_t result;
    
    result.is_BST = true;
    result.size   = 0;
    
    if (ptr) {
        result_t l_result = findLargestBst(ptr->left);
        result_t r_result = findLargestBst(ptr->right);
        
        if (!l_result.is_BST || (l_result.size > 0 && ptr->data < l_result.max)) {
            result.is_BST = false;
        }
        else {
            result.min = (l_result.size) ? l_result.min : ptr->data;
        }
        
        if (!r_result.is_BST || (r_result.size > 0 && ptr->data > r_result.min)) {
            result.is_BST = false;
        }
        else {
            result.max = (r_result.size) ? r_result.max : ptr->data;
        }
        
        result.size = (result.is_BST) ? (l_result.size + r_result.size + 1)
                                      : max(l_result.size, r_result.size);
    }
    
    return result;
}

int largestBst(Node *root)
{
	result_t result = findLargestBst(root);
	return result.size;
}
