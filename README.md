# Equvalance_Relation
정의역 집합과 관계집합을 set 형태로 넘겨주면 동치관계를 판별하는 코드이다.

---
## 동치의 조건
* 반사적(reflexive)   
    정의역 집합에 속하는 원소 a에 대해 (a,a)의 관계가 모두 존재해야함.
* 대칭적(symmetric)   
    정의역 집합에 속하는 원소 a,b에 대해 (a,b)의 관계가 존재할 경우 항상 (b,a)의 관계도 존재해야함.
* 추이적(transitive)   
    정의역 집합에 속하는 원소 a,b,c에 대해 (a,b),(b,c) 두 관계가 존재할 때에 항상 (c,a)의 관계도 존재해야함.

---
## Functions
[`check_reflexive(A,R)`](#check_reflexiveAR)
[`check_symmetric(A)`](#check_symmetricR)
[`check_transitive(A,R)`](#check_transitiveAR) →
[`check_equivalance(A,R)`](#check_equivalanceAR)   

정의역 집합 A와 관계집합 R을 입력으로 받아 반사, 대칭, 추이를 각각 판별하여 모두 만족하는지 판별한다.   

### check_reflexive(A,R)[▲](#Functions)   
> 반사적 성질 판별
> ```python
> def check_reflexive(A,R):
>    for x in A:
>        if (x,x) in R:
>            continue
>        else:
>            return False
>    return True
> ```
> 정의역 집합에 있는 모든 원소에 대해 관계집합에 반사 관계가 존재하면 `continue`, 모두 반사를 만족하여 `True`를 반환.   
> 하나의 원소라도 반사 관계를 만족하지 않으면 `False`를 반환.

### check_symmetric(R)[▲](#Functions)   
> 대칭적 성질 판별
> ```python
> def check_symmetric(R):
>     for (x,y) in R:
>         if (y,x) in R:
>             continue
>         else:
>             return False
>     return True
> ```
> 관계집합의 관계쌍을 모두 가져와 대칭 관계가 존재하면 `continue`, 모두 대칭을 만족하여 `True` 반환.   
> 하나의 관계쌍이라도 대칭 관계가 존재하지 않으면 `False`를 반환.

### check_transitive(A,R)[▲](#Functions)   
> 추이적 성질 판별
> ```python
> def check_transitive(A,R):
>     for (x,y) in R:
>         for z in A:
>             if (y,z) in R:
>                 if (x,z) in R:
>                     continue
>                 else:
>                     return False
>     return True
> ```
> 관계집합의 관계쌍 (a,b)를 차례로 가져와, 해당 관계쌍의 치역 b를 정의역으로 갖고 정의역 집합의 원소 하나 c를 치역으로 갖는 관계쌍 (b,c)가 존재할 경우,   
> 첫 관계쌍의 정의역과 정의역 집합에서 뽑은 원소 사이의 관계 (a,c) 또한 존재하면 `continue`, 모두 추이를 만족하여 `True` 반환.   
> 앞의 경우를 만족하는데 (a,c)가 존재하지 않으면 `False`를 반환.   
> 앞의 경우를 만족하지 않는 경우는 판별하지 않음.

### check_equivalance(A,R)[▲](#Functions)   
> 동치 관계 판별
> ```python
> def check_equivalance(A,R):
>     if check_reflexive(A,R) and check_symmetric(R) and check_transitive(A,R):
>         return True
>     else:
>         return False
> ```   
> 앞의 반사, 대칭, 추이의 성질을 판별하는 함수를 호출하여 반환값이 모두 `True`인 경우에만 `True`를 반환.   
> 하나라도 `False`일 경우 동치관계가 아니므로 `False`를 반환.
