class UserManager:
    def __init__(self):
        self.users = []
        self.db_connection = None
        self.email_service = None
    
    def create_user(self, name, email, password, age, address, phone):
        # Validation
        if len(name) < 2 or len(name) > 50:
            return False
        if "@" not in email or "." not in email:
            return False
        if len(password) < 8:
            return False
        if age < 18 or age > 120:
            return False
        
        # Hash password
        import hashlib
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Create user
        user = {
            'id': len(self.users) + 1,
            'name': name,
            'email': email,
            'password': hashed_password,
            'age': age,
            'address': address,
            'phone': phone,
            'created_at': '2024-01-01',  # Hardcoded date
            'is_active': True
        }
        
        # Save to database
        self.users.append(user)
        
        # Send welcome email
        email_body = f"Welcome {name}! Your account has been created."
        print(f"Sending email to {email}: {email_body}")
        
        # Log activity
        print(f"User {name} created successfully")
        
        return True
