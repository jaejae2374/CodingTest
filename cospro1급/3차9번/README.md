## 문제9
모 매장에서는 팝업스토어를 열려고 합니다. 팝업스토어란 한정 기간 문을 여는 매장입니다. 팝업스토어는 k일 동안 연속해서 열 예정입니다. n일 동안의 추정 매출액이 주어질 때, 언제 팝업스토어를 열어야 가장 매출이 높을지 알아보려 합니다.

n일 간의 추정 매출액이 담긴 리스트 revenue와 팝업스토어를 열 날의 수 k가 매개변수로 주어질 때, 최대 매출액 합을 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
##### 매개변수 설명

추정 매출액이 담긴 리스트 revenue와 팝업스토어를 열 날의 수 k가 solution 함수의 매개변수로 주어집니다.

* revenue의 길이는 1 이상 200,000 이하입니다.
* revenue의 원소는 10,000 이하의 자연수입니다.
* k는 1 이상 100,000 이하이고, revenue의 길이보다 작거나 같습니다.

---
##### return 값 설명

최대 매출액 합을 return 해주세요.

---
##### 예시

| revenue | k | return |
|----------------|---|--------|
| [1, 1, 9, 3, 7, 6, 5, 10] | 4 | 28 |
| [1, 1, 5, 1, 1] | 1 | 5 |

##### 예시 설명

예시 #1
4일간 매출액 합이 최대가 되는 경우는 [7, 6, 5, 10]입니다. 따라서 최대 매출액은 28입니다.

예시 #2
1일간 매출액 합이 최대가 되는 경우는 [5]입니다. 따라서 최대 매출액은 5입니다.
