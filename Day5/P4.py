def make_counter():
    count = 0
    def increment():
        # keyword used inside nested function to declare that a variable 
        # belongs to nearest enclosing function scope
        nonlocal count
        count+=1
        return count