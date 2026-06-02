import schedule
import time
import subprocess

def collect():
    print("⏰ Running data collection...")
    subprocess.run(["python", "src/collect_data.py"])
    print("✅ Done! Waiting for next hour...\n")

# Run every hour
schedule.every(1).hours.do(collect)

# Also run immediately when script starts
collect()

print("🤖 Scheduler running! Data will be collected every hour.")
print("Press Ctrl+C to stop.\n")

while True:
    schedule.run_pending()
    time.sleep(60)