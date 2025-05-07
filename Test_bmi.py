import Lab2.bmi as bmi




def test_bmi_normal_weight():

    height=1.75
    weight=60
    output = bmi.calculate_bmi(height,weight)
    x = bmi.classify_bmi(output)
    assert(x==0)


def test_bmi_over_weight():
    height=1.75
    weight=99
    output = bmi.calculate_bmi(height,weight)
    x = bmi.classify_bmi(output)
    assert(x==1)
        

def test_bmi_under_weight():
    height=1.75
    weight=10
    output = bmi.calculate_bmi(height,weight)
    x = bmi.classify_bmi(output)
    assert(x==-1)