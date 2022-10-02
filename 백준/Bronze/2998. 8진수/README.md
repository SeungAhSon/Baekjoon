# [Bronze II] 8진수 - 2998 

[문제 링크](https://www.acmicpc.net/problem/2998) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>창영이는 여러 가지 진법을 공부하고 있다. 창영이는 어제 2진법을 배웠고, 오늘은 8진법을 배웠다. 이제, 2진법 수를 8진법 수로 변환하려고 한다.</p>

<p>창영이가 사용한 방법은 다음과 같다.</p>

<ol>
	<li>2진수의 길이가 3으로 나누어 떨어질 때 까지 수의 앞에 0을 붙인다.</li>
	<li>그 다음, 3자리씩 그룹을 나눈다.</li>
	<li>아래의 표를 참고해 8진수로 바꾼다.</li>
</ol>

<p>2진수가 주어졌을 때, 창영이가 사용한 방법을 이용해 8진수로 바꾸는 프로그램을 작성하시오.</p>

<table class="table table-bordered table-center-20 td-center">
	<tbody>
		<tr>
			<td>000</td>
			<td>0</td>
		</tr>
		<tr>
			<td>001</td>
			<td>1</td>
		</tr>
		<tr>
			<td>010</td>
			<td>2</td>
		</tr>
		<tr>
			<td>011</td>
			<td>3</td>
		</tr>
		<tr>
			<td>100</td>
			<td>4</td>
		</tr>
		<tr>
			<td>101</td>
			<td>5</td>
		</tr>
		<tr>
			<td>110</td>
			<td>6</td>
		</tr>
		<tr>
			<td>111</td>
			<td>7</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 2진수가 주어진다. 이 수는 100자리 이내이고, 첫 번째 자리는 1이다.</p>

### 출력 

 <p>첫째 줄에 8진수를 출력한다.</p>

