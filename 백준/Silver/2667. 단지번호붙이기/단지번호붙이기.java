import java.util.*;

public class Main {

    private int complexesCnt;

    private final List<Integer> houseCnt;
    private final Queue<int[]> queue;

    private final int[] dx = {0, 0, -1, 1};
    private final int[] dy = {1, -1, 0, 0};

    public Main(){
        this.houseCnt = new ArrayList<>();
        this.queue = new LinkedList<>();
    }

    public void bfs(int n, int w, int h, final char[][] apartments){
        int cnt = 0;

        queue.add(new int[]{w, h});

        while(!queue.isEmpty()){
            int[] node = queue.poll();

            cnt++;
            apartments[node[0]][node[1]] = 'x';
            
            for(int i=0; i<dx.length; i++){
                int x = Integer.valueOf(node[0]) + Integer.valueOf(dx[i]);
                int y = Integer.valueOf(node[1]) + Integer.valueOf(dy[i]);

                if(x >=0 && x<n && y >=0 && y<n && apartments[x][y] == '1') {
                    apartments[x][y] = 'x';
                    queue.add(new int[]{x, y});
                }
            }
        }

        if(cnt > 0){
            complexesCnt += 1;
            houseCnt.add(cnt);
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.valueOf(sc.nextLine());
        char[][] apartments = new char[n][];

        for(int i=0; i<n; i++){
            char[] homes = sc.nextLine().toCharArray();

            apartments[i] = homes;
        }

        Main apartment = new Main();

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(apartments[i][j] == '1')
                    apartment.bfs(n, i, j, apartments);
            }
        }

        if(apartment.houseCnt.size() > 0)
            Collections.sort(apartment.houseCnt);

        System.out.println(apartment.complexesCnt);
        for (int count : apartment.houseCnt)
            System.out.println(count);
    }
}
