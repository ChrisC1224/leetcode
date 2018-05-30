class Solution {
public:
    int romanToInt(string s) {
        map<char,int> M;
        M['I']=1;
        M['V']=5;
        M['X']=10;
        M['L']=50;
        M['C']=100;
        M['D']=500;
        M['M']=1000;
        int result=0;
        int num=0;
        int prenum=0;
        for(int i=s.length()-1;i>=0;i--){
            num=M[s[i]];
            if(num<prenum){
                result-=num;
            }
            else{
                result+=num;
            }
            prenum=num;
        }
        return result;
    }
};
