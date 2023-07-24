from tkinter import *
root=Tk()
root.geometry("1000x800")
root.resizable(0,0)
root.title("Admin Panel")
label_roots=Label(root,text="Tour and Tarvel Booking System",font=("arial",29,"bold"),fg="orange")
label_roots.place(x=232,y=5)

def logout():
    root.destroy()
    import log_in
button_logout=Button(root,text="Logout",font=("Arial",22,"bold"),fg="blue",command=logout,relief=GROOVE,bd=0)
button_logout.place(x=880,y=0)

def frame_user():
    

    frame_user=Frame(root,width=800,height=800,g="green")
    frame_user.place(x=200,y=50)
    user_label=Label(frame_user,text="Hello",font=("Arial",24,"bold"))
    user_label.place(x=280,y=400)
def frame_feedback():
    frame_feedback=Frame(root,width=800,height=800,g="green")
    frame_feedback.place(x=200,y=50)
    user_label=Label(frame_feedback,text="Hi",font=("Arial",24,"bold"))
    user_label.place(x=280,y=400)
def frame_formdetails():
    frame_formdetails=Frame(root,width=800,height=800,bg="green")
    frame_formdetails.place(x=200,y=50)
    user_label=Label(frame_formdetails,text="magadascar",font=("Arial",24,"bold"))
    user_label.place(x=280,y=400)
def frame_destination_details():
    frame_destination_details=Frame(root,width=800,height=800,g="green")
    frame_destination_details.place(x=200,y=50)
    user_label=Label(frame_destination_details,text="Islands",font=("Arial",24,"bold"))
    user_label.place(x=280,y=400)
options_frame=Frame(root,width=200,height=800,bg="grey")
options_frame.place(x=0,y=0)
label_options=Label(options_frame,text="Dashboard",font=("Arial",27,"bold"),fg="blue",bg="grey")
label_options.place(x=0,y=0)
button_user_details=Button(options_frame,text="User Information",font=("Arial",17,"bold"),fg="blue",bg="grey",bd=0,command=frame_user)
button_user_details.place(x=0,y=80)
button_help_feedback=Button(options_frame,text="Help Requested",font=("Arial",17,"bold"),fg="blue",bg="grey",bd=0,command=frame_feedback)
button_help_feedback.place(x=0,y=170)
button_form_details=Button(options_frame,text="Form Details",font=("Arial",17,"bold"),fg="blue",bg="grey",bd=0,command=frame_formdetails)
button_form_details.place(x=0,y=260)
button_destination_details=Button(options_frame,text="Destination",font=("Arial",17,"bold"),fg="blue",bg="grey",bd=0,command=frame_destination_details)
button_destination_details.place(x=0,y=345)
root.mainloop()