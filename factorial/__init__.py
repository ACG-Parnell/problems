import check50

@check50.check()
def exists():
    """factorial.py exists."""
    check50.exists("factorial.py")

@check50.check(exists)
def Testfive():
    """responds to 5"""
    check50.run("python3 factorial.py").stdin("5").stdout("120").exit(0)

@check50.check(exists)
def TestNine():
    """responds to 9"""
    check50.run("python3 factorial.py").stdin("9").stdout("362880").exit(0)
    
@check50.check(exists)
def Test0099():
    """responds to 99"""
    check50.run("python3 factorial.py").stdin("99").stdout("933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000").exit(0)
    
@check50.check(exists)
def testNegative():
    """rejects a negative"""
    check50.run("python3 factorial.py").stdin("-5").reject()
