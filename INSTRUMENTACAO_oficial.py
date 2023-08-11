from machine import ADC, Pin
import time
from utime import ticks_ms, sleep_ms
# Configuração do pino do sensor de corrente
pin_sensor = Pin(32, Pin.IN)
pin_tensao_bateria = Pin(34, Pin.IN)
# Configuração do pino analógico
adc_corrente = ADC(Pin(32))
adc_tensao_bateria = ADC(Pin(34))

start = 0
elapsed = 0
circMetric = 2.093  # wheel circumference (in meters)
circImperial = 0  # using 1 kilometer = 0.621371192 miles
speedk = 0  # holds calculated speed values in metric
speedm = 0  # holds calculated speed values in imperial

def ler_corrente(x2):
    valor_analogico = x2.read()
    tensao = valor_analogico * 3.3 / 4095  # Converter valor ADC para tensão
    corrente1 = (tensao - 2.291) / 0.066  # Calcular corrente usando o fator de sensibilidade do ACS712
    return corrente1
def tensao(x):
 r1 = 30000.0
 r2 = 7500.0
 for i in range(5000):
    tensaoDC = x.read()
    tensaoDC = tensaoDC * (0.000973)
    tensaoDC=  (tensaoDC +(tensaoDC / (r2/(r1+r2))))
    
 return tensaoDC
# Loop principal
while True:
    for i in range (1000):
       
       corrente2 = ler_corrente(adc_corrente)
       corrente2 = corrente2 + corrente2
       corrente2 = corrente2/1000
       tensaobateria = tensao(adc_tensao_bateria)
       tensaoDC1 = adc_tensao_bateria.read()
       
    print("corrente: {:.2f} A        Tensao bateria: {:.2f} V".format(corrente1, tensaobateria))
    
    time.sleep(0.0001)
