typedef struct {
    int *elements;
    int  len;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack *stack = (MinStack *)malloc(sizeof(MinStack));
    
    stack->elements = (int *)malloc(sizeof(int) * maxSize);
    stack->len = 0;
    return stack;
}

void minStackPush(MinStack* obj, int x) {
    obj->elements[obj->len++] = x;
}

void minStackPop(MinStack* obj) {
    obj->len--;
}

int minStackTop(MinStack* obj) {
    return obj->elements[obj->len - 1];
}

int minStackGetMin(MinStack* obj) {
    int i, min = minStackTop(obj);
    for (i = obj->len - 1; i >= 0; i--) {
        if (obj->elements[i] < min) {
            min = obj->elements[i];
        }
    }
    return min;
}

void minStackFree(MinStack* obj) {
    free(obj->elements);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */
