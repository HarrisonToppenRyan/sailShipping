def costGroundShipping(weight):
  cost = 0
  premiumGroundShipping = 125
  if weight <= 2:
    cost = 1.50
    return ((weight * cost) + 20.00)
  elif (weight > 2) and (weight <= 6):
    cost = 3.00
    return ((weight * cost) + 20.00)
  elif (weight > 6) and (weight <= 10):
    cost = 4.00
    return ((weight * cost) + 20.00)
  else:
    cost = 4.75
    return ((weight * cost) + 20.00)

def costDroneShipping(weight):
  cost = 0 
  if weight <= 2:
    cost = 4.50
    return (weight * cost)
  elif (weight > 2) and (weight <= 6):
    cost = 9.00
    return (weight * cost)
  elif (weight > 6) and (weight <= 10):
    cost = 12.00
    return (weight * cost)
  else:
    cost = 14.25
    return (weight * cost) 


def total(weight):
    if (costGroundShipping(weight)) > 125 and (costDroneShipping(weight) > 125):
        print("The cheapest way to ship a", weight, "lb package is using premium ground shipping and it will cost $125.00.")

    elif costGroundShipping(weight) > costDroneShipping(weight):
        print("The cheepest way to ship a", weight, "package is using drone shipping and it will cost you $",costDroneShipping(weight))
    
    elif costGroundShipping(weight) < costDroneShipping(weight):
        print("The cheepest way to ship a", weight, "lb package is using ground shipping and it will cost you $",costGroundShipping(weight))



print(total(41.8))