CARD = {
    "id": "VC-SF-021",
    "slots": ["ROLE_TEXT"],
    "default_duration": 3.5,
    "css": r""".lt-strip{position:absolute;left:96px;bottom:420px;display:flex;align-items:stretch;opacity:0;transform:translateX(-40px);}
.lt-accent{width:12px;background:#00D4AA;border-radius:4px;}
.lt-body{background:rgba(10,22,40,.85);border:1px solid rgba(0,212,170,.35);border-left:none;border-radius:0 14px 14px 0;padding:26px 36px;}
.lt-role{font-family:'Space Grotesk';font-weight:700;font-size:48px;color:#FFFFFF;}
.lt-sub{font-family:Inter;font-weight:500;font-size:32px;color:#00D4AA;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;}""",
    "body": r"""<div class="lt-strip" id="ltStrip"><div class="lt-accent"></div><div class="lt-body"><div class="lt-role">__ROLE_TEXT__</div><div class="lt-sub">AmpCoreX</div></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.1)/0.7));var s=document.getElementById('ltStrip');s.style.opacity=e;s.style.transform='translateX('+(-40*(1-e))+'px)';""",
}
