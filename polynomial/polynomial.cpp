#include "polynomial.h"
#include <iostream>
#include <iomanip>

using namespace std;

pLink* add(pLink *a, pLink *b) 
{
    pLink *p, *q;
    pLink *head = NULL;
    q = new pLink;
    while (a != NULL) 
    {
        p = new pLink;
        if (a->exp > b->exp) 
        {
            p->exp = a->exp;
            p->coe = a->coe;
            a = a->next;
        } 
        else if (a->exp < b->exp) 
        {
            p->exp = b->exp;
            p->coe = b->coe;
            b = b->next;
        } 
        else if (a->exp == b->exp)
        {
            p->exp = a->exp;
            p->coe = a->coe + b->coe;
            a = a->next;
            b = b->next;
        }
        if (head == NULL) 
        {
            head = p;
            q = p;
        }
        else 
        {
            q->next = p;
            q = p;
        }
        q->next = NULL;
        /*
        **下面按照栈式结构建立链表
        p->next = q;
        q = p;
        return q;
        */
    }
    return head;
}

pLink* init() 
{
    pLink *p, *q;
    pLink *h = NULL;
    for (int i = 2; i >= 0; i--)
    {
        p = new pLink;
        p->coe = 1;
        p->exp = i;
        if (h == NULL)
        {
            q = p;
            h = q;
        }
        else {
            q->next = p;
            q = p;
        }
        q->next = NULL;
        /*
        **下面按照栈式结构建立链表
        p->next = q;
        q = p;
        return q;
        */
    }
    return h;
}

void del(pLink *head) //删除动态分配的链表
{      
    pLink *p1,*p2;
    p1 = head;
    p2 = p1;
    while(p1 != NULL)
    {
        p1 = p1->next;
        delete p2;
        p2 = p1;
    }
}

void show(pLink *head) 
{
    pLink *p;
    p = head;
    while (p != NULL)
    {
        cout<<p->coe<<endl;
        cout<<p->exp<<endl;
        p = p->next;
    }
}

int main() 
{    
    pLink *p = init();
    show(add(p, p));
    del(p);
    return 0;
}