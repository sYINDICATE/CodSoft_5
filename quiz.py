import tkinter as tk
from tkinter import *
correct = 0
wrong = 0
index = 0

root = tk.Tk()
root.geometry("1250x400")
root.title("Quiz game")
root.configure(background="#C0C0FF")


QUESTIONS =["1) How many time zones are there in India? ",
            "2) Solve 3 + 6 ( 5 + 4) ÷ 3 - 7 ",
            "3) Which 3 numbers have the same answer whether they’re added or multiplied together?",
            "4) Solve  - 15+ (-5x) =0",
            "5) How many sides does a decagon have?",
            "6) Which of the following is used in pencils?",
            "7) Which of the following metals forms an amalgam with other metals?",
            "8) Following super cars Gallardo and Murcielago belongs to which company?",
            "9) The inert gas which is substituted for nitrogen in the air used by deep sea divers for breathing, is: ",
            "10) The members of the Rajya Sabha are elected for a term of ?",
            "11) Non stick cooking utensils are coated with",
            "12) What is three fifth of hundred?",
            "13) Can you simplify -3i(4 + 2i)?",
            "14) In how many countries was USSR divided?",
            "15) Most intelligent mammals are:",
            "16) Myopia is connected with",
            "17) Our skin, when exposed to excess sunlight, becomes dark. This is because our skin pigments called",
            "18) The World's highest annual rainfall is reported at",
            "19) Magnetism at the centre of a bar magnet is",
            "20) On a rainy day, small oil films on water show brilliant colours. This is due to",
            "21) Stars twinkle because",
            "22) Sound travels at the fastest speed in: ",
            "23) Example of palindrome among th following is:",
            "24) Which consists of two plates separated by a dielectric and can store a charge?",
            "25) Which of the following is Marsh gas",
            "26) One kilobyte has _____?",
            "27) Which of these is a correct UPI virtual address?",
            "28) In which of the following only decade, India’s Population had shown negative growth?",
            "29) Which of the following type of Coal has maximum carbon content?",
            "30) Which of the following non-metals is most electronegative?",
            "31) Chemical composition of heavy water is: ",
            "32) Antacids are found in drugs that give relief to: ",
            "33) Citric acid is present in free form in: ",
            "34) What does Insulin do?",
            "35) Defence Acquisition Council (DAC) approved the procurement of 83 Tejas fighter aircrafts, manufactured by which organisation?",
            "36) Which supersonic cruise missile with Indigenous Booster has been successfully flight tested?",]

CHOICE = [["[A] One","[B] Zero","[C] Two","D] Three"],
        ["[A] 11","[B] 16","[C] 14","[D] 15"],
        ["[A] 4,5,6","[B] 7,8,9","[C] 1,2,3","[D] 10,11,12"],
        ["[A] 3","[B] -3","[C] 10","[D] -10"],
        ["[A] 8","[B] 9","[C] 10","[D] 11"],
        ["[A]Graphite","[B]Silicon","[C]Charcoal","[D]Phosphorous"],
        ["[A]Tin","[B]Mercury","[C]Lead","[D]Zinc"],
        ["[A]Audi","[B]Rolls Royce","[C]Lamborghini","[D]Porsche"],
        ["[A]Helium","[B]Xenon","[C]Oxygen","[D]Krypton"],
        ["[A]six years","[B] determined by the state legislative assembly of a state","[C]	four years","[D]	None of the above"],
        ["[A]Teflon","[B]PVC","[C]black paint","[D]polystyrene"],
        ["[A]40","[B]60","[C]80","[D]20"],
        ["[A] -12i +6i","[B] -12i - 6i","[C] 5","[D] 6 - 12i"],
        ["[A]12","[B]15","[C]25","[D]35"],
        ["[A]Elephants","[B]Whale","[C]Wolf","[D]Dolphin"],
        ["[A]Eyes","[B]Skin","[C]Ear","[D]Nose"],
        ["[A]Keratin","[B]Melanin","[C]Calcium","[D]None of these"],
        ["[A]Cherapunji","[B]Mt.Everest","[C]Mawsynram","[D]None of these"],
        ["[A]Null","[B]Minimum","[C]Maximum","[D]Some"],
        ["[A]Refraction","[B]Interference","[C]Reflection","[D]Transmission"],
        ["[A]the intensity of light emitted by them changes with time","[B]the distance of the stars from the earth changes with time","[C]the refractive index of the different layers of the earth's atmosphere changes continuously, consequently the position of the image of a start changes with time","[D]the light from the star is scattered by the dust particles and air molecules in the earth's atmosphere"],
        ["[A]Steel","[B]Water","[C]Air","[D]Vacuum"],
        ["[A]Radar","[B]Sensor","[C]Radio","[D]Book"],
        ["[A]Resistor","[B]Capacitor","[C]Insulator","[D]None of these"],
        ["[A]Methane","[B]Chlorine","[C]Helium","[D]None of these"],
        ["[A]1000 bytes","[B] 128 bytes","[C] 1024 bytes","[D] 1036 bytes"],
        ["[A] abc-sbi""[B] abc","[C] abc@sbi.com","[D] abc@sbi"],
        ["[A] 1901-11","[B] 1911-1921","[C] 1921-1931","[D] 1931-1941"],
        ["[A] Peat","[B] Lignite","[C] Antharacite","[D] Bituminious"],
        ["[A] Neon","[B] Fluorine","[C] Chlorine","[D] Oxygen"],
        ["[A] H2O2","[B] H2O","[C] HDO","[D] D2O"],
        ["[A] Eye sight","[B] Headache","[C] Acne","[D] Stomachache"],
        ["[A] Tamarind","[B] Milk","[C] Apple","[D] Lemon"],
        ["[A] Increases blood sugar","[B] Decreases blood sugar","[C] Constricts blood vessels","[D] Stimulates lactation"],
        ["[A] Hindustan Aeronautics Limited","[B] Bharat Electronics Limited","[C] Bharat Heavy Electricals Limited","[D] Or,dnance Factory Board"],
        ["[A] BrahMos","[B] Nirbhay","[C] Shaurya","[D] Viraat"]]

#List of correct answers
ANSWERS = [CHOICE[0][0],CHOICE[1][2],CHOICE[2][1],CHOICE[3][2],CHOICE[4][1],CHOICE[5][0],CHOICE[6][2],CHOICE[7][1],CHOICE[8][3],CHOICE[9][2],CHOICE[10][0],CHOICE[11][0],CHOICE[12][1],CHOICE[13][3],CHOICE[14][1],CHOICE[15][1],CHOICE[16][0],CHOICE[17][2],CHOICE[18][0],CHOICE[19][1],CHOICE[20][3],CHOICE[21][0],CHOICE[22][0],CHOICE[23][1],CHOICE[24][0],CHOICE[25][2],CHOICE[26][1],CHOICE[27][1],CHOICE[28][2],CHOICE[29][1],CHOICE[30][2],CHOICE[31][3],CHOICE[32][3],CHOICE[33][1],CHOICE[34][0],CHOICE[35][0]]

opts = CHOICE[index]

frame =tk.Frame(root,padx=10,pady=10)
question_label =tk.Label(frame,text=QUESTIONS[index],font=("Verdana",15),bg="#C0C0FF")

v1 = StringVar(frame,opts[0])
v2 = StringVar(frame,opts[1])
v3 = StringVar(frame,opts[2])
v4 = StringVar(frame,opts[3])

#Create a label to display whether the selected answer is correct.
res_display = StringVar(frame)#StringVar will act as variable text to result display label.
res_label = Label(frame,textvariable = res_display)#Display label
res_label.pack()
res_label.grid(row=5,column=3)

#Create a label to display conclusion
conclusion = StringVar(frame)
conclusion_label = Label(frame,textvariable=conclusion)

#Create a function to check the selected answer
def checkAnswer(radio):
    global wrong,correct, index

    if radio['text'] == ANSWERS[index]:
        res_display.set("Yeah, you got the correct answer!")
        correct+=1
    else:
        res_display.set("Sorry, you got the wrong answer!")
        wrong+=1
        
    
    index +=1
    disableButtons(tk.DISABLED)

option2 = tk.Radiobutton(frame,text=CHOICE[index][1],bg="#F0F0FF",variable=v2,command= lambda : checkAnswer(option2),font=("Comicsansms",10))
option1 = tk.Radiobutton(frame,text=CHOICE[index][0],bg="#F0F0FF",variable=v1,command= lambda : checkAnswer(option1),font=("Comicsansms",10))
option3 = tk.Radiobutton(frame,text=CHOICE[index][2],bg="#F0F0FF",variable=v3,command= lambda : checkAnswer(option3),font=("Comicsansms",10))
option4 = tk.Radiobutton(frame,text=CHOICE[index][3],bg="#F0F0FF",variable=v4,command= lambda : checkAnswer(option4),font=("Comicsansms",10))

#Create a functon to disable radiobutton
def disableButtons(state):
    option1['state']= state
    option2['state']= state
    option3['state']= state
    option4['state']= state

disableButtons(tk.NORMAL)

frame.pack(fill="both",expand="true")
question_label.grid(row=0,column=1)

option1.grid(row=1,column=1)
option2.grid(row=2,column=1)
option3.grid(row=3,column=1)
option4.grid(row=4,column=1)

#Create a function to create next question
def displayNextQuestion():
    global opts
    question_label['text'] = QUESTIONS[index]

    disableButtons(tk.NORMAL)
    opts=CHOICE[index]
    option1['text'] = opts[0]    
    option2['text'] = opts[1]
    option3['text'] = opts[2]
    option4['text'] = opts[3]
    v1.set(opts[0])
    v2.set(opts[1])
    v3.set(opts[2])
    v4.set(opts[3])
    res_display.set("")
    if index >= len(QUESTIONS):
        conclusion.set("Congratulations, you have completed the quiz!")
        conclusion_label.pack()
        question_label.grid_forget
        disableButtons(tk.DISABLED)


button_next = tk.Button(frame,text="Next",font=("Comicsansms"),command= lambda : displayNextQuestion())
button_next.grid(row=2,column=5)
print(index)
root.mainloop()