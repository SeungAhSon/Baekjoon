# [Bronze V] Арифметическая магия - 18096 

[문제 링크](https://www.acmicpc.net/problem/18096) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

수학(math)

### 문제 설명

<p>Дэвид Блейн попросил зрителя задумать два числа.  Затем он попросил перемножить два числа, большие каждого из задуманных на единицу,  вычесть из результата сначала одно задуманное число, затем другое, а затем --- их произведение, а полученный результат возвести в <mjx-container class="MathJax" jax="CHTML" style="font-size: 109.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>-ю степень.</p>

<p>David Blaine은 시청자에게 두 개의 숫자를 생각해 보라고 했습니다. 그런 다음 그는 두 숫자에 각각 1을 더한 값을 곱하고, 그 결과에서 첫 숫자와 두 숫자를 뺀 다음 두 숫자의 곱을 뺀 결과를 N 제곱한 결과를 요구했습니다.</p>

<p>После чего Дэвид внимательно вгляделся в лицо зрителя и правильно назвал получившийся результат. Ваша задача --- повторить фокус Дэвида. По заданному <mjx-container class="MathJax" jax="CHTML" style="font-size: 109.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> угадайте получившееся у зрителя число.</p>
<p>그 후 David는 시청자의 얼굴을주의 깊게 들여다보고 결과를 올바르게 불렀습니다. 당신의 임무는 David의 트릭을 반복하는 것입니다. 주어진 바에 따르면$N$시청자 번호를 맞춰보세요.</p>
<p>*정리하자면 ((x+1)(y+1)-x-y-xy)^N</p>

### 입력 

 <p>Входные данные содержат одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le N \le 1000$</span></mjx-container>).</p>
 <p>입력에 단일 정수가 포함됩니다.$N$ ($0 \le N \le 1000$).</p>
 
### 출력 

 <p>Выведите одно число --- получившийся у зрителя результат.</p>
 <p>단일 숫자 인쇄</p>

