CSS = """
<style>

html, body, [class*="css"], .stApp {
    font-family: 'Segoe UI', sans-serif !important;
    background-color: #0e1117 !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] {
    background: #0e1117 !important;
    border-right: 1px solid #2d2d2d !important;
}
section[data-testid="stSidebar"] h2 {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #ffd43b !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 14px !important;
    color: #ffffff !important;
    padding: 4px 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stCaption"] {
    color: #adb5bd !important;
}

h1, h2, h3 {
    color: #ffffff !important;
}

[data-testid="stCaption"] {
    color: #adb5bd !important;
}

.stButton > button {
    font-size: 13px !important;
    border-radius: 6px !important;
    border: 1px solid #3d3d3d !important;
    background: #1a1d26 !important;
    color: #ffffff !important;
}
.stButton > button:hover {
    border-color: #ffd43b !important;
    color: #ffd43b !important;
}
.stButton > button[kind="primary"] {
    background: #ffd43b !important;
    border-color: #ffd43b !important;
    color: #0e1117 !important;
    font-weight: 600 !important;
}
.stButton > button[kind="primary"]:hover {
    background: #fcc419 !important;
    border-color: #fcc419 !important;
}

.upload-hint {
    border: 2px dashed #3d3d3d;
    border-radius: 8px;
    padding: 40px 24px;
    text-align: center;
    color: #adb5bd;
    font-size: 14px;
    background: #1a1d26;
}

.empty-state {
    text-align: center;
    padding: 40px 24px;
    color: #adb5bd;
    font-size: 14px;
    border: 1px solid #2d2d2d;
    border-radius: 8px;
    background: #1a1d26;
}

.receipt-card {
    background: #1a1d26;
    border: 1px solid #2d2d2d;
    border-radius: 8px;
    padding: 20px;
    font-family: 'Courier New', monospace;
    font-size: 13px;
}
.receipt-header {
    border-bottom: 1px dashed #3d3d3d;
    padding-bottom: 12px;
    margin-bottom: 12px;
    text-align: center;
}
.restaurant-name {
    font-size: 16px;
    font-weight: 700;
    color: #ffd43b;
    margin-bottom: 4px;
}
.receipt-meta {
    font-size: 12px;
    color: #adb5bd;
}
.item-row {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    font-size: 13px;
    color: #ffffff;
    border-bottom: 1px dotted #2d2d2d;
}
.item-row:last-child { border: none; }
.item-price {
    font-weight: 600;
    color: #ffd43b;
}
.total-row {
    display: flex;
    justify-content: space-between;
    padding-top: 10px;
    border-top: 1px solid #3d3d3d;
    font-weight: 700;
    font-size: 14px;
    margin-top: 8px;
    color: #ffffff;
}
.total-amount {
    color: #ffd43b;
    font-size: 16px;
}

[data-testid="stMetric"] {
    background: #1a1d26 !important;
    border: 1px solid #2d2d2d !important;
    border-radius: 8px !important;
    padding: 16px !important;
}
[data-testid="stMetricLabel"] {
    color: #adb5bd !important;
}
[data-testid="stMetricValue"] {
    color: #ffd43b !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid #2d2d2d !important;
    border-radius: 8px !important;
}

[data-testid="stChatMessage"] {
    background: #1a1d26 !important;
    border: 1px solid #2d2d2d !important;
    border-radius: 8px !important;
    color: #ffffff !important;
}

[data-testid="stChatInput"] textarea {
    background: #1a1d26 !important;
    color: #ffffff !important;
    border: 1px solid #3d3d3d !important;
    border-radius: 6px !important;
}

[data-testid="stExpander"] {
    background: #1a1d26 !important;
    border: 1px solid #2d2d2d !important;
    border-radius: 8px !important;
}

hr {
    border-color: #2d2d2d !important;
}

[data-testid="stAlert"] {
    border-radius: 6px !important;
    color: #ffffff !important;
}
</style>
"""