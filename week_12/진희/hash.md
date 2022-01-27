## 알고리즘 스터디 나의 목표

소마 코테에 합격하는 것이 목표
다양한 문제를 접해보고, 개념을 확실하게 정리하려고 한다.

1. 기초/고급 알고리즘
   - https://ryute.tistory.com/m/33
   - https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit
2. 웹
   - 추천해주세요..!!
3. SQL
   - https://programmers.co.kr/learn/challenges?tab=sql_practice_kit

<br>

## 해시

[코딩테스트 연습 - 완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576)

### **문제 설명**

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

| participant                                       | completion                               | return   |
| ------------------------------------------------- | ---------------------------------------- | -------- |
| ["leo", "kiki", "eden"]                           | ["eden", "kiki"]                         | "leo"    |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko"  |
| ["mislav", "stanko", "mislav", "ana"]             | ["stanko", "ana", "mislav"]              | "mislav" |

### 입출력 예 설명

예제 #1"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

### 코드

```
def solution(participant, completion):
    dic = {}
    temp = 0
    answer = ''
    for part in participant :
        dic[hash(part)] = part
        temp += hash(part)
    for comp in completion :
        temp -= hash(comp)

    answer = dic[temp]
    return answer
```

### 풀이

- dic : 빈 딕셔너리를 만들어 해시 테이블을 만들었다.
- Key : participant의 hash 값
- Value : participant 값
- temp : participant 해시값을 모두 더하고 completion의 해시값을 모두 빼면 마지막 한 사람의 해시값만 남게 된다. 이 값을 Key로 해서 value를 return 한다.

![](https://images.velog.io/images/ginee_park/post/a4794096-99c0-4d31-941a-596298646078/image.png)
