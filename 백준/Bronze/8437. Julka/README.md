# [Bronze V] Julka - 8437 

[문제 링크](https://www.acmicpc.net/problem/8437) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Julka zaskoczyła wczoraj w przedszkolu swoją wychowawczynię rozwiązując następującą zagadkę:</p>
<p>Julka는 어제 유치원에서 다음 수수께끼를 풀면서 가정교사를 놀라게 했습니다.</p>

<blockquote>Klaudia i Natalia mają razem 10 jabłek, ale Klaudia ma o 2 jabłka więcej niż Natalia. Ile jabłek ma każda z dziewczynek?</blockquote>
<blockquote>Klaudia와 Natalia는 함께 사과 10개를 가지고 있지만 Klaudia는 Natalia보다 2개 더 많은 사과를 가지고 있습니다. 각 소녀들은 몇 개의 사과를 가지고 있습니까?</blockquote>


<p>Julka odpowiedziała bez namysłu: Klaudia ma sześć jabłek, natomiast Natalia ma cztery jabłka.</p>
<p>Julka는 생각 없이 대답했습니다. Klaudia는 6개의 사과를 가지고 있고 Natalia는 4개의 사과를 가지고 있습니다.</p>

<p>Wychowywaczyni postanowiła sprawdzić, czy odpowiedź Julki nie była przypadkowa i powtarzała zagadkę, za każdym razem zwiększając liczby jabłek w zadaniu. Julka zawsze odpowiadała prawidłowo. Zaskoczona wychowawczyni chciała kontynuować ,,badanie'' Julki, ale przy bardzo dużych liczbach sama nie potrafiła szybko rozwiązać zagadki. Pomóż pani przedszkolance i napisz program, który będzie podpowiadał jej rozwiązania.</p>
<p>튜터는 Julka의 대답이 우발적이지 않은지 확인하기로 결정하고 과제에 사과의 수를 늘릴 때마다 수수께끼를 반복했습니다. Julka는 항상 올바르게 대답했습니다. 놀란 선생님은 Julka의 '연구'를 계속하고 싶었지만 너무 많은 숫자로 인해 스스로 퍼즐을 빨리 풀 수 없었습니다. 유치원 교사를 돕고 해결책을 제안하는 프로그램을 작성하십시오.</p>

<p>Napisz program, który:</p>
<ul>
	<li>wczyta (ze standardowego wejścia) liczbę jabłek, które mają razem obie dziewczynki oraz o ile więcej jabłek ma Klaudia,</li>
	<li>obliczy, ile jabłek ma Klaudia i ile jabłek ma Natalia,</li>
	<li>wypisze wynik (na standardowe wyjście).</li>
</ul>
<p>다음과 같은 프로그램을 작성하십시오.</p>
<ul>
	<li>(표준 입력에서) 두 소녀가 함께 가지고 있는 사과 수와 Klaudia가 가지고 있는 사과 수를 읽습니다.</li>
	<li>Klaudia의 사과 수와 Natalia의 사과 수를 계산합니다.</li>
	<li>결과를 씁니다(표준 출력에).</li>
</ul>


### 입력 

 <p>Wejście składa się z dwóch wierszy. Pierwszy wiersz zawiera liczbę wszystkich jabłek posiadanych przez dziewczynki, natomiast drugi - liczbę mówiącą, o ile więcej jabłek ma Klaudia. Obie liczby są całkowite i dodatnie. Wiadomo, że dziewczynki mają razem nie więcej niż 10<sup>100</sup> (jedynka i sto zer) jabłek. Jak widać, jabłka mogą być bardzo malutkie.</p>
 <p>입구는 두 줄로 되어 있습니다. 첫 번째 줄은 소녀들이 소유한 모든 사과의 수를 포함하고 두 번째 줄은 Klaudia가 얼마나 더 많은 사과를 가지고 있는지를 나타냅니다. 두 숫자 모두 정수와 양수입니다. 소녀들은 총 10,100 개 이하  의 사과를 가지고 있는 것으로 알려져 있습니다 . 보시다시피, 사과는 매우 작을 수 있습니다.</p>

### 출력 

 <p>Twój program powinien wypisać (na standardowe wyjście) w dwóch kolejnych wierszach dwie liczby całkowite, po jednej w wierszu. Pierwszy wiersz powinien zawierać liczbę jabłek Klaudii, natomiast drugi - liczbę jabłek Natalii. Wiadomo, że dziewczynki zawsze mają całe jabłka.</p>
 <p>당신의 프로그램은 (표준 출력에) 두 개의 연속적인 라인에 두 개의 정수를 한 줄에 하나씩 써야 합니다. 첫 번째 줄에는 Klaudia의 사과 개수가 포함되어야 하고 두 번째 줄에는 Natalia의 사과 개수가 포함되어야 합니다. 소녀들은 항상 사과를 통째로 가지고 있는 것으로 알려져 있습니다.</p>
