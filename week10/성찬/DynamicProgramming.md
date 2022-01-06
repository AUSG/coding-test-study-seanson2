# DP
다이나믹 프로그래밍이란.
문제의 크기가 동적으로 변한다는 뜻이다.

# 꿀팁
문제의 규칙을 찾자.

1. 각 케이스를 직접 나열해보자. (생각해내기 어려울 때 까지)
2. 케이스 간 규칙을 찾자. 
3. 무엇으로 끝날지를 기준으로 찾으면 좋다.

# 실전

## 123더하기
문제: https://www.acmicpc.net/problem/9095

완전탐색?
N = 11만 생각해보자.
1 + 1 + 1 ... + 1 중복을 검사해야한다.
1 + 1 + 1 ... + 2 는 순서를 바꿔야 하니까 9개
1 + 1 + 1 ... + 3 은? 4는? 5는?

프로그램이 너무 복잡하고 연산 숫자가 너무 많다.

시간 제한 1초 (1억번의 연산)를 지키지 못하니까 다른 방법이 필요하다.

풀이과정: https://onedrive.live.com/redir?resid=C2ECCC1A6F04BD28%214903&page=Edit&wd=target%28%EC%83%88%20%EC%83%89%EC%85%98%201.one%7C478cb9ef-f4b0-894b-ac67-fd1e754d8a9a%2F%EC%A0%9C%EB%AA%A9%20%EC%97%86%EB%8A%94%20%ED%8E%98%EC%9D%B4%EC%A7%80%7C8b4d6caf-25fb-3c43-9f3f-28c1d94bd662%2F%29

## 이친수
문제: https://www.acmicpc.net/problem/2193
0 과 1로만 이루어져 있으며 1이 두번 연속으로 나타나지 않는 숫자 이친수를 구하라
ex) 1, 10, 100, 101, 1000, 1001 이친수
ex) 0_010101, 10_11_01 이친수 X

풀이과정: https://onedrive.live.com/redir?resid=C2ECCC1A6F04BD28%214903&page=Edit&wd=target%28%EC%83%88%20%EC%83%89%EC%85%98%201.one%7C478cb9ef-f4b0-894b-ac67-fd1e754d8a9a%2F%EC%A0%9C%EB%AA%A9%20%EC%97%86%EB%8A%94%20%ED%8E%98%EC%9D%B4%EC%A7%80%7Cd57fa865-59e7-b14d-91b3-bd02e0b645b8%2F%29