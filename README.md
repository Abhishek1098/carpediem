# carpediem
A python application that generates a visual representation of how many days have passed since your last birthday using Python Turtle, EasyGui, DateTime, OS modules.

Setup:
Install easygui using ```pip install easygui```

During the inital run the program prompts the user for their birthday. 
![user_input](https://user-images.githubusercontent.com/37665968/130194255-e0ec9b23-4d53-4e0a-a39f-c62528df9688.PNG)

Example run of application:
![example](https://user-images.githubusercontent.com/37665968/130195072-adc60d56-ea9c-47c9-8468-9c3e9622ce0f.PNG)
![output](https://user-images.githubusercontent.com/37665968/130195080-651649f6-9d15-4118-b110-71383756d8ff.PNG)

After inital run, the users birthday is saved to the text file 'carpediem_helper.txt'.

I created a simple batch file to run my python script. 
```
@echo off
"C:\Users\17328\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\17328\Desktop\carpediem\carpediem.py"
pause 
```

Lastly, I setup Window Task Scheduler to run my batch file once a day if the computer is logged into. 
![task_scheduler_1](https://user-images.githubusercontent.com/37665968/130196664-28153945-4763-4008-8b62-037c4e2d8fc9.PNG)
![task_scheduler_2](https://user-images.githubusercontent.com/37665968/130196659-aafb2470-beb0-4a7f-8be1-bdd9b45773ce.PNG)
![task_scheduler_3](https://user-images.githubusercontent.com/37665968/130196662-4f4323f5-4c6f-41c9-9b3a-eed6193056a3.PNG)



