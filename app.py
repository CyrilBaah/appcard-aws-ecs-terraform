from flask import Flask, Response

app = Flask(__name__)

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
      --bg: #EFF6FF;
      --card: #ffffff;
      --border: #BFDBFE;
      --accent: #2563EB;
      --accent-light: #DBEAFE;
      --text: #1E3A5F;
      --muted: #64748B;
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
    }

    .app-initial {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: rgba(255,255,255,0.2);
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
      color: rgba(255,255,255,0.65);
    }

    .version-badge {
      position: absolute;
      top: 28px;
      right: 28px;
      background: rgba(255,255,255,0.2);
      border: 1px solid rgba(255,255,255,0.3);
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
      border-bottom: 1px solid #F1F5F9;
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

    .card-footer {
      background: var(--accent-light);
      border-top: 1px solid var(--border);
      padding: 12px 28px;
      font-size: 11px;
      color: var(--accent);
      font-family: var(--mono);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .footer-dot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--accent);
      opacity: 0.5;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="card-header">
      <div class="app-initial">SA</div>
      <div class="app-name">StatusApp</div>
      <div class="app-tagline">Container identity card</div>
      <div class="version-badge">v1.0.0</div>
    </div>

    <div class="card-body">
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
        <span class="field-value">1.0.0</span>
      </div>
      <div class="field">
        <span class="field-label">Environment</span>
        <span class="field-value">production</span>
      </div>
      <div class="field">
        <span class="field-label">App name</span>
        <span class="field-value">statusapp</span>
      </div>
    </div>

    <div class="card-footer">
      <div class="footer-dot"></div>
      Deployed on AWS ECS Fargate
    </div>
  </div>
</body>
</html>"""


@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")


@app.route("/health")
def health():
    from flask import jsonify
    return jsonify({"status": "healthy", "version": "1.0.0"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)