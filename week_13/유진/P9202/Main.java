package DAY03.P9202;

import java.io.BufferedReader;
import java.io.InputStreamReader;

// 주석만 보면서 다시 풀어보자...
// Trie - 중요!
// 이 문제 난이도 정도로 프로 시험 출제

public class Main {

    static int W,N;
    static Node root = new Node();
    static char[][] map;
    static boolean[][] visited;
    static int sum, count;
    static StringBuilder sb;
    static String answer;
    static int[] dx = {-1, -1, -1, 1, 1, 1, 0, 0};
    static int[] dy = {-1, 0, 1, -1, 0, 1, -1, 1};
    static int[] score = {0, 0, 0, 1, 1, 2, 3, 5, 11};


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        W = Integer.parseInt(br.readLine());
        // 사전에 단어 insert
        for(int w=0 ; w<W ; w++){
            insertTrieNode(br.readLine());
        }
        br.readLine();

        N = Integer.parseInt(br.readLine());
//        StringBuilder resultSb = new StringBuilder();
        for(int n=0 ; n<N ; n++){
            visited = new boolean[4][4];
            map = new char[4][4];
            answer = "";
            sum = 0;
            count = 0;
            sb = new StringBuilder();

            for(int i=0 ; i<4 ; i++){
                String in = br.readLine();
                for(int k=0 ; k<4 ; k++){
                    map[i][k] = in.charAt(k);
                }
            }

            br.readLine();
            for(int y=0 ; y<4 ; y++){
                for(int x=0 ; x<4 ; x++) {
                    // 출발 가능 조건 -> root가 해당 child를 가지면
                    if(root.hasChild(map[y][x])) {
                        search(y,x,1,root.getChild(map[y][x]));
                    }
                }
            }

            root.clearHit();
            System.out.println(sum + " " + answer + " " + count);
        }
    }

    // DFS
    static void search(int y, int x, int length, Node node) {
        // 1. 체크인 - history 체크
        visited[y][x] = true;
        sb.append(map[y][x]);
        // 2. 목적지에 도달하였는가?
        if(node.isEnd && !node.isHit) {
            sum += score[length];
            count++;
            node.isHit = true;
            String foundWord = sb.toString();
            if(compare(answer, foundWord) > 0){
                answer = foundWord;
            }
        }
        // 3. 연결된 곳을 순회 -> 8방
        for(int i=0 ; i<8 ; i++) {
            int ty = y + dy[i];
            int tx = x + dx[i];
            // 4. 가능한가? - map 경계, 방문하지 않았는지, node가 해당 자식을 가지고 있는지
            // map 경계 체크
            if(0 <= ty && ty < 4 && 0 <= tx && tx < 4){
                // 방문 여부 & 자식 존재 여부
                if(!visited[ty][tx] && node.hasChild(map[ty][tx])){
                    // 5. 간다.
                    search(ty, tx, length+1, node.getChild(map[ty][tx]));
                }
            }
        }
        // 6. 체크아웃 - history 빼주기
        visited[y][x] = false;
        sb.deleteCharAt(length-1);
    }

    static void insertTrieNode(String word) {
        char c;
        Node curNode = root;
        for(int i=0 ; i<word.length() ; i++){
            c = word.charAt(i);
            // 해당 알파벳이 child 배열에 없을 경우 생성
            if(!curNode.hasChild(c)) {
                curNode.children[c-'A'] = new Node();
            }
            curNode = curNode.getChild(c);
        }
        // 위 반복문이 끝났을 때는, current가 맨 끝 철자를 가리키고 있기 때문에
        // end 마킹
        curNode.isEnd = true;
    }

    // 이런 건 따로 메서드로 빼서 작업하는 게 수월하다
    static int compare(String arg0, String arg1) {
        // 길이 내림차순
        int comp = Integer.compare(arg1.length(), arg0.length());
        // 길이가 같다면 알파벳 빠른 거부터
        if(comp == 0){
            return arg0.compareTo(arg1);
        } else{
            return comp;
        }
    }
}

class Node {
    Node[] children = new Node[26];
    boolean isEnd;
    boolean isHit;

    boolean hasChild(char c){
        return children[c-'A'] != null;
    }

    Node getChild(char c) {
        return children[c - 'A'];
    }

    void clearHit() {
        isHit = false;
        for (int i = 0; i < children.length; i++) {
            Node child = children[i];
            if(child != null) {
                child.clearHit();
            }
        }
    }
}