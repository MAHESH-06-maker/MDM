import tkinter as tk 
root = tk.Tk()
root.title("EM Spectrum")
root.geometry("1000x300")
bands = [
    ("VLF", "3-30 kHz", "Submarine", "red"),
    ("LF", "30-300 kHz", "Navigation", "orange"),
    ("MF", "300 kHz-3 MHz", "AM Radio", "yellow"),
    ("HF", "3-30 MHz", "Shortwave", "green"),
    ("VHF", "30-300 MHz", "FM Radio TV", "cyan"),
    ("UHF", "300 MHz-3 GHz", " Bluetooth 4G", "blue"),
    ("SHF", "3-30 GHz", "5Ghz Wi-Fi, Satellite", "purple"),
    ("EHF", "30-300 GHz", "5G mmWave", "pink"),
    ("Infrared", "300 GHz-400 THz", "Remote", "orange"),
    ("Visible", "400-800 THz", "Light", "green"),
    ("UV", "800 THz-30 PHz", "Sterilisation", "violet"),
    ("X-ray", "30 PHz-30 EHz", "Medical", "gray"),
    ("Gamma", "Above 30 EHz", "Nuclear", "Brown")
]
frame = tk.Frame(root)
frame.pack(expand=True)
for name , freq , use , color in bands:
    tk.Label(frame , text=name+" \n "+freq+" \n "+use+" \n ", bg=color, width=15 , height=5).pack(side="left")
frame.mainloop()




import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, N in zip(axes, [3, 7]):
    for q in range(-3, 4):
        for r in range(-3, 4):
            if max(abs(q), abs(r), abs(q + r)) > 3:
                continue
            # Find hexagon position
            x = math.sqrt(3) * (q + r / 2)
            y = 1.5 * r
            # Find frequency group
            if N == 3:
                group = (q + 2 * r) % N
            else:
                group = (3 * q + r) % N
            # Draw hexagon
            hexagon = RegularPolygon(
                (x, y), 6, radius=1,
                orientation=math.pi / 6,
                facecolor=plt.cm.tab10(group),
                edgecolor="black"
            )
            ax.add_patch(hexagon)
            ax.text(x, y, str(group + 1),
                    ha="center", va="center")
    # Draw distance line
    i, j = (1, 1) if N == 3 else (2, 1)
    x = math.sqrt(3) * (i + j / 2)
    y = 1.5 * j
    ax.plot([0, x], [0, y], "k--", linewidth=2)
    ax.set_title(f"N = {N}, D/R = {math.sqrt(3 * N):.2f}")
    ax.set_aspect("equal")
    ax.set_xlim(-6.8, 6.8)
    ax.set_ylim(-5.8, 5.8)
    ax.axis("off")
fig.suptitle("Frequency Reuse in Hexagonal Cellular Networks")
plt.tight_layout()
plt.savefig("frequency_reuse.png", dpi=180)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
distance = np.linspace(0, 5, 500)
# Generate 5 reflected signals
signal = np.zeros(500, dtype=complex)
for i in range(5):
    amplitude = np.random.rand()
    phase = np.random.rand() * 2 * np.pi
    signal += amplitude * np.exp(1j * (
        phase + 2 * np.pi * distance * np.random.rand()
    ))
# Calculate signal strength in dB
strength = 20 * np.log10(
    np.abs(signal) / np.mean(np.abs(signal))
)
plt.plot(distance, strength)
plt.axhline(-10, color='red', linestyle='--')
plt.xlabel("Distance (m)")
plt.ylabel("Signal Strength (dB)")
plt.title("Multipath Fading")
plt.savefig("exp7.jpeg")
plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
N = 200000
bits = np.random.randint(0, 2, N) #0 and 1
signal = 2 * bits - 1 #0 = -1 , 1 = 1
snr = range(11)
ber1, ber2, ber3 = [], [], []
for x in snr:
    noise = np.random.randn(N) / np.sqrt(2 * 10**(x/10))
    r1 = signal + noise
    r2 = signal + noise + 10**(-6/20) * np.random.choice([-1, 1], N)
    r3 = signal + noise + 10**(-3/20) * np.random.choice([-1, 1], N)
    ber1.append(np.mean((r1 > 0) != bits))
    ber2.append(np.mean((r2 > 0) != bits))
    ber3.append(np.mean((r3 > 0) != bits))
plt.semilogy(snr, np.maximum(ber1, 1e-6), "o-", label="Noise only")
plt.semilogy(snr, np.maximum(ber2, 1e-6), "s-", label="SIR 6 dB")
plt.semilogy(snr, np.maximum(ber3, 1e-6), "^-", label="SIR 3 dB")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Noise and Interference Analysis")
plt.savefig("image.jpeg")
plt.grid()
plt.legend()
plt.show()



# import {useState} from 'react';
# import {View ,Text ,TextInput ,Button} from 'react-native'
# export default function App(){
#   const [A , setA] = useState("");
#   const [B , setB] = useState("");
#   const [R , setR] = useState("0")
#   const cal = (input)=>{
#     const x = parseFloat(A);
#     const y = parseFloat(B);
#     let r = 0;
#     if(input === "+") r =x+y;
#     if(input === "-") r =x+y;
#     if(input === "*") r =x+y;
#     if(input === "/") r =x+y;
#     if(input === "%") r =x+y;
#     setR(String(r));
#   };
#   const clear = ()=>{
#     setR("0");
#     setA("");
#     setB("");
#   };
#   return (
#     <View style={{padding:30 , alignItems:'center' }}>
#       <Text style={{fontSize:30 , fontWeight:900 , color:"blue"}}>Calculator</Text>
#       <TextInput
#       style={{borderWidth:2 ,padding:10, margin:10, textAlign:'center'}}
#       placeholder="number1"
#       keyboardType="numeric"
#       value={A}
#       onChangeText={setA}
#       />
#       <TextInput
#       style={{borderWidth:2 ,padding:10, margin:10, textAlign:'center'}}
#       placeholder="number2"
#       keyboardType="numeric"
#       value={B}
#       onChangeText={setB}
#       />
#       <View style={{ flexDirection: 'row', gap:10, marginTop: 20 }}>
#       <Button title="+" onPress={()=>cal("+")}/>
#       <Button title="-" onPress={()=>cal("-")}/>
#       <Button title="*" onPress={()=>cal("*")}/>
#       <Button title="/" onPress={()=>cal("/")}/>
#       <Button title="%" onPress={()=>cal("%")}/>
#       <Button title="clear" onPress={()=>clear()}/>
#      </View>
#     <Text style={{ fontSize: 30, marginTop: 30  }}>{R}</Text>
#     </View>
#   );
# }

