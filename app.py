# app.py
import os

def install_and_run():
    # pip ব্যবহার করে একটি প্যাকেজ ইনস্টল করুন
    os.system("pip install requests")

    # ইনস্টলেশন পরীক্ষা করুন
    try:
        import requests
        print("Requests লাইব্রেরি সফলভাবে ইনস্টল হয়েছে!")
        response = requests.get("https://api.github.com")
        print(f"GitHub API Status: {response.status_code}")
    except ImportError:
        print("Requests লাইব্রেরি ইনস্টল করতে ব্যর্থ হয়েছে।")

if __name__ == "__main__":
    install_and_run()
