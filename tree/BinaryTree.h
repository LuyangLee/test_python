#include <iostream>
#include <vector>

typedef struct BinaryTree 
{
    int data;
    struct BinaryTree *leftTree;
    struct BinaryTree *rightTree;
}Btree;