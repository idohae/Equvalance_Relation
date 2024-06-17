# Equvalance_Relation
정의역 집합과 관계집합을 set 형태로 넘겨주면 동치관계를 판별하는 코드이다.

---
## functions
[`check_reflexive`](#check_reflexive(A,R))
[`check_symmetric`](#check_symmetric(R))
[`check_transitive`](#check_transitive(A,R))
[`check_equivalance`](#check_equivalance(A,R))

## 1. check_reflexive(A,R)[▲](#functions)
```python
def check_reflexive(A,R):
   for x in A:
       if (x,x) in R:
           continue
       else:
           return False
   return True
```

## 2. check_symmetric(R)
```python
def check_symmetric(R):
    for (x,y) in R:
        if (y,x) in R:
            continue
        else:
            return False
    return True
```

## 3. check_transitive(A,R)
```python
def check_transitive(A,R):
    for (x,y) in R:
        for z in A:
            if (y,z) in R:
                if (x,z) in R:
                    continue
                else:
                    return False
    return True
```

## 4. check_equivalance(A,R)
```python
def check_equivalance(A,R):
    if check_reflexive(A,R) and check_symmetric(R) and check_transitive(A,R):
        return True
    else:
        return False
```
