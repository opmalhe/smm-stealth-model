import requests
import time
import random
import math
import threading
from flask import Flask

# ================= CONFIGURATION =================
API_KEY = "5eca871fd120f7c876738fedc98936c0e74a9688"
REEL_LINK = "https://www.instagram.com/reel/DUOjpjNgETA/?igsh=N24zYml1NnN0c3lx" 

TG_TOKEN = "8122746592:AAGB8xJOcCZSrpB8vg8egInqoWGYJ6jptfI"
TG_CHAT_ID = "5148094149"

# SMM SERVICE IDs (2026 Verified)
UK_VIEW = 12183           
UAE_VIEW = 12181          
AUTHORITY_12034 = 12034   
OLD_LIKES = 9920          

app = Flask(__name__)

@app.route('/')
def health(): 
    return {"status": "Global Blitz Active", "safe_mode": True}, 200

# ================= HELPER TOOLS =================

def get_headers():
    u_agents = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 290.0.0.33.191"
    ]
    return {'User-Agent': random.choice(u_agents)}

def notify(msg):
    try: requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", 
                       data={"chat_id": TG_CHAT_ID, "text": f"📊 ANALYTICS: {msg}"}, timeout=10)
    except: pass

def place_order(s_id, qty, label):
    url = "https://smmonly.com/api/v2"
    payload = {'key': API_KEY, 'action': 'add', 'service': s_id, 'link': REEL_LINK, 'quantity': qty}
    try:
        r = requests.post(url, data=payload, headers=get_headers(), timeout=30).json()
        return "order" in r
    except: return False

# ================= THE MASTER ALGO =================

def run_sync_blitz():
    # Warm-up delay for server stability
    time.sleep(20)
    notify("SYSTEM ONLINE. Phase 1 (0-850) Starting.")

    current_v = 0
    target_v = 1150

    while current_v < target_v:
        
        # PHASE 2: THE 850-900 SLOW DRIP & 6-HOUR FREEZE
        if 850 <= current_v < 900:
            notify("📍 850 Reached. Firing Slow Drip Packet.")
            # Unified Drip Packet
            place_order(AUTHORITY_12034, 80, "DRIP-IMP")
            place_order(OLD_LIKES, 10, "DRIP-LIKE")
            place_order(UK_VIEW, 50, "DRIP-VIEW")
            
            current_v += 50
            notify("💤 ANALYST BYPASS: Sleeping for 6 Hours. Data will normalize.")
            time.sleep(21600) 
            
            notify("🔥 WAKE UP: Starting Final Fast-Drip Blitz.")
            current_v = 901
            continue

        # PHASE 3: FAST-DRIP BLITZ (901-1150)
        if current_v >= 901:
            batch = random.randint(85, 115)
            # Sync Fast Packets (High Impression Ratio 1.5x)
            place_order(AUTHORITY_12034, int(batch * 1.5), "FAST-IMP")
            place_order(OLD_LIKES, random.randint(15, 25), "FAST-LIKE")
            if place_order(UK_VIEW, batch, "FAST-VIEW"):
                current_v += batch
            
            notify(f"⚡ FAST-DRIP: {current_v}/1150. Speed: Aggressive.")
            time.sleep(random.randint(90, 180)) # 1.5 - 3 min gap
            continue

        # PHASE 1: S-CURVE (0-850)
        prog = current_v / 850
        velocity = math.sin(prog * math.pi) + 0.35
        batch = int(random.randint(55, 85) * velocity)
        
        # Unified Packet (Fire everything at once)
        place_order(AUTHORITY_12034, int(batch * 1.3), "SYNC-IMP")
        place_order(OLD_LIKES, random.randint(8, 15), "SYNC-LIKE")
        if place_order(random.choice([UK_VIEW, UAE_VIEW]), batch, "SYNC-VIEW"):
            current_v += batch
            
        wait_time = int(1300 / (velocity * 2.3))
        notify(f"🌊 Growth Wave: {current_v}/850 | Next in {wait_time}s")
        time.sleep(wait_time)

    notify("✅ MISSION COMPLETE. 1,150 Views. Reach > Views. Perfect Analytic Curve.")

if __name__ == "__main__":
    threading.Thread(target=run_sync_blitz, daemon=True).start()
    # Important: Run on 0.0.0.0 for Koyeb/Heroku compatibility
    app.run(host='0.0.0.0', port=8000)
