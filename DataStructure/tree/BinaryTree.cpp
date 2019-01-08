#include "BinaryTree.h"

using namespace std;
Btree *constructCore(int *preStart, int *preEnd, int *inStart, int *inEnd)
{
    Btree *root = new Btree;
    int rootData = *preStart;
    root->data = rootData;
    root->leftTree = NULL;
    root->rightTree = NULL;
    exception e;
    if(preStart == preEnd)
    {
    	if(inStart == inEnd && *inStart == *preStart)
	    	return root;	
	    else
    		throw e;
    }
    int *inroot = inStart;
    while( inroot <= inEnd && *inroot != rootData)
    	inroot++;
   	if(inroot > inEnd || *inroot != rootData)
   		throw e;
	int leftLength = inroot - inStart;
	int *leftPreEnd = preStart + leftLength; 
	if(inroot > inStart)
	{
		root->leftTree = constructCore(preStart + 1,leftPreEnd,inStart, inroot - 1);
	}
	if(preEnd >= preStart + leftLength)
	{
		root->rightTree = constructCore(preStart + leftLength + 1, preEnd, inroot + 1, inEnd);
	}
	return root;
}

Btree * construct(int *preOrder, int * inOrder, int length)
{
    if(preOrder == NULL || inOrder == NULL || length == NULL)
        return NULL;
    else    
        return constructCore(preOrder, preOrder + length - 1, inOrder, inOrder + length - 1);
}

void preTraverse(Btree *myroot)
{
	if(myroot != NULL)
	{
		cout<<myroot->data<<" "<<endl;
		preTraverse(myroot->leftTree);
		preTraverse(myroot->rightTree);
	} 
}

int main()
{
	int a[8] = {1, 2, 4, 7, 3, 5, 6, 8};
	int b[8] = {4, 7, 2, 1, 5, 3, 8, 6};
	Btree *ptree;
	try
	{
		ptree = construct(a, b, 8);
	}
	catch (exception e)
	{
		e.what();
	}
	preTraverse(ptree);
	return 0;
}

