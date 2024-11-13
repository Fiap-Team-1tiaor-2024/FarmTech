#include <DHT.h>

#define DHTPIN 13          // Pino de conexão do DHT22
#define DHTTYPE DHT22      // Tipo do sensor DHT22
DHT dht(DHTPIN, DHTTYPE);

#define LDR_PIN 34         // Alterado para um pino analógico
#define PK_BUTTON_PIN1 25  // Botão para representar o sensor de Fósforo (P)
#define PK_BUTTON_PIN2 26  // Botão para representar o sensor de Potássio (K)
#define RELAY_PIN 4        // Pino do relé para a bomba de água

const unsigned long intervaloLeitura = 2000;
unsigned long ultimoTempo = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PK_BUTTON_PIN1, INPUT_PULLUP);  // Botão P
  pinMode(PK_BUTTON_PIN2, INPUT_PULLUP);  // Botão K
  pinMode(RELAY_PIN, OUTPUT);             // Relé da bomba
  dht.begin();
}

void loop() {
  unsigned long tempoAtual = millis();
  if (tempoAtual - ultimoTempo >= intervaloLeitura) {
    ultimoTempo = tempoAtual;

    // Leitura dos sensores
    bool isPDetected = digitalRead(PK_BUTTON_PIN1) == LOW;
    bool isKDetected = digitalRead(PK_BUTTON_PIN2) == LOW;
    float humidity = dht.readHumidity();
    
    if (isnan(humidity)) {
      Serial.println("Erro ao ler o sensor DHT22!");
      humidity = 0;  // Ou um valor padrão
    }

    int ldrValue = analogRead(LDR_PIN);

    // Critérios para acionar o relé
    bool needIrrigation = (humidity < 50) && (isPDetected || isKDetected) && (ldrValue < 2000);

    // Ativa ou desativa o relé com base na necessidade de irrigação
    digitalWrite(RELAY_PIN, needIrrigation ? HIGH : LOW);

    // Envia os dados para o monitor serial para armazenamento manual
    Serial.print("P: "); Serial.print(isPDetected);
    Serial.print(" K: "); Serial.print(isKDetected);
    Serial.print(" Humidity: "); Serial.print(humidity);
    Serial.print(" LDR(pH): "); Serial.print(ldrValue);
    Serial.print(" Relay: "); 
    if (!digitalRead(PK_BUTTON_PIN1)){
      digitalWrite(RELAY_PIN, HIGH);
      Serial.print("ON - Bomba de água ligada!");
    } else {
      digitalWrite(RELAY_PIN, LOW);
      Serial.print("OFF - Bomba de água desligada!");
    }
  }

}
