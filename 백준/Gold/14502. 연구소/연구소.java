import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

	int[] dx = new int[]{0, 0, -1, 1};
	int[] dy = new int[]{1, -1, 0, 0};

	int max = 0;

	int n, m;
	int[][] lab;
	List<int[]> zero;
	List<int[]> two;

	public Main(int n, int m, int[][] lab, List<int[]> zero, List<int[]> two) {
		this.n = n;
		this.m = m;
		this.lab = lab;
		this.zero = zero;
		this.two = two;
	}

	public void wall(int wallCount) {
		if (wallCount == 3) {
			virus();
			return;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (lab[i][j] == 0) {
					lab[i][j] = 1;
					wall(wallCount + 1);
					lab[i][j] = 0;
				}
			}
		}
	}

	public void virus() {
		int[][] copyLab = new int[lab.length][lab[0].length];
		for (int i = 0; i < lab.length; i++){
			copyLab[i] = lab[i].clone();
		}

		List<int[]> queue = new LinkedList<>(two);

		while (!queue.isEmpty()) {
			int[] v = queue.remove(0);
			for (int i=0; i<4; i++){
				int x = v[0] + dx[i];
				int y = v[1] + dy[i];
				if (x >= 0 && y >= 0 && x < n && y  < m) {
					if (copyLab[x][y] == 0) {
						queue.add(new int[]{x, y});
						copyLab[x][y] = 2;
					}
				}
			}
		}
		result(copyLab);
	}

	public void result(int[][] lab) {
		int result = 0;
		for (int i=0; i< lab.length; i++) {
			for (int j=0; j< lab[i].length; j++) {
				if(lab[i][j] == 0) {
					result++;
				}
			}
		}
		this.max = Math.max(result, this.max);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] nm = sc.nextLine().split(" ");

		int n = Integer.valueOf(nm[0]);
		int m = Integer.valueOf(nm[1]);
		int[][] lab = new int[n][m];
		List<int[]> zero = new ArrayList<>(); // 벽 후보
		List<int[]> two = new ArrayList<>();
		Main main = new Main(n, m, lab, zero, two);

		for (int i = 0; i < n; i++) {
			String[] input = sc.nextLine().split(" ");
			for (int j = 0; j < m; j++) {
				lab[i][j] = Integer.valueOf(input[j]);
				if (Integer.valueOf(input[j]) == 0) {
					zero.add(new int[]{i, j});
				}
				if (Integer.valueOf(input[j]) == 2) {
					two.add(new int[]{i, j});
				}
			}
		}
		main.wall(0);
		System.out.println(main.max);
	}
}
