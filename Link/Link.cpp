#include "Link.h"

dlink* init(int d)  //初始化链表
{
    dlink *head = new dlink;
    head->data = d;
    head->next = NULL;
    return head;
}

dlink* add(dlink* head,dlink* ins)      //添加元素到链表尾部
{
    dlink* ptr;
    ptr = head;
    while(ptr->next != NULL)
    {
        ptr = ptr->next;
    }
    ptr->next = ins;
    return head;
}

void del(dlink *head)     //删除动态分配的链表
{
    dlink *p1,*p2;
    p1 = head;
    p2 = p1;
    while(p1 != NULL)
    {
        p1 = p1->next;
        delete p2;
        p2 = p1;
    }
}

void print(dlink *head)     //打印链表
{
    dlink *p = head;
    while(p != NULL)
    {
        cout<<p->data<<endl;
        p = p->next;
    }
}

dlink* invert(dlink *head)      //翻转链表，首先初始是p为head，q为空，r什么也没有
{
    if(head == NULL)
        return head;
    dlink *p,*q,*r;
    p = head; 
    q = NULL;
    while(p != NULL)
    {
        r = q;
        q = p;
        p = p->next;
        q->next = r;
    }
    head = q;
    return head;
}

// 反向输出链表
void printLink_Reverse(dlink *head)
{
    stack<dlink *> nodes;
    dlink *p = head;
    while (p != NULL)
    {
        nodes.push(p);
        p = p->next;
    }
    while (!nodes.empty())
    {
        p = nodes.top();
        printf("%d\n",p->data);
        nodes.pop();
    }
}
int main()
{
    dlink *head = init(5);
    dlink* ins = new dlink;
    ins->data = 6;
    ins->next = NULL;
    head = add(head,ins);
    print(head);
    head =invert(head);
    print(head);
    printLink_Reverse(head);
    del(head);
}