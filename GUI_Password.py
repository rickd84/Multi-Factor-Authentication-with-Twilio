from twilio.rest import Client
import tkinter
import random

root = tkinter.Tk()
root.title("Two factor authentication")

account_sid = 'AC7a5eb26af08bf3acc94dfb5fabb6a36d'
auth_token = 'bdf3d455fc6cfdb637ef9399f0f7cfc3'
client = Client(account_sid, auth_token)

randomDigits = random.randint(100000,999999)
r1 = randomDigits
x="Demo for Proffesor Essa\n Your code is: ", randomDigits
message = client.messages.create(
                     body="Demo for Proffesor Essa\n Your code is: " + str(r1),
                     from_='+12162509015',
                     to='+14406231816'
                 )

   
def forgotPass():
   global question1
   global question2
   #root.destroy()
   questions = tkinter.Tk()
   questions.title("Security Questions")
   tkinter.Label(questions, text = "Please Answer the Following Questions").place(x=80, y=15)
   tkinter.Label(questions, text = question[random1]+":").place(x=50, y=50)
   question1 = tkinter.Entry(questions, textvariable = q1)
   question1.place(x = 50, y = 80)
   tkinter.Label(questions, text = question[random2]+":").place(x=50, y=100) 
   question2 = tkinter.Entry(questions, textvariable = q2)
   question2.place(x = 50, y = 120) 
   tkinter.Button(questions, text="Submit", command = get_data).place(x=160, y=120)
   questions.geometry("450x200")
   questions.mainloop()

def get_data():
   global user_ans1
   global user_ans2
   user_ans1 = question1.get()
   q1.set(user_ans1)
   user_ans2 = question2.get()
   q2.set(user_ans2)
   print(q1.get())
   print(q2.get())
   print(user_ans1)
   print(user_ans2)
   if user_ans1 == answers[random1]:
      if user_ans2 == answers[random2]:
         print("Continue")
         Number()
      else:
         print("Try Again")
   else:
      print("Incorrect")     
   
def Number():
   
   number = tkinter.Tk()
   number.title("Phone Number Identification")
   tkinter.Label(number, text = "Please input your phone-number").place(x=80, y=15)
   tkinter.Label(number, text = "Phone Number:").place(x=80, y=50)
   tkinter.Entry(number).place(x=120, y=50)
   tkinter.Button(number, text= "Send code", command = sendCodeButton).place(x=160, y=120)
   number.geometry("450x200")
   number.mainloop()

def sendSMS():
   global sixDigitCode
   sendSMS = tkinter.Tk()
   sendSMS.title("Authorization")
   tkinter.Label(sendSMS, text = "Please enter your six digit code:").place(x=100, y=15)
   sixDigitCode = tkinter.Entry(sendSMS, textvariable = q3)
   sixDigitCode.place(x = 120, y = 40)
   tkinter.Button(sendSMS, text = "Verify me", command = codeVerify).place(x=160, y= 120)
   sendSMS.geometry("450x200")
   sendSMS.mainloop()

def codeVerify():
   global user_ans3
   user_ans3 = sixDigitCode.get()
   q3.set(user_ans3)
   print(q3.get())
   print(user_ans3)
   print(r1)
   
   if str(user_ans3) == str(r1):
      print("Continue")
      verified()
   else:
      print("Incorrect")

def sendCodeButton():
   sendSMS()
   print(message.sid)

def verified():
   verified = tkinter.Tk()
   verified.title("Reset Password ")
   tkinter.Label(verified, text = "Please reset yout password:").place(x=80, y=15)
   tkinter.Label(verified, text = "Username:").place(x=80, y=50)
   tkinter.Entry(verified).place(x=200, y=50)
   tkinter.Label(verified, text = "New Password:").place(x=80, y=90)
   tkinter.Entry(verified).place(x=200, y=90)
   tkinter.Label(verified, text = "Confirm Password:").place(x=80, y=130)
   tkinter.Entry(verified).place(x=200, y=130)
   tkinter.Button(verified, text = "Submit", command = fin ).place(x= 160, y=160)
   verified.geometry("450x200")
   verified.mainloop()

def fin():
   fin = tkinter.Tk()
   fin.title(" ")
   tkinter.Label(fin, text = "Your password has been reset").place(x=80, y=15)
   tkinter.Button(fin, text = "Login", command = root.lift).place(x=210, y=90)
   fin.geometry("450x200")
   fin.mainloop()

q1 = tkinter.StringVar()
q2 = tkinter.StringVar()
q3 = tkinter.StringVar()
user_ans1 = tkinter.StringVar()
user_ans2 = tkinter.StringVar()
user_ans3 = tkinter.StringVar()

random1 = random.randint(0,4)
random2 = random.randint(0,4)


   
tkinter.Label(root, text = "Welcome to our two factor authentication program").place(x=80, y=15)

tkinter.Label(root, text = "Email:").place(x=80, y=50)

tkinter.Entry(root).place(x=120, y=50)

tkinter.Label(root, text = "Password:").place(x=60, y=90) 

tkinter.Entry(root).place(x=120, y=90)

tkinter.Button(root, text="Login").place(x=120, y=120)
tkinter.Button(root, text="Forgot My Password", command = forgotPass).place(x=160, y=120)
root.geometry("400x200")

question = ['What was the first book I ever read?', 'What was the first company I ever worked for?', 'What High School did my mother attend?', 'In which city was my mother born?', 'In which city was my father born?']
answers = ['Catcher in the Rye', 'Hyland', 'John Marshall', 'Cleveland', 'Toronto']
root.mainloop()
