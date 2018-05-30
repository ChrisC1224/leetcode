class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        map<int, int> M;
        int res;
        for(int i=0;i<nums.size();i++){
            res=target-nums[i];
            map<int, int>::iterator iter=M.find(res);
            if(iter!=M.end()){
                result.push_back(i);
                result.push_back(iter->second);
            }
            M[nums[i]]=i;
        }
        return result;
    }
};
