package 스도쿠_2580;

import java.io.*;
import java.util.*;

import org.junit.jupiter.api.Test;

class Main {

    static int N;

    static int[][] map = new int[10][10];

    static List<XY> empty = new ArrayList<>();

    static Set<Integer>[] row = new Set[10];
    static Set<Integer>[] col = new Set[10];
    static Set<Integer>[] area = new Set[10];

    static StringBuilder answer;

    static class XY {
        int x, y;

        public XY(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    @Test
    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        // 9 * 9 의 스도쿠 판

        // 가로줄과 세로줄에는 1부터 9까지의 숫자가 한번씩만.
        // 3 * 3 에도 1부터 9까지의 숫자가 한번씩만
        // 완전탐색? 매번 행, 열, 사각형을 검증해야한다. 절대 불가능.

        // 열, 행, 사각형을 캐싱하고 있는 Set을 유지하면 어떨까?


        // 0 인 부분의 좌표를 기억하고 있자.
        // 각 좌표에 0 ~ 9 를 반복하자.

        N = empty.size();
        backtracking(0);
//        String result = "1 3 5 4 6 9 2 7 8 " +
//                "7 8 2 1 3 5 6 4 9 " +
//                "4 6 9 2 7 8 1 3 5 " +
//                "3 2 1 5 4 6 8 9 7 " +
//                "8 7 4 9 1 3 5 2 6 " +
//                "5 9 6 8 2 7 4 1 3 " +
//                "9 1 7 6 5 2 3 8 4 " +
//                "6 4 3 7 8 1 9 5 2 " +
//                "2 5 8 3 9 4 7 6 1 ";
        System.out.println(answer);
    }

    private static void backtracking(int n) {
        // 빈 칸을 모두 채울 때 까지 반복
        // n == 채운 빈칸 수
        // backtracking(0) 에서 시작
        if (n == N) {

            // 다 채웠으면 정답 리턴
            answer = new StringBuilder();
            for (int i = 1; i < 10; i++) {
                for (int j = 1; j < 10; j++) {
                    answer.append(map[i][j]).append(' ');
                }
                answer.append('\n');
            }
        } else {
            XY xy = empty.get(n);
            int x = xy.x;
            int y = xy.y;
            for (int i = 1; i < 10; i++) {
                // 정답 존재하면
                if (Objects.nonNull(answer)) return;
                // 사각형에 이미 숫자가 존재하면
                if (getArea(y, x).contains(i)) continue;
                // 가로에 존재하면
                if (row[y].contains(i)) continue;
                // 세로에 존재하면 종료
                if (col[x].contains(i)) continue;

                // 다음 칸으로 이동하기 전에 
                map[y][x] = i; // 스도쿠에 숫자 적기
                getArea(y, x).add(i); // 사각형에 숫자 넣었다고 알려주기
                row[y].add(i); // 가로에 숫자 넣었다고 알려주기
                col[x].add(i); // 세로에 숫자 넣었다고 알려주기

                backtracking(n + 1); // 다음 빈칸으로 넘어가기

                map[y][x] = 0; // 스도쿠에 숫자 지우기
                getArea(y, x).remove(i);  // 사각형에 숫자 빼기
                row[y].remove(i); // 가로에 빼기
                col[x].remove(i); // 세로에도 빼라 좀
            }
        }
    }

    private static void input() throws IOException {
        InputReader r = new InputReader("C:\\Users\\workspace\\boj\\src\\test\\java\\스도쿠_2580\\input.txt");
        for (int i = 1; i < 10; i++) {
            row[i] = new HashSet<>();
            col[i] = new HashSet<>();
            area[i] = new HashSet<>();
        }

        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < 10; j++) {
                map[i][j] = r.nextInt();
                // 빈 칸의 좌표를 기억한다.
                if (map[i][j] == 0) empty.add(new XY(j, i));
                else {
                    // 빈 칸이 아니면 가로, 세로, 사각형의 Set에 저장한다.
                    row[i].add(map[i][j]);
                    col[j].add(map[i][j]);
                    getArea(i, j).add(map[i][j]);
                }
            }
        }
    }

    static Set<Integer> getArea(int y, int x) {

        int idx = -1;
        if (y <= 3) {

            if (x <= 3) {
                idx = 1;
            } else if (x <= 6) {
                idx = 2;
            } else {
                idx = 3;
            }

        } else if (y <= 6) {

            if (x <= 3) {
                idx = 4;
            } else if (x <= 6) {
                idx = 5;
            } else {
                idx = 6;
            }

        } else {

            if (x <= 3) {
                idx = 7;
            } else if (x <= 6) {
                idx = 8;
            } else {
                idx = 9;
            }

        }

        return area[idx];
    }

    private static class InputReader {
        StringTokenizer st;
        BufferedReader r;

        public InputReader(String filePath) throws FileNotFoundException {
            this(new FileReader(filePath));
        }

        public InputReader() {
            this(new InputStreamReader(System.in));
        }

        private InputReader(InputStreamReader reader) {
            r = new BufferedReader(reader);
            st = new StringTokenizer("");
        }

        public int nextInt() throws IOException {
            if (!st.hasMoreTokens()) st = new StringTokenizer(r.readLine());
            return Integer.parseInt(st.nextToken());
        }

        public char[] nextCharArr() throws IOException {
            return r.readLine().toCharArray();
        }
    }


}