# [Gold I] Bicycle puzzle - 11118 

[문제 링크](https://www.acmicpc.net/problem/11118) 

### 성능 요약

메모리: 118940 KB, 시간: 320 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 제출 일자

2025년 4월 3일 08:41:31

### 문제 설명

<p>Per and Gunnar has found a wonderful online bicycle picture puzzle flash solitaire game, and since they are very competitive, they want to find out who is best. The purpose of the game is to descramble a picture of a bicycle. At the start of each game, the picture of the bicycle is cut into W times H equally sized rectangles and scrambled randomly. Then the player repeatedly chooses two arbitrary rectangles and swaps them. He continues to swap rectangles until the picture is complete again. The game keeps track of the number of swaps, which is the score for that particular playthrough.</p>

<p>After Gunnar has played a game, he sends his score (along with W and H) to Per, and challenges Per to beat this score. Per soon realizes that if he is unlucky with the scrambling, it is impossible to beat Gunnar’s score.</p>

<p>Per quickly writes a program to find out the probability that he can beat Gunnar’s score (assuming that all scrambled pictures are equally probable) if he plays optimally. But he is not sure whether his program is correct and wants to verify its correctness by challenging you to write the same program.</p>

### 입력 

 <p>The first line of the input consists of a single number T, the number of scenarios. Each scenario is given by a line with three integers W, H and S, where S is Gunnar’s last score.</p>

<ul>
	<li>0 < T ≤ 150</li>
	<li>0 < W ≤ 5</li>
	<li>0 < H ≤ 4</li>
	<li>0 ≤ S ≤ W · H</li>
	<li>When comparing two scores, the lowest one is best</li>
</ul>

### 출력 

 <p>For each scenario, output a line with the probability that Per beats Gunnar’s score. Format the probability as an irreducible fraction where the numerator and the denominator are separated by /. Output only the numerator if the answer is an integer.</p>

