import java.util.Scanner;

public class Main {

	int n;

	public void floydWarshall(int[][] datas) {
		for (int m = 0; m < n; m++) {
			for (int i = 0; i < n; i++) {
				if (i == m) {
					continue;
				}
				for (int j = 0; j < n; j++) {
					if (j == m || datas[i][j] == 1) {
						continue;
					}
					if (datas[i][m] == 1 && datas[m][j] == 1) {
						datas[i][j] = 1;
					}
				}
			}
		}
	}

	public static void main(String[] args) {
		Main findRoute = new Main();
		Scanner sc = new Scanner(System.in);

		findRoute.n = Integer.valueOf(sc.nextLine());
		int[][] datas = new int[findRoute.n][findRoute.n];

		for (int i = 0; i < findRoute.n; i++) {
			String[] data = sc.nextLine().split(" ");
			for (int j = 0; j < data.length; j++) {
				datas[i][j] = Integer.valueOf(data[j]);
			}
		}
		findRoute.floydWarshall(datas);

		for (int i = 0; i < findRoute.n; i++) {
			for (int j = 0; j < findRoute.n; j++) {
				System.out.print(datas[i][j] + " ");
			}
			System.out.println();
		}
	}
}
