# serial-communication-python-arduino
data communication between Python and Arduino via serial port.

Sample Arduino Code:
```
int count = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("test");
  pinMode(13,OUTPUT);
}

void loop() {

     while (Serial.available() > 0) {
       int pixel = Serial.parseInt();
       if (Serial.read() =='\n') {
        count++;
        Serial.println(pixel);
        }
        trigger_led_on_success();

    }



    Serial.println(count);

} 

void trigger_led_on_success() {

      if (count == 784) {
      Serial.println(count);

        digitalWrite(13,HIGH);
        delay(3000);
        digitalWrite(13,LOW);
        delay(1000);

        
        digitalWrite(13,HIGH);
        delay(3000);
        digitalWrite(13,LOW);
    }

}
```
