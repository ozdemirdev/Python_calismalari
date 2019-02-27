  
# import everything from Tkinter module / Tkinter modülündeki kodları projeye dahil ediyoruz  
from Tkinter import*
  
# globally declare the expression variable / expression'u global değişken olarak tanımlıyoruz.  
expression = "" 
  
  
# Function to update expression /Butonlarla girdiğimiz değerleri metin kutusuna ekler.
def press(num): 
    global expression  
    expression = expression + str(num)  
    equation.set(expression) 
  
  
# Function to evaluate the final expression/ İşlem sonucunun kontrol metodu
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. /
    # Try ve Except statementleri hataları kontrol etmek için kullanılır, bir sayının sıfıra bölünmesi vs.
  
    try: 
  
        global expression 
        total = str(eval(expression)) 
  
        equation.set(total) 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block /
    #Eğer hata alınırsa except bloğu reaksiyon gösterir ve "error" yazısı gösterir
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
# Clear ile text box'u temizletme işlemini burası yapacak.
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code /Görsel arayüzümüzü inşa ettiğimiz alan.
if __name__ == "__main__": 
    # create a GUI window / Bir GUI (Graphic User Interface yani görsel kullanıcı arayüzü) penceresi oluştur.
    gui = Tk() 
  
    # set the background colour of GUI window (GUI penceresinin arkaplan rengini ayarlıyoruz)
    gui.configure(background="black") 
  
    # set the title of GUI window (GUI penceresinin başlığını ayarlıyoruz)
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window (GUI'nin pixel bazında boyutunu ayarlıyoruz)
    gui.geometry("265x125") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    #StringVar() bir değişken class'ıdır , bu class'dan bir örnek oluşturduk
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    #expression'ı göstermek için bir metin kutusu oluşturduk
    expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    #widget'ları (butonlar vs.) Düzenli biçimde göstermek için "Grid" yapısı kullanıyoruz
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window .
    # when user press the button, the command or 
    # function affiliated to that button is executed ./
    # Butonları oluşturup onları belli bir düzende yerlerine koyuyoruz(height,width değişkenleri pozisyon bilgisi için).
    #Kullanıcı bir butona bastığında buton içindeki fonksiyon çalışacak ve tepki verecektir.  
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    # start the GUI/
    #Görsel arayüzü başlat
    gui.mainloop()