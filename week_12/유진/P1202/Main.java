package DAY03.P1202;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Jewelry {
    int weight;
    int cost;

    public Jewelry(int weight, int cost) {
        this.weight = weight;
        this.cost = cost;
    }

    public int getWeight() {
        return weight;
    }

    public int getCost() {
        return cost;
    }
}

public class Main {

    static int N, K, M, V;
    static long C;
    static List<Jewelry> jewel;
    static List<Long> bag;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Jewelry> pq = new PriorityQueue<>(Comparator.comparingInt(Jewelry::getCost).reversed());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        jewel = new ArrayList<>();
        for(int i=0 ; i<N ; i++){
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());
            jewel.add(new Jewelry(M, V));
        }
        Collections.sort(jewel, Comparator.comparingInt(Jewelry::getWeight));

        bag = new ArrayList<>();
        for(int i=0 ; i<K ; i++){
            C = Long.parseLong(br.readLine());
            bag.add(C);
        }
        Collections.sort(bag);

        int curJ = 0;
        long total = 0;
        for(int i=0 ; i<K ; i++) {
            long curBag = bag.get(i);

            while(curJ < N && jewel.get(curJ).weight <= curBag) {
                pq.offer(jewel.get(curJ++));
            }

            if(!pq.isEmpty()){
                total += pq.poll().cost;
            }
        }
        System.out.println(total);
    }
}
