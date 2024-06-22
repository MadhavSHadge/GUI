#define ENA 10
#define IN1 8
#define IN2 9

void setup() {
  // Initialize the serial communication
  Serial.begin(9600);
  
  // Set the motor control pins as outputs
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming byte
    char command = Serial.read();
    
    // Forward command
    if (command == 'F') {
      int speed = Serial.parseInt(); // Read s
peed value (0-255)
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, speed);
    }
    
    // Backward command
    if (command == 'B') {
      int speed = Serial.parseInt(); // Read speed value (0-255)
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(ENA, speed);
    }
    
    // Stop command
    if (command == 'S') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 0);
    }
  }
}
