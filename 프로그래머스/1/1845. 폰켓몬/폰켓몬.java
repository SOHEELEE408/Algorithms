import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> poketmons = new HashMap<>();
        for (int num : nums) {
            if(poketmons.containsKey(num)) {
                poketmons.put(num, poketmons.get(num) + 1);
            } else {
                poketmons.put(num, 1);
            }
        }
        int possibleCount = nums.length / 2;
        return possibleCount > poketmons.keySet().size() ? poketmons.keySet().size() : possibleCount;
    }
}