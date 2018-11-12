#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

template<typename T> class BitreeNode
{
    private:
        int data;
        BitreeNode *LTree;
        BitreeNode *RTree;
    public:
        BitreeNode(T newData)
        {
            data = newData;
            LTree = RTree = NULL;
        }
        BitreeNode()
        {
            data = NULL;
            LTree = RTree = NULL;
        }
};

template<typename K> class Bitree
{
    private:
        BitreeNode<K> *root;
    public:
        Bitree()
        {
            root = new BitreeNode<K>();
        }

}