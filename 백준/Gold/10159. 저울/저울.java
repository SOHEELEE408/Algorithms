import java.util.Scanner;

public class Main {

	int N, M;

	public Main(int N, int M) {
		this.N = N;
		this.M = M;
	}

	public void floydWarshall(int[][] datas) {
		for (int m = 1; m <= N; m++) {
			for (int i = 1; i <= N; i++) {
				if (m == i) {
					continue;
				}
				for (int j = 1; j <= N; j++) {
					if (datas[i][j] == 1 || j == m) {
						continue;
					}
					if (datas[i][m] == 1 && datas[m][j] == 1) {
						datas[i][j] = 1;
					}
				}
			}
		}
	}

	public void result(int[][] datas, int[][] datas_reverse) {
		for (int i = 1; i <= N; i++) {
			int result = 0;
			for (int j = 1; j <= N; j++) {
				if (datas[i][j] == 1 || datas_reverse[i][j] == 1) {
					continue;
				}
				result++;
			}
			System.out.println(result);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Integer n = Integer.valueOf(sc.nextLine());
		Integer m = Integer.valueOf(sc.nextLine());
		Main scales = new Main(n, m);
		int[][] datas = new int[n + 1][n + 1];
		int[][] datas_reverse = new int[n + 1][n + 1];

		for (int i = 0; i < m; i++) {
			String[] data = sc.nextLine().split(" ");
			datas[Integer.valueOf(data[0])][Integer.valueOf(data[1])] = 1;
			datas_reverse[Integer.valueOf(data[1])][Integer.valueOf(data[0])] = 1;
		}

		for (int i = 1; i <= n; i++) {
			datas[i][i] = 1;
			datas_reverse[i][i] = 1;
		}
		scales.floydWarshall(datas);
		scales.floydWarshall(datas_reverse);
		scales.result(datas, datas_reverse);
	}
}
