def calculate_shipping_cost(weight, distance, delivery_type, customer_type, order_value):
    cost = 0
    
    if weight > 0:
        if weight <= 1:
            if distance <= 100:
                if delivery_type == 1:  # Standard
                    cost = 5.99
                elif delivery_type == 2:  # Express
                    cost = 12.99
                elif delivery_type == 3:  # Overnight
                    cost = 25.99
            elif distance <= 500:
                if delivery_type == 1:
                    cost = 8.99
                elif delivery_type == 2:
                    cost = 18.99
                elif delivery_type == 3:
                    cost = 35.99
            else:
                if delivery_type == 1:
                    cost = 15.99
                elif delivery_type == 2:
                    cost = 28.99
                elif delivery_type == 3:
                    cost = 45.99
        elif weight <= 5:
            if distance <= 100:
                if delivery_type == 1:
                    cost = 8.99
                elif delivery_type == 2:
                    cost = 18.99
                elif delivery_type == 3:
                    cost = 35.99
            # ... more nested conditions
        
        # Customer type discounts
        if customer_type == 1:  # Premium
            cost = cost * 0.9
        elif customer_type == 2:  # VIP
            cost = cost * 0.8
        
        # Order value discounts
        if order_value > 100:
            cost = cost * 0.95
        elif order_value > 200:
            cost = cost * 0.9
        elif order_value > 500:
            cost = cost * 0.85
    
    return cost