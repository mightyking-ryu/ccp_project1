# Simple Interactive Calculator

## 🔍 프로젝트 개요

이 프로젝트는 간단한 **대화형 계산기(Interactive Calculator)** 를 구현하는 것으로, 다음과 같은 기능을 제공합니다:
- 사칙연산 (덧셈, 뺄셈, 곱셈, 나눗셈)
- 몫과 나머지 계산
- 제곱과 순열/조합 계산
- 제곱근, 최대공약수(GCD) 계산
- 이진법 및 십진법 변환
- 자연상수(e) 및 원주율(π) 계산

사용자는 특정 입력 형식을 통해 계산식을 입력하고, 계산기는 해당 결과를 출력한 뒤 다음 입력을 대기합니다. 잘못된 입력이 주어지면 적절한 에러 메시지를 출력합니다.

---

## ⚙️ 주요 기능

| 입력 형식                  | 설명                                           |
|---------------------------|------------------------------------------------|
| `a + b`                   | 실수 `a`와 `b`의 합 계산                      |
| `a - b`                   | 실수 `a`와 `b`의 차 계산                      |
| `a * b`                   | 실수 `a`와 `b`의 곱 계산                      |
| `a / b`                   | 실수 `a`를 `b`로 나눈 값 계산                 |
| `a // b`                  | 정수 `a`를 `b`로 나눈 몫 계산                 |
| `a % b`                   | 정수 `a`를 `b`로 나눈 나머지 계산             |
| `a ^ b`                   | `a`의 `b`제곱 계산                            |
| `a P b`                   | 정수 `a`와 `b`에 대해 순열 계산               |
| `a C b`                   | 정수 `a`와 `b`에 대해 조합 계산               |
| `r a`                     | 실수 `a`에 대해 제곱근 계산 (뉴턴 근사법 사용)|
| `g a, b`                  | 정수 `a`와 `b`의 GCD 계산 (유클리드 호제법 사용)|
| `b a`                     | 정수 `a`를 이진수로 변환                      |
| `d a`                     | 이진수 `a`를 십진수로 변환                    |
| `e`                       | 자연상수 계산 (테일러 급수 사용)              |
| `pi`                      | 원주율 계산 (라이프니츠 급수 사용)            |
| `q`                       | 프로그램 종료                                  |

출력값이 실수일 경우, 소수점 이하 셋째 자리까지 표시됩니다.

---

## 🛠️ 구현 세부 사항

### 1. 뉴턴 근사법을 이용한 제곱근 계산
- 초기 추정값으로 시작해 연속적으로 평균값을 계산하며 근사치를 구합니다.
- 계산 종료 조건: 연속된 두 결과의 차이가 `MAX_ERROR = 0.00001`보다 작아질 때.

  ![Newton Method Formula](https://od.lk/s/MzhfMjgxMzU0NjZf/equation1.jpg)

### 2. 유클리드 호제법을 이용한 GCD 계산
1. 두 정수 중 큰 값을 `M`에, 작은 값을 `N`에 할당.
2. `M`을 `N`으로 나누고 나머지를 `R`로 설정.
3. `R`이 0이 아니면 `M`을 `N`으로, `N`을 `R`로 설정하고 반복.
4. `R`이 0이 될 때 `N`이 GCD.

    ![Euclid's Algorithm](https://od.lk/s/MzhfMjgxMzU0Njdf/equation2.jpg)

### 3. 테일러 급수를 이용한 자연상수 계산
- 테일러 급수는 다음 식을 사용:

  ![Taylor Series](https://od.lk/s/MzhfMjgxMzU0Njhf/equation3.jpg)

- 연속된 두 결과의 차이가 `MAX_ERROR`보다 작아질 때까지 계산.

### 4. 라이프니츠 급수를 이용한 원주율 계산
- 다음 식을 사용하여 π 값을 계산:

  ![Leibniz Formula](https://od.lk/s/MzhfMjgxMzU0Njlf/equation4.jpg)

- 연속된 두 결과의 차이가 `MAX_ERROR`보다 작아질 때까지 반복.

---

## 🖥️ 프로그램 동작 시나리오
1. 프로그램 실행 후 `Enter mathematical expression : ` 메시지가 출력됩니다.
2. 위의 입력 형식 중 하나를 입력하면 계산 결과가 출력됩니다.
3. `q`를 입력하면 프로그램이 종료됩니다.

### 입출력 예시
```
Enter mathematical expression : 3 + 5
8.000

Enter mathematical expression : 9 // 2
4

Enter mathematical expression : 16 r
4.000

Enter mathematical expression : q
Goodbye!
```

---

## 🚨 에러 처리
- **알 수 없는 연산 기호**: `Unknown expression`
- **0으로 나누기**: `Division by zero error`
- 그 외 사용자가 항상 올바르게 입력한다고 가정.

---

## 📂 프로젝트 구조
```
|-- ccp_project1/
|   |-- main.py             # 메인 프로그램 파일
|   |-- README.md           # 프로젝트 설명 파일
```

---

## ✨ 참고 자료
- Structure and Interpretation of Computer Programs (1985)
- [Newton's Method - Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_method)
- [Euclid's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Taylor Series - Wikipedia](https://en.wikipedia.org/wiki/Taylor_series)
- [Leibniz Formula - Wikipedia](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
