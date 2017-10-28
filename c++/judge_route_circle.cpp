
class Solution {
public:
    bool judgeCircle(string moves) {
        if(moves.size()==0){
            return true;
        }
        pair<int, int> location(0,0);
        for(int i=0;i<moves.size();i++){
            char currentMove = moves[i];
            switch(currentMove){
                case 'L':
                    location.first-=1;
                    break;
                case 'R':
                    location.first+=1;
                    break;
                case 'U':
                    location.second+=1;
                    break;
                case 'D':
                    location.second-=1;
                    break;
            } 
        }
        if(location == make_pair(0,0)){
            return true;
        }
        return false;
    }
};