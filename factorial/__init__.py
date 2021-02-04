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
def test0():
    """rejects a negative"""
    check50.run("python3 factorial.py").stdin("-5").reject()
