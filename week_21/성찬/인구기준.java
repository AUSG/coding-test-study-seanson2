package 우체국_2141;

import java.io.*;
import java.util.*;

import org.junit.jupiter.api.Test;

class Main {

    static int N;

    static long[] populationSum;

    static City[] cities;

    static class City implements Comparable<City> {
        int position, population;

        public City(int position, int population) {
            this.position = position;
            this.population = population;
        }


        @Override
        public int compareTo(City o) {
            return Integer.compare(position, o.position);
        }
    }

    @Test
    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        Arrays.sort(cities);

        
        populationSum[0] = cities[0].population;
        for (int i = 1; i < N; i++) {
            populationSum[i] = cities[i].population + populationSum[i - 1];
        }

        // 인구 누적합의 절반
        long half = (populationSum[N - 1] + 1) / 2;

        for (int i = 0; i < N; i++) {
            if (half <= populationSum[i]) {
                System.out.println(cities[i].position);
                return;
            }
        }
    }

    private static void input() throws IOException {
        InputReader r = new InputReader("C:\\Users\\workspace\\boj\\src\\test\\java\\우체국_2141\\input.txt");

        N = r.nextInt();

        cities = new City[N];
        for (int i = 0; i < N; i++) {
            cities[i] = new City(r.nextInt(), r.nextInt());
        }

        populationSum = new long[N];
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
        }    }


}
