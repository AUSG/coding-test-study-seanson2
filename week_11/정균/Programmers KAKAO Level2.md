## `Programmers KAKAO Summer Intern Level2`

```java
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * created by Gyunny 2021/01/10
 * https://programmers.co.kr/learn/courses/30/lessons/81302
 */
public class Two {
    private static int N;
    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};

    public static int[] solution(String[][] places) {
        N = places.length;
        int[] answer = new int[places.length];

        for (int i = 0; i < N; ++i) {
            boolean check = true;
            String[] result = places[i];

            out:for (int j = 0; j < N; ++j) {
                String resultOne = places[i][j];
                for (int k = 0; k < resultOne.length(); ++k) {
                    if (resultOne.charAt(k) == 'P') {
                        if (!bfs(j, k, result)) {
                            check = false;
                            break out;
                        }
                    }
                }
            }

            if (check) answer[i] = 1;
        }

        return answer;
    }

    private static boolean bfs(int a, int b, String[] places) {
        Queue<Edge> queue = new LinkedList<>();
        queue.add(new Edge(a, b));

        while (!queue.isEmpty()) {
            Edge e = queue.poll();

            for (int i = 0; i < 4; ++i) {
                int nx = dx[i] + e.x;
                int ny = dy[i] + e.y;

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && (nx != a || ny != b)) {
                    int distance = Math.abs(nx - a) + Math.abs(ny - b);
                    if (places[nx].charAt(ny) == 'P' && distance <= 2) {
                        return false;
                    }
                    if (places[nx].charAt(ny) == 'O' && distance < 2) {
                        queue.add(new Edge(nx, ny));
                    }
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String[][] places = {
                {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}
        };
        System.out.println(Arrays.toString(solution(places)));
    }
}

class Edge {
    int x;
    int y;

    public Edge(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

- `2021년 카카오 여름 인턴 2번 문제이었음`
- 문제에서 바로 알 수 있듯이 전형적인 `bfs/dfs` 문제임
