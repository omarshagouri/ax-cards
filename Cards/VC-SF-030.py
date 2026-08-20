CARD = {
    "id": "VC-SF-030",
    "name": "Blueprint Sequential Build",
    "default_duration": 6.0,
    "slots": ["HOOK", "DATA_LABEL", "DATA_VALUE", "TAKEAWAY"],
    "css": """
        .grid-container { display: flex; flex-direction: column; height: 100%; padding: 30px; box-sizing: border-box; background: #0f1115; color: #e2e8f0; border: 1px solid #334155; border-radius: 8px; }
        .header-block, .data-block, .footer-block { opacity: 0; }
        .header-block { border-bottom: 1px solid #334155; padding-bottom: 20px; }
        .tag { font-family: 'JetBrains Mono', monospace; color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
        .title { font-family: 'Space Grotesk', sans-serif; font-size: 24px; font-weight: 700; color: #f8fafc; line-height: 1.2; }
        .data-block { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; }
        .data-row { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 15px; }
        .chem-label { font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 700; }
        .chem-value { font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 400; color: #38bdf8; }
        .footer-block { background: #1e293b; padding: 20px; border-radius: 6px; border-left: 3px solid #38bdf8; }
        .footer-title { font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700; color: #38bdf8; margin-bottom: 8px; text-transform: uppercase;}
        .footer-text { font-size: 13px; line-height: 1.5; color: #cbd5e1; }
    """,
    "body": """
        <div class="grid-container">
            <div class="header-block" id="block-1">
                <div class="tag">Analysis</div>
                <div class="title">__HOOK__</div>
            </div>
            <div class="data-block" id="block-2">
                <div class="data-row">
                    <div class="chem-label">__DATA_LABEL__</div>
                    <div class="chem-value">__DATA_VALUE__</div>
                </div>
            </div>
            <div class="footer-block" id="block-3">
                <div class="footer-title">Engineering Note</div>
                <div class="footer-text">__TAKEAWAY__</div>
            </div>
        </div>
    """,
    "seek": """
        function easeOutCubic(p) { return 1 - Math.pow(1 - p, 3); }
        
        let p1 = clamp(t / 0.6);
        let e1 = easeOutCubic(p1);
        let block1 = document.getElementById('block-1');
        block1.style.opacity = e1;
        block1.style.transform = `translateY(${(1 - e1) * 20}px)`;

        // At 2.5s, reveal the data
        let p2 = clamp((t - 2.5) / 0.6);
        let e2 = easeOutCubic(p2);
        let block2 = document.getElementById('block-2');
        block2.style.opacity = e2;
        block2.style.transform = `translateY(${(1 - e2) * 20}px)`;

        // At 4.5s, reveal the takeaway
        let p3 = clamp((t - 4.5) / 0.6);
        let e3 = easeOutCubic(p3);
        let block3 = document.getElementById('block-3');
        block3.style.opacity = e3;
        block3.style.transform = `translateY(${(1 - e3) * 20}px)`;
    """
}
