import requests
import time
import random
import math
import threading
from flask import Flask

# ================= CONFIGURATION =================
API_KEY = "5eca871fd120f7c876738fedc98936c0e74a9688"
# Cleaned Reel Link for Stealth Delivery
REEL_LINK = "https://www.instagram.com/reel/DUOjpjNgETA/?igsh=N24zYml1NnN0c3lx" 

TG_TOKEN = "8122746592:AAGB8xJOcCZSrpB8vg8egInqoWGYJ6jptfI"
TG_CHAT_ID = "5148094149"

# SMM SERVICE IDs (2026 Verified High Retention)
UK_VIEW = 12183           
UAE_VIEW = 12181          
AUTHORITY_12034 = 12034   # Impressions + Visits
OLD_LIKES = 9920          # Aged Accounts

app = Flask(__name__)
engine_started = False

# ================= STEALTH HELPERS =================

def get_headers():
    u_agents = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; Samsung Galaxy S24 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 316.0.0.35.109"
    ]
    return {'User-Agent': random.choice(u_agents)}

def notify(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", 
                       data={"chat_id": TG_CHAT_ID, "text": f"📊 {msg}"}, timeout=10)
    except:
        pass

def place_order(s_id, qty, label):
    url = "https://smmonly.com/api/v2"
    payload = {'key': API_KEY, 'action': 'add', 'service': s_id, 'link': REEL_LINK, 'quantity': qty}
    try:
        r = requests.post(url, data=payload, headers=get_headers(), timeout=30).json()
        return "order" in r
    except:
        return False

# ================= THE UNIFIED BLITZ ENGINE =================

def run_sync_blitz():
    # Wait for Koyeb to fully stabilize
    time.sleep(20)
    notify(f"🚀 ENGINE STARTED\nReel: DUOjpjNgETA\nTarget: 1,150 Synchronized Units")

    current_v = 0
    target_v = 1150

    while current_v < target_v:
        
        # --- PHASE 2: THE 850-900 SLOW DRIP & 6-HOUR FREEZE ---
        if 850 <= current_v < 900:
            notify("🛑 ANALYST ZONE (850): Executing Stealth Drip...")
            # Unified Packet
            place_order(AUTHORITY_12034, 90, "DRIP-IMP")
            place_order(OLD_LIKES, 10, "DRIP-LIKE")
            place_order(UK_VIEW, 50, "DRIP-VIEW")
            
            current_v += 50
            notify("💤 6-HOUR GAP INITIATED: Mimicking natural trend decay.")
            time.sleep(21600) # 6 HOURS
            
            notify("🔥 RE-ENGAGING: Starting Final Velocity Push.")
            current_v = 901
            continue

        # --- PHASE 3: FAST-DRIP BLITZ (901-1150) ---
        if current_v >= 901:
            batch = random.randint(90, 130)
            # Higher Intensity for the finish line
            place_order(AUTHORITY_12034, int(batch * 1.6), "FAST-IMP")
            place_order(OLD_LIKES, random.randint(15, 30), "FAST-LIKE")
            if place_order(UK_VIEW, batch, "FAST-VIEW"):
                current_v += batch
            
            notify(f"⚡ BLITZ: {current_v}/1150 | Velocity: MAX")
            time.sleep(random.randint(60, 120)) # 1-2 min rapid fire
            continue

        # --- PHASE 1: S-CURVE (0-850) ---
        prog = current_v / 850
        velocity = math.sin(prog * math.pi) + 0.35
        batch = int(random.randint(60, 90) * velocity)
        
        # Combined Packet (Views + Reach + Engagement)
        place_order(AUTHORITY_12034, int(batch * 1.4), "SYNC-IMP")
        place_order(OLD_LIKES, random.randint(7, 14), "SYNC-LIKE")
        if place_order(random.choice([UK_VIEW, UAE_VIEW]), batch, "SYNC-VIEW"):
            current_v += batch
            
        wait_time = int(1100 / (velocity * 2.4))
        notify(f"🌊 WAVE: {current_v}/850 | Next in {wait_time}s")
        time.sleep(wait_time)

    notify("✅ MISSION COMPLETE: 1,150 Reach/Views synced. Ready for Whop payout.")

# ================= FLASK ROUTES & TRIGGER =================

@app.route('/')
def health():
    global engine_started
    if not engine_started:
        threading.Thread(target=run_sync_blitz, daemon=True).start()
        engine_started = True
        return "Stealth Engine Triggered Successfully", 200
    return "Stealth Engine is Active - Tracking Wave Progression...", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
