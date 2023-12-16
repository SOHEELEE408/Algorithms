import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	final int[] dx = {0, 0, -1, 1};
	final int[] dy = {1, -1, 0, 0};

	int result;
	int weaknessResult;

	int n;
	String[][] grid;

	public Main(String[][] grid, int n) {
		this.grid = grid;
		this.n = n;
	}

	public void countSection() {
		boolean[][] visited_weakness = new boolean[n][n];
		boolean[][] visited = new boolean[n][n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				weaknessResult += bfs(Type.WEAKNESS, new Node(i, j), grid[i][j], visited_weakness);
				result += bfs(Type.NOT_WEAKNESS, new Node(i, j), grid[i][j], visited);
			}
		}
	}

	public int bfs(Type type, Node start, String color, boolean[][] visited) {
		if (visited[start.i][start.j]) {
			return 0;
		}
		Queue<Node> queue = new LinkedList<>();
		queue.offer(start);

		while (!queue.isEmpty()) {
			Node node = queue.poll();
			if (!visited[node.i][node.j]) {
				visited[node.i][node.j] = true;
				for (int i = 0; i < 4; i++) {
					int x = node.i + dx[i];
					int y = node.j + dy[i];
					if (x >= 0 && x < n && y >= 0 && y < n) {
						if (isSame(type, color, grid[x][y])) {
							queue.offer(new Node(x, y));
						}
					}
				}
			}
		}

		return 1;
	}

	public boolean isSame(Type type, String current, String next) {
		if (type == Type.WEAKNESS) {
			if (current.equals(next) || (current.equals("R") && next.equals("G")) || (current.equals("G")
				&& next.equals("R"))) {
				return true;
			}
		}

		if (type == Type.NOT_WEAKNESS && current.equals(next)) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		// 입력 받기
		Scanner sc = new Scanner(System.in);
		int n = Integer.valueOf(sc.nextLine());
		String[][] grid = new String[n][];

		for (int i = 0; i < n; i++) {
			grid[i] = sc.nextLine().split("");
		}
		Main main = new Main(grid, n);
		main.countSection();
		System.out.println(main.result + " " + main.weaknessResult);
	}

	enum Type {
		WEAKNESS,
		NOT_WEAKNESS;
	}

	class Node {
		int i;
		int j;

		Node(int i, int j) {
			this.i = i;
			this.j = j;
		}
	}
}
