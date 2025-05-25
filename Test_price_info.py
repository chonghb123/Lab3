
import price_info as price

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost_of_shopping():
    test_price = 46.75
    total = price.total_cost_shopping()
    assert(total == test_price)
      
def test_cost_of_fruit():
    fruit = 'apple'
    quantity =10
    test_cost = 12
    cost = price.cost_of_fruits(fruit, quantity)
    assert(cost == test_cost)