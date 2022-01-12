## `Programmers 위클리챌린지 피로도 Level2`

```java
import java.util.Arrays;

/**
 * created by Gyunny 2022/01/11
 * https://programmers.co.kr/learn/courses/30/lessons/87946
 */
public class Tired {
    public static int solution(int k, int[][] dungeons) {
        int answer = 0;

        Arrays.sort(dungeons, (int[] o1, int[] o2) -> {
            if ((o1[0] - o1[1]) < (o2[0] - o2[1])) {
                return 1;
            }

            return -1;
        });

        for (int i = 0; i < dungeons.length; ++i) {
            if (dungeons[i][0] <= k) { // 던전 참여 가능
                k -= dungeons[i][1];
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[][] list = {{80,20},{50,40},{30,10}};

        System.out.println(solution(80, list));
    }
}
```

위의 코드로 하면 `82.4/100` 이 나온다. 왜일까.. 일단 문제 보자마자 직관적으로 `배열 안에 값의 차이가 가장 큰거 먼저 던전을 가면 되겠다` 라는 생각하고 풀었음. 근데 이렇게 풀면 당연히 맞지 않는 반례가 존재할 것임.. 그래서 82.5점 나온듯

다른 사람들의 코드를 보니 다 `dfs`로 풀었다. 문제 보기 전에는 안떠올랐는데 `dfs`로 푼 거보니 그렇게도 풀 수 있겠다 싶었음. 순열, 조합과 연관되어 있는 느낌이었음. 이런 문제도 뭔가 코테에서 많이 나오는 유형이라 잘 익혀놓으면 좋겠다는 느낌도 들었음.



```java
class Solution {
    public static boolean check[];
    public static int ans = 0;
    
    public int solution(int k, int[][] dungeons) {
        check = new boolean[dungeons.length];
        
        dfs(k, dungeons, 0);
        
        return ans;
    }
    public static void dfs(int tired, int[][] dungeons, int cnt){
        
        for (int i = 0; i < dungeons.length; i++){
            if (!check[i] && dungeons[i][0] <= tired){
                check[i] = true;
                dfs(tired - dungeons[i][1], dungeons, cnt+1);
                check[i] = false;
            }
        }
        ans = Math.max(ans, cnt);
    }
}
```

즉, 위처럼 `dfs(백트래킹) + 순열/조합` 유형은 잘 나오니 많이 연습해두자.