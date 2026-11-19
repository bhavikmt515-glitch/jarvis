import datetime
import re

def speak(text):
    print(f"Jarvis: {text}")
    # phone pe awaz ke liye, agar pyttsx3 nahi hai to sirf print hoga
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def handle_command(cmd):
    c = cmd.lower().strip()

    if "hello" in c or "hi jarvis" in c or "namaste" in c:
        return "Hello sir, main Jarvis hun. Batao kya karna hai?"

    if "time" in c:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Sir, time hai {now}"

    if "date" in c or "tarikh" in c:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Sir, aaj date hai {today}"

    if "room" in c:
        nums = re.findall(r'(\d+(\.\d+)?)', c)
        nums = [float(n[0]) for n in nums]
        if len(nums) >= 2:
            w = nums[0]
            h = nums[1]
            area = w * h
            wall = "9 inch"
            if "4.5" in c or "4.5 inch" in c:
                wall = "4.5 inch"
            if "9 inch" in c:
                wall = "9 inch"
            return f"Room ban gaya sir - {w} x {h} feet, Area {area} sq ft, Wall {wall}"
        return "Room ka size batao sir, jaise room 12 by 14"

    if "rectangle" in c or "rect" in c:
        nums = re.findall(r'(\d+(\.\d+)?)', c)
        nums = [float(n[0]) for n in nums]
        if len(nums) >= 2:
            return f"Rectangle ban gaya sir - {nums[0]} x {nums[1]}"
        return "Rectangle ka size batao"

    if "circle" in c:
        nums = re.findall(r'(\d+(\.\d+)?)', c)
        nums = [float(n[0]) for n in nums]
        if nums:
            return f"Circle ban gaya sir - radius {nums[0]}"
        return "Circle ka radius batao"

    if "colour" in c or "color" in c or "colour" in c:
        return "Colour set ho gaya sir"

    if "bye" in c or "band" in c or "exit" in c:
        return "BYE"

    return "Samajh nahi aaya sir, try karo - time batao, room 12 by 14 banao, hello"

print("Jarvis Online Hai Sir...")
while True:
    user = input("You: ")
    if user.lower().strip() in ["exit", "quit", "bye"]:
        print("Jarvis: Bye sir")
        break
    ans = handle_command(user)
    speak(ans)
