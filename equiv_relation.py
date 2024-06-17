def check_reflexive(A,R):
    for x in A:
        if (x,x) in R:
            continue
        else:
            return False
    return True

def check_symmetric(R):
    for (x,y) in R:
        if (y,x) in R:
            continue
        else:
            return False
    return True

def check_transitive(A,R):
    for (x,y) in R:
        for z in A:
            if (y,z) in R:
                if (x,z) in R:
                    continue
                else:
                    return False
    return True

def check_equivalance(A,R):
    if check_reflexive(A,R) and check_symmetric(R) and check_transitive(A,R):
        return True
    else:
        return False