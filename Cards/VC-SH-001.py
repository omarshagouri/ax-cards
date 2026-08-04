# VC-SH-001.py — AmpCoreX Visual Card — Stat (hero number)
CARD = {
    "id": "VC-SH-001",
    "slots": ["KICKER", "NUM", "PCT"],
    "default_duration": 3.0,
    "css": """
        #block{ position:absolute; top:430px; left:0; width:1080px; text-align:center; }
        .kicker{ color:#8CA0B8; font-size:56px; font-weight:500; letter-spacing:6px;
                 text-transform:uppercase; margin:0 0 10px; clip-path: inset(0 100% 0 0); }
        .hero{ color:#FFFFFF; font-size:300px; font-weight:700; margin:0; line-height:1;
               opacity:0; transform: scale(0.85); }
        .hero .key{ color:#00D4AA; }
    """,
    "body": """
        <div id="block">
            <p class="kicker" id="kick">__KICKER__</p>
            <h1 class="hero" id="hero">__NUM__<span class="key">__PCT__</span></h1>
        </div>
    """,
    "seek": """
        var kick = document.getElementById('kick');
        var hero = document.getElementById('hero');
        var we = easeOutCubic(clamp((t - 0.0) / 1.0));
        kick.style.clipPath = 'inset(0 ' + (100 * (1 - we)) + '% 0 0)';
        var pp = clamp((t - 1.0) / 0.5);
        hero.style.opacity = pp > 0 ? 1 : 0;
        var scale;
        if (pp < 0.6){ scale = 0.85 + (1.05 - 0.85) * easeOutCubic(pp / 0.6); }
        else { scale = 1.05 - (1.05 - 1.0) * easeOutCubic((pp - 0.6) / 0.4); }
        hero.style.transform = 'scale(' + scale + ')';
    """,
}
