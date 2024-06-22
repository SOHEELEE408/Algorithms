import java.util.*;

/**
모두 이어붙여야 하므로 자릿 수 일정
가장 큰 수는 999
조합했을 때 더 큰 숫자가 앞에 오도록 한다. 
*/
class Solution {
    public String solution(int[] numbers) {    
        if(isAllZero(numbers)) {
            return "0";
        }
        StringBuilder answer = new StringBuilder();
        String[] strNumbers = new String[numbers.length];
        for(int i = 0; i < numbers.length; i++) {
            strNumbers[i] = String.valueOf(numbers[i]);
        }
        sort(strNumbers, 0, numbers.length - 1);
        for(int i = 0; i < numbers.length; i++) {
            answer.append(strNumbers[i]);
        }
        return answer.toString();
    }
    
    public boolean isAllZero(int[] numbers) {
        int zeroCnt = 0;
        for(int number : numbers) {
            if(number == 0) {
                zeroCnt++;
            }
        }
        return zeroCnt == numbers.length;
    }
    
    public void sort(String[] strNumbers, int left, int right) {
        if (right <= left) {
            return;
        }
        int mid = (left + right) / 2;
        sort(strNumbers, left, mid);
        sort(strNumbers, mid + 1, right);
        merge(strNumbers, left, mid, right);
    }
    
    public void merge(String[] strNumbers, int left, int mid, int right) {
        String[] sortedNumbers = new String[right - left + 1];
        int leftP = left;
        int rightP = mid + 1;
        int p = 0;
        
        while(leftP <= mid && rightP <= right) {
            Integer caseA = Integer.parseInt(strNumbers[rightP] + strNumbers[leftP]);
            Integer caseB = Integer.parseInt(strNumbers[leftP] + strNumbers[rightP]);
            if(caseA > caseB) {
                sortedNumbers[p++] = strNumbers[rightP++];
            } else {
                sortedNumbers[p++] = strNumbers[leftP++];
            }
        }
        
        while(leftP <= mid) {
            sortedNumbers[p++] = strNumbers[leftP++];
        }
        
        while(rightP <= right) {
            sortedNumbers[p++] = strNumbers[rightP++];
        }
        
        for(int i = left; i <= right; i++) {
            strNumbers[i] = sortedNumbers[i - left];
        }
    }
}