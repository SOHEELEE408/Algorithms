class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        int idx1 = 0;
        int idx2 = 0;
        
        for(String word : goal){
            if(idx1 < cards1.length && word.equals(cards1[idx1])){
                idx1++;
                answer = "Yes";
                continue;
            } else if(idx2 < cards2.length && word.equals(cards2[idx2])){
                idx2++;
                answer = "Yes";
                continue;
            }
            
            answer = "No";
            break;
        }
        
        return answer;
    }
}