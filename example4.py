class Order:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = items
        self.status = "pending"
    
    def calculate_total(self, customer, tax_service, discount_service):
        subtotal = 0
        for item in self.items:
            subtotal += item.price * item.quantity
        
        # Feature envy - accessing too much of customer object
        if customer.membership_type == "premium":
            if customer.years_active > 5:
                discount = discount_service.get_loyalty_discount(customer.years_active)
            else:
                discount = discount_service.get_premium_discount()
        elif customer.membership_type == "vip":
            discount = discount_service.get_vip_discount(customer.total_purchases)
        else:
            discount = 0
        
        discounted_total = subtotal - (subtotal * discount)
        
        # More feature envy
        tax_rate = tax_service.get_tax_rate(customer.address.state, customer.address.country)
        tax_amount = discounted_total * tax_rate
        
        return discounted_total + tax_amount
    
    def send_confirmation_email(self, customer, email_service):
        # Feature envy - should customer handle its own email preferences?
        if customer.email_preferences.order_confirmations:
            subject = f"Order Confirmation - #{self.id}"
            body = f"Dear {customer.first_name} {customer.last_name}, your order has been confirmed."
            email_service.send_email(customer.email, subject, body)
    
    def update_inventory(self, inventory_service):
        for item in self.items:
            inventory_service.reduce_stock(item.product_id, item.quantity)