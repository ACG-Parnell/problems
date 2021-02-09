import check50

@check50.check()
def exists():
    """sara.py exists."""
    check50.exists("sara.py")

@check50.check(exists)
def route1():
    """check the route YYYY."""
    check50.run("python3 sara.py").stdin("Y").stdin("Y").stdin("Y").stdin("Y").stdout("Best cake ever!").exit(0)
    
@check50.check(exists)
def route2():
    """check the route YYYN."""
    check50.run("python3 sara.py").stdin("Y").stdin("Y").stdin("Y").stdin("N").stdout("Boom! Explosion!").exit(0)
    
@check50.check(exists)
def route3():
    """check the route YYNN"""
    check50.run("python3 sara.py").stdin("Y").stdin("Y").stdin("N).stdin("N").stdout("Butterflies are evil").exit(0)

@check50.check(exists)
def route4():
    """check the route YYNYY."""
    check50.run("python3 sara.py").stdin("Y").stdin("Y").stdin("N").stdin("Y").stdin("Y").stdout("Cursed!").exit(0)
    
@check50.check(exists)
def route6():
    """check the route YNN."""
    check50.run("python3 sara.py").stdin("Y").stdin("N").stdin("N").stdout("Happy end").exit(0)
    
@check50.check(exists)
def route7():
    """check the route YNYN."""
    check50.run("python3 sara.py").stdin("Y").stdin("N").stdin("Y").stdin("N").stdout("No!").exit(0)
    
@check50.check(exists)
def route8():
    """check the route YNYY."""
    check50.run("python3 sara.py").stdin("Y").stdin("N").stdin("Y").stdin("Y").stdout("Poison!").exit(0)

@check50.check(exists)
def route9():
    """check the route NY."""
    check50.run("python3 sara.py").stdin("N").stdin("Y").stdout("Kidnapped!").exit(0)
    
@check50.check(exists)
def route10():
    """check the route NN."""
    check50.run("python3 sara.py").stdin("N").stdin("N").stdout("Happy ending").exit(0)
