import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def carregar_imagens():
    img = {
        "Img001": ImageTk.PhotoImage(Image.open(".venv/img/001_.jpg")),
        "Img002": ImageTk.PhotoImage(Image.open(".venv/img/002_.jpg")),
        "Img003": ImageTk.PhotoImage(Image.open(".venv/img/003_.jpg")),
        "Img004": ImageTk.PhotoImage(Image.open(".venv/img/004_.jpg")),
        "Img005": ImageTk.PhotoImage(Image.open(".venv/img/005_.jpg"))
    }
    return img

def jogar(saldo, aposta, imagens, labels):
    simbolos = ["Img001", "Img002", "Img003", "Img004", "Img005"]
    pesos = [0.2, 0.2, 0.2, 0.2, 0.2]  # Ajuste os pesos conforme necessário
    rolos = random.choices(simbolos, pesos, k=3)
    
    for i in range(3):
        labels[i].config(image=imagens[rolos[i]])
    
    if rolos[0] == rolos[1] == rolos[2]:
        if rolos[0] == "Img001":
            ganho = aposta * 3
            messagebox.showinfo("Resultado", f"Parabéns! Você ganhou R${ganho} com três imagens iguais de 001_.jpg!")
        elif rolos[0] == "Img002":
            ganho = aposta * 4
            messagebox.showinfo("Resultado", f"Parabéns! Você ganhou R${ganho} com três imagens iguais de 002_.jpg!")
        else:
            ganho = aposta * 2
            messagebox.showinfo("Resultado", f"Parabéns! Você ganhou R${ganho} com três imagens iguais!")
        saldo += ganho
    elif len(set(rolos)) == 3:
        saldo += aposta
        messagebox.showinfo("Resultado", f"Você recuperou sua aposta de R${aposta} com três imagens diferentes!")
    else:
        messagebox.showinfo("Resultado", "Tente novamente!")
    
    return saldo

def main():
    saldo = 1000
    
    root = tk.Tk()
    root.title("!!! Jogo MISA!!!")
    root.geometry("500x500")
    
    # Adicionando fundo
    bg_image = ImageTk.PhotoImage(Image.open(".venv/img/fundo.jpg"))
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagens = carregar_imagens()
    labels_frame = tk.Frame(root, bg="white")
    labels_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    
    labels = [tk.Label(labels_frame, bg="white") for _ in range(3)]
    for label in labels:
        label.pack(side=tk.LEFT, padx=10)
    
    saldo_label = tk.Label(root, text=f"Saldo atual: R${saldo}", bg="white", font=("Helvetica", 14))
    saldo_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    aposta_frame = tk.Frame(root, bg="white")
    aposta_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    aposta_label = tk.Label(aposta_frame, text="Aposta:", bg="white", font=("Helvetica", 12))
    aposta_label.pack(side=tk.LEFT)
    
    aposta_entry = tk.Spinbox(aposta_frame, from_=1, to=saldo, increment=1, font=("Helvetica", 12))
    aposta_entry.pack(side=tk.LEFT)
    
    def jogar_callback():
        nonlocal saldo
        try:
            aposta = int(aposta_entry.get())
            if aposta > saldo:
                messagebox.showerror("Erro", "Aposta maior que o saldo disponível. Tente novamente.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número.")
            return
        
        saldo -= aposta
        saldo = jogar(saldo, aposta, imagens, labels)
        saldo_label.config(text=f"Saldo atual: R${saldo}")
        
        if saldo <= 0:
            messagebox.showinfo("Fim de Jogo", "Saldo insuficiente para continuar jogando.")
            if messagebox.askyesno("Reiniciar", "Deseja reiniciar o jogo?"):
                saldo = 1000
                saldo_label.config(text=f"Saldo atual: R${saldo}")
            else:
                root.quit()
    
    jogar_button = tk.Button(root, text="Jogar", command=jogar_callback, font=("Helvetica", 12))
    jogar_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    
    root.mainloop()

if __name__ == "__main__":
    main()
