package 단지번호붙이기_2667;

import java.io.*;
import java.util.*;

import org.junit.jupiter.api.Test;

class Main {

    static int N;
    static char[][] map;
    static boolean[][] visit;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};

    private static void solution() {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visit[i][j]) continue;

                if (map[i][j] == '1') {
                    int count = dfs(i, j);
                    answer.add(count);
                }

            }
        }

        Collections.sort(answer);

        StringBuilder sb = new StringBuilder();
        sb.append(answer.size()).append('\n');
        for (int i : answer) sb.append(i).append('\n');
        System.out.println(sb);
    }

    // 이 메서드에 들어왔으면 무조건 1이라고 가정
    private static int dfs(int y, int x) {
        visit[y][x] = true;

        int count = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 메서드에 들어가기 전에 필터링
            if (isOut(nx) || isOut(ny) || visit[ny][nx] || map[ny][nx] == '0') continue;
            count += dfs(ny, nx);
        }

        return count + 1;
    }

    private static int bfs(int y, int x) {
        // 큐에 들어갔다면 1이라고 가정
        Queue<Position> que = new LinkedList<>();
        que.offer(new Position(x, y));
        visit[y][x] = true;

        int count = 0;
        while (!que.isEmpty()) {
            Position now = que.poll();
            count++;

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                // 큐에 넣기 전에 필터링
                if (isOut(nx) || isOut(ny) || visit[ny][nx] || map[ny][nx] == '0') continue;
                que.offer(new Position(nx, ny));
                visit[ny][nx] = true;
            }
        }

        return count;
    }

    private static boolean isOut(int position) {
        return position < 0 || position > N - 1;
    }

    private static class Position {
        int x, y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static void input() throws IOException {
        BufferedReader r = new BufferedReader(new FileReader("C:\\Users\\prayme\\workspace\\boj\\src\\test\\java\\단지번호붙이기_2667\\input.txt"));
        N = Integer.parseInt(r.readLine());
        visit = new boolean[N][N];
        map = new char[N][N];

        for (int i = 0; i < N; i++) {
            map[i] = r.readLine().toCharArray();
        }
    }

    @Test
    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

}

