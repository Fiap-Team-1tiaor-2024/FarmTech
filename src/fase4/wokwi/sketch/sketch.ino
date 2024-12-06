#include <DHT.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

#define DHTPIN 13          // Pino de conexão do DHT22
#define DHTTYPE DHT22      // Tipo do sensor DHT22
DHT dht(DHTPIN, DHTTYPE);

#define LDR_PIN 34         // Alterado para um pino analógico
#define PK_BUTTON_PIN1 25  // Botão para representar o sensor de Fósforo (P)
#define PK_BUTTON_PIN2 26  // Botão para representar o sensor de Potássio (K)
#define RELAY_PIN 4        // Pino do relé para a bomba de água

const unsigned int intervaloLeitura = 2000;
unsigned int ultimoTempo = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PK_BUTTON_PIN1, INPUT_PULLUP);  // Botão P
  pinMode(PK_BUTTON_PIN2, INPUT_PULLUP);  // Botão K
  pinMode(RELAY_PIN, OUTPUT);             // Relé da bomba
  dht.begin();

  lcd.begin(16, 2); // Nº de Colunas e Linhas do Display
  lcd.init(); // Inicializa o Display
  lcd.backlight(); // Liga o BackLight
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
      humidity = 0;  // Ou um valor padrão
    }

    int ldrValue = analogRead(LDR_PIN);

    // Critérios para acionar o relé
    bool needIrrigation = (humidity < 50) && (isPDetected || isKDetected) && (ldrValue < 2000);

    // Ativa ou desativa o relé com base na necessidade de irrigação
    digitalWrite(RELAY_PIN, needIrrigation ? HIGH : LOW);

    // Envia os dados para o Serial Plotter
    Serial.print("Humidity:");
    Serial.print(humidity);
    Serial.print(" LDR:");
    Serial.print(ldrValue);
    Serial.print(" P:");
    Serial.print(isPDetected);
    Serial.print(" K:");
    Serial.print(isKDetected);
    Serial.print(" Relay:");
    Serial.println(needIrrigation);


    lcd.setCursor(0,0); // Coluna 0, Linha 0
    lcd.print("LDR:");  
    lcd.println(ldrValue);
    
    lcd.setCursor(0,1);
    lcd.print("Humidity:"); 
    lcd.println(humidity);

    lcd.setCursor(0,2);
    lcd.print("Relay:"); 
    lcd.println(needIrrigation);
    
    lcd.setCursor(0,3);
    lcd.print("P:"); 
    lcd.println(isPDetected);

    lcd.setCursor(5,3);
    lcd.print("K:"); 
    lcd.println(isKDetected);


    delay(3000);
  }
}
