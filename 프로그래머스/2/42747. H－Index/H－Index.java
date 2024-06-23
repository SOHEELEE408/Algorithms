import java.util.*;
/**
1. 주어진 배열을 오름차순 정렬한다. [0, 1, 3, 5, 6]
2. 차례대로 돌면서 조건을 만족하는 지 체크한다.
    - h편 이상이다. > citations.length - i(자기 자신의 인덱스)
*/
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int citationCnt = citations.length;
        sort(citations, 0, citationCnt - 1);
        for(int i = 0; i < citationCnt; i++) {
            if(i + 1 <= citations[i]) {
                answer = Math.max(answer, i + 1);
            }
        }
        return answer;
    }
    
    public void sort(int[] citations, int left, int right) {
        if(right <= left) {
            return;
        }
        int mid = (right + left) / 2;
        sort(citations, left, mid);
        sort(citations, mid + 1, right);
        merge(citations, left, mid, right);
    }
    
    public void merge(int[] citations, int left, int mid, int right) {
        int[] newCitations = new int[right - left + 1];
        int leftP = left;
        int rightP = mid + 1;
        int p = 0;
        
        while(leftP <= mid && rightP <= right) {
            if(citations[leftP] <= citations[rightP]) {
                newCitations[p++] = citations[rightP++];
            } else {
                newCitations[p++] = citations[leftP++];
            }
        }
        
        while(leftP <= mid) {
            newCitations[p++] = citations[leftP++];
        }
        
        while(rightP <= right) {
            newCitations[p++] = citations[rightP++];
        }
        
        for(int i = left; i <= right; i++) {
            citations[i] = newCitations[i - left];
        }
    }
}