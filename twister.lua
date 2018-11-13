#!/bin/lua

arto = {"mano destra", "mano sinistra", "piede destro", "piede sinistro"}
colore = {"verde", "giallo", "blu", "rosso"}
urandom = io.open("/dev/urandom", "rb")
seed = 0
for i = 0, 7 do seed = seed + urandom:read(1):byte() * (256 ^ i) end
math.randomseed(seed)
urandom:close()

function play(name)
  os.execute("paplay '" .. name .. "'.wav")
end

print("Premi enter per sentire la mia voce. ESC + enter per uscire.")
while true do
  local key = io.read()
  if not key or key:byte() == 27 then return end
  local arto, colore, numero = arto[math.random(#arto)], colore[math.random(#colore)], math.random(6)
  io.write(arto, "\t", colore, "\t", numero, "\t"):flush()
  play(arto) play(colore) play(numero)
end
