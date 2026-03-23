from flask import Flask, Response, jsonify
import datetime
import os

app = Flask(__name__)

START_TIME = datetime.datetime.utcnow()


def uptime():
    delta = datetime.datetime.utcnow() - START_TIME
    h, rem = divmod(int(delta.total_seconds()), 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}h {m}m"
    return f"{m}m {s}s"


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>StatusApp</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #ECFDF5;
      --card: #ffffff;
      --border: #A7F3D0;
      --accent: #059669;
      --accent-light: #D1FAE5;
      --accent-glow: #10B981;
      --text: #064E3B;
      --muted: #047857;
      --mono: 'IBM Plex Mono', monospace;
      --sans: 'IBM Plex Sans', sans-serif;
    }

    body {
      font-family: var(--sans);
      background: var(--bg);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      width: 100%;
      max-width: 420px;
      overflow: hidden;
    }

    .card-header {
      background: var(--accent);
      padding: 28px 28px 24px;
      position: relative;
      background: linear-gradient(135deg, #047857 0%, #059669 100%);
    }

    .app-initial {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: rgba(255,255,255,0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--mono);
      font-weight: 600;
      font-size: 18px;
      color: #fff;
      margin-bottom: 14px;
      letter-spacing: -1px;
    }

    .app-name {
      font-size: 20px;
      font-weight: 500;
      color: #fff;
      margin-bottom: 4px;
    }

    .app-tagline {
      font-size: 13px;
      color: rgba(255,255,255,0.6);
    }

    .version-badge {
      position: absolute;
      top: 28px;
      right: 28px;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      color: #fff;
      font-family: var(--mono);
      font-size: 11px;
      padding: 4px 10px;
      border-radius: 20px;
    }

    .card-body {
      padding: 24px 28px;
    }

    .field {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
    }

    .field:last-child { border-bottom: none; }

    .field-label {
      font-size: 12px;
      font-weight: 500;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: .06em;
    }

    .field-value {
      font-family: var(--mono);
      font-size: 13px;
      color: var(--text);
    }

    .field-value.highlight {
      color: var(--accent-glow);
    }

    .status-dot {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #22C55E;
      animation: blink 2s ease-in-out infinite;
    }

    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }

    /* New in v2: uptime counter ticks live */
    #uptime-val { transition: opacity 0.3s; }

    .divider {
      height: 1px;
      background: var(--border);
      margin: 4px 0;
    }

    .section-label {
      font-size: 10px;
      font-weight: 600;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: .08em;
      padding: 14px 0 6px;
    }

    .card-footer {
      background: var(--accent-light);
      border-top: 1px solid var(--border);
      padding: 12px 28px;
      font-size: 11px;
      color: var(--accent-glow);
      font-family: var(--mono);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .footer-dot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--accent-glow);
      opacity: 0.5;
    }

    .sha-pill {
      background: rgba(5,150,105,0.16);
      border: 1px solid var(--border);
      color: var(--accent-glow);
      font-family: var(--mono);
      font-size: 11px;
      padding: 3px 9px;
      border-radius: 6px;
      letter-spacing: .02em;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="card-header">
      <div class="app-initial">SA</div>
      <div class="app-name">StatusApp</div>
      <div class="app-tagline">Container identity card</div>
      <div class="version-badge">v2.0.0</div>
    </div>

    <div class="card-body">

      <div class="section-label">App info</div>

      <div class="field">
        <span class="field-label">Status</span>
        <span class="field-value">
          <span class="status-dot">
            <span class="dot"></span>
            online
          </span>
        </span>
      </div>
      <div class="field">
        <span class="field-label">Version</span>
        <span class="field-value">2.0.0</span>
      </div>
      <div class="field">
        <span class="field-label">Environment</span>
        <span class="field-value">production</span>
      </div>
      <div class="field">
        <span class="field-label">App name</span>
        <span class="field-value">statusapp</span>
      </div>

      <div class="section-label">Deployment</div>

      <div class="field">
        <span class="field-label">Uptime</span>
        <span class="field-value highlight" id="uptime-val">__UPTIME__</span>
      </div>
      <div class="field">
        <span class="field-label">Region</span>
        <span class="field-value highlight">__REGION__</span>
      </div>
      <div class="field">
        <span class="field-label">Build</span>
        <span class="field-value"><span class="sha-pill">__BUILD__</span></span>
      </div>
      <div class="field">
        <span class="field-label">Image tag</span>
        <span class="field-value highlight">__IMAGE_TAG__</span>
      </div>

    </div>

    <div class="card-footer">
      <div class="footer-dot"></div>
      Deployed on AWS ECS Fargate
    </div>
  </div>

  <script>
    function tick() {
      fetch('/api/info')
        .then(r => r.json())
        .then(d => {
          document.getElementById('uptime-val').textContent = d.uptime;
        })
        .catch(() => {});
    }
    setInterval(tick, 5000);
  </script>
</body>
</html>"""


@app.route("/")
def index():
    region = os.environ.get("AWS_REGION", "us-east-1")
    build = os.environ.get("BUILD_SHA", "abc1234")
    image_tag = os.environ.get("IMAGE_TAG", "latest")

    html = (HTML
            .replace("__UPTIME__", uptime())
            .replace("__REGION__", region)
            .replace("__BUILD__", build)
            .replace("__IMAGE_TAG__", image_tag))
    return Response(html, mimetype="text/html")


@app.route("/api/info")
def info():
    return jsonify({
        "version": "2.0.0",
        "status": "healthy",
        "uptime": uptime(),
        "region": os.environ.get("AWS_REGION", "us-east-1"),
        "build": os.environ.get("BUILD_SHA", "abc1234"),
        "image_tag": os.environ.get("IMAGE_TAG", "latest"),
        "environment": "production",
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": "2.0.0"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)