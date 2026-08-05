CARD = {
    "id": "VC-SF-026",
    "slots": ["SOURCE_NAME"],
    "default_duration": 2.5,
    "css": r""".st-tag{position:absolute;left:96px;bottom:320px;display:flex;align-items:center;gap:20px;opacity:0;transform:translateX(-24px);}
.st-bar{width:12px;height:48px;background:#00D4AA;border-radius:3px;}
.st-txt{font-family:Inter;font-weight:600;font-size:32px;color:#FFFFFF;letter-spacing:.02em;}""",
    "body": r"""<div class="st-tag" id="stTag"><div class="st-bar"></div><div class="st-txt">SOURCE: __SOURCE_NAME__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.1)/0.6));var el=document.getElementById('stTag');el.style.opacity=e;el.style.transform='translateX('+(-24*(1-e))+'px)';""",
}
