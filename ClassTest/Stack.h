#define MAX_SIZE 50

template <class T>
class Stack
{
    private:
        T *m_data;
        int m_maxSize;
        int m_top;
        int m_size;
    public:
        Stack();
        ~Stack();
        void push(T data);
        T pop();
        bool isEmpty();
};