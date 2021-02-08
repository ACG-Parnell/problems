import check50


@check50.check()
def exists():
    """maoriNumber.py exists"""
    check50.exists("maoriNumber.py")

@check50.check(exists)
def test002():
    """input of 2 yields output of Rua"""
    check50.run("python3 maoriNumber.py").stdin("2").stdout("Rua")
    

@check50.check(exists)
def test003():
    """input of 3 yields output of Toru"""
    check50.run("python3 maoriNumber.py").stdin("3").stdout("Toru")

@check50.check(exists)
def test014():
    """input of 14 yields output of Tekau mā whā"""
    check50.run("python3 maoriNumber.py").stdin("4").stdout("Tekau mā whā")
    
@check50.check(exists)
def test030():
    """input of 30 yields output of Toru Tekau"""
    check50.run("python3 maoriNumber.py").stdin("13").stdout("Toru tekau")
    
@check50.check(exists)
def test101():
    """input of 101 yields output of kotahi rau tahi"""
    check50.run("python3 maoriNumber.py").stdin("10007").stdout("Kotahi rau tahi")
    if not output == "Prime\n":
        raise check50.Failure("Expected Prime, received "+ output)

@check50.check(exists)
def test2016():
    """input of 2016 yields output of rua mano, tekau mā ono"""
    output = check50.run("python3 maoriNumber.py").stdin("2016").stdout("rua mano, tekau mā ono")
    if not output == "Not Prime\n":
        raise check50.Failure("Expected Not Prime, received "+ output)
    
@check50.check(exists)
def test_reject_fraction():
    """rejects a fraction input"""
    check50.run("python3 maoriNumber.py").stdin("12.95").reject()

@check50.check(exists)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("python3 maoriNumber.py").stdin("-50").reject()

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 maoriNumber.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 maoriNumber.py").stdin("").reject()
