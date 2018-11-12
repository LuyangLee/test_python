class Solution {
public:
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b 
     */
    int aplusb(int a, int b) {
        // write your code here
        int temp;
        while(b != 0)
        {
            temp = a ^ b;
            b = (a & b)<<1;
            a = temp;
        }
        return a;
    }
};
// 数据不变的方法：与0异或