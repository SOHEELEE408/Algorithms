import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int answerPtr = 0;
        for (int[] command : commands) {
            int[] copy = copyArray(array, command[0] - 1, command[1] -1);
            sort(copy, 0, copy.length -1);
            answer[answerPtr++] = copy[command[2] - 1];
        }
        return answer;
    }
    
    public int[] copyArray(int[] array, int h, int t) {
        int[] copy = new int[t - h + 1];
        for (int m = 0; m < copy.length; m++) {
            copy[m] = array[m + h];
        }
        return copy;
    }
    
    public void sort(int[] array, int left, int right) {
        if (right <= left) {
            return;
        }
        int mid = (left + right) / 2;
        sort(array, left, mid);
        sort(array, mid + 1, right);
        merge(array, left, mid, right);
    }
    
    public void merge(int[] array, int left, int mid, int right) {
        int [] temp = new int[right - left + 1];
        int l = left;
        int r = mid + 1;
        int p = 0;
        while(l <= mid && r <= right) {
            if(array[l] < array[r]) {
                temp[p++] = array[l++];
            } else {
                temp[p++] = array[r++];
            }
        }
        
        while(l <= mid) {
            temp[p++] = array[l++];
        }
        
        while(r <= right) {
            temp[p++] = array[r++];
        }
        
        for(int i = left; i <= right; i++) {
            array[i] = temp[i - left];
        }
    }
}