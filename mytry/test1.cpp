#include<iostream>
#include<vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result(2);
        int len = nums.length;
        int i = 0, j = len-1;
        while (i < j) {
            if (nums.get(i) + nums.get(j) == target) {
                result[0] = i;
                result[1] = j;
            }
            if (nums.get(i) + nums.get(j) < target) {
                i ++;
            }
            if (nums.get(i) + nums.get(j) > target) {
                j --;
            }
        }
        return result;
    }
};