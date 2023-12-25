import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	int depth;
	String[] inputs;

	public Main(int depth, String[] inputs) {
		this.depth = depth;
		this.inputs = inputs;
	}

	public void result(Node root) {
		Queue<Node> nodes = new LinkedList<>();
		nodes.offer(root);
		int depth = root.depth;

		while (!nodes.isEmpty()) {
			Node node = nodes.poll();
			if (node.depth != depth) {
				System.out.println();
				depth = node.depth;
			}
			System.out.print(node.value + " ");
			if (node.left != null) {
				nodes.offer(node.left);
			}
			if (node.right != null) {
				nodes.offer(node.right);
			}
		}
	}

	public Node makeNode(int start, int length, int depth) {
		if (length < 1) {
			return null;
		}
		int middle = (length - 1) / 2;
		int value = Integer.valueOf(inputs[start + middle]);
		Node root = new Node(value, depth);
		root.left = makeNode(start, middle, depth - 1);
		root.right = makeNode(start + middle + 1, middle, depth - 1);

		return root;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int depth = Integer.valueOf(sc.nextLine());
		String[] inputs = sc.nextLine().split(" ");

		Main main = new Main(depth, inputs);
		Node result = main.makeNode(0, inputs.length, depth);
		main.result(result);
	}

	class Node {
		int value;
		Node left;
		Node right;

		int depth;

		Node(int value, int depth) {
			this.value = value;
			this.left = null;
			this.right = null;
			this.depth = depth;
		}

		public Node(int value, Node left, Node right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}
	}
}
