import Lab2.Lab2 as Lab2




def test_bmi_normal_weight():

    height=1.75
    weight=60
    output = Lab2.calculate_bmi(height,weight)
    x = Lab2.classify_bmi(output)
    assert(x==0)


def test_bmi_over_weight():
    height=1.75
    weight=99
    output = Lab2.calculate_bmi(height,weight)
    x = Lab2.classify_bmi(output)
    assert(x==1)
        

def test_bmi_under_weight():
    height=1.75
    weight=10
    output = Lab2.calculate_bmi(height,weight)
    x = Lab2.classify_bmi(output)
    assert(x==-1)