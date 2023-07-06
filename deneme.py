import schedule

def run_job():
    # Görevin yapılması gereken işlemler
    print("Görev çalıştı!")

schedule.every().hour.do(run_job)