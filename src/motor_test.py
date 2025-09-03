#!/usr/bin/env python3
"""
Motor Test for Raspberry Pi Smart Car
Basic forward movement test only
"""

import RPi.GPIO as GPIO
import time

# Pin definitions (matching L298N documentation)
ENA = 18  # PWM pin for motor A - Physical Pin 12
IN1 = 17  # Physical Pin 11
IN2 = 27  # Physical Pin 13
IN3 = 22  # Physical Pin 15
IN4 = 23  # Physical Pin 16
ENB = 10  # PWM pin for motor B - Physical Pin 19

def setup():
    """Initialize GPIO settings"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set all pins as outputs
    GPIO.setup([ENA, IN1, IN2, IN3, IN4, ENB], GPIO.OUT)
    
    # Setup PWM with low frequency for smooth control
    pwm_a = GPIO.PWM(ENA, 1000)  # 1000 Hz frequency
    pwm_b = GPIO.PWM(ENB, 1000)
    pwm_a.start(0)  # Start with 0% duty cycle (off)
    pwm_b.start(0)
    
    return pwm_a, pwm_b

def cleanup():
    """Clean up GPIO settings"""
    GPIO.cleanup()

def forward(pwm_a, pwm_b, speed=15):
    """Move both motors forward at slow speed"""
    print(f"Moving FORWARD at {speed}% speed")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

def stop(pwm_a, pwm_b):
    """Stop both motors"""
    print("STOPPING motors")
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

def test_forward_only(pwm_a, pwm_b):
    """Run forward movement test only"""
    print("\n🚗 Starting FORWARD Movement Test 🚗")
    print("=" * 40)
    
    try:
        print("\nTesting FORWARD movement...")
        print("Watch the motors to see which direction they spin!")
        print("Press Ctrl+C to stop the test\n")
        
        forward(pwm_a, pwm_b, 15)  # Very slow speed
        
        # Keep running until user stops
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n⚠️ Test stopped by user")
    finally:
        stop(pwm_a, pwm_b)
        print("Motors stopped.")

def main():
    """Main test function"""
    print("🔧 L298N Motor Controller - FORWARD TEST ONLY")
    print("=" * 50)
    print("Pin Configuration:")
    print(f"ENA (Motor A Enable): GPIO {ENA} (Pin 12)")
    print(f"IN1: GPIO {IN1} (Pin 11)")
    print(f"IN2: GPIO {IN2} (Pin 13)")
    print(f"IN3: GPIO {IN3} (Pin 15)")
    print(f"IN4: GPIO {IN4} (Pin 16)")
    print(f"ENB (Motor B Enable): GPIO {ENB} (Pin 19)")
    print("\n⚠️  Make sure all connections are secure!")
    print("⚠️  This test will only move FORWARD!")
    print("⚠️  Watch the motor direction to identify correct wiring!")
    print("\nPress Ctrl+C to stop the test\n")
    
    pwm_a, pwm_b = setup()
    
    try:
        # Run forward test only
        test_forward_only(pwm_a, pwm_b)
        
    except KeyboardInterrupt:
        print("\n\n👋 Exiting motor test...")
    finally:
        stop(pwm_a, pwm_b)
        cleanup()
        print("GPIO cleaned up. Goodbye!")

if __name__ == "__main__":
    main()
