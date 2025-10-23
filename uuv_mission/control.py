class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0
    
    def compute_control(self, reference, measurement):
        # Calculate error
        error = reference - measurement
        
        # PD control law
        control_action = self.kp * error + self.kd * (error - self.previous_error)
        
        # Update previous error for next iteration
        self.previous_error = error
        
        return control_action
    
    def reset(self):
        """Reset controller state."""
        self.previous_error = 0.0