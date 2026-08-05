CARD = {
    "id": "VC-SF-020",
    "slots": ["TAG_TEXT"],
    "default_duration": 3.0,
    "css": r""".tag-chip{position:absolute;left:96px;top:300px;display:inline-flex;align-items:center;gap:16px;background:rgba(10,22,40,.82);border:2px solid #00D4AA;border-radius:14px;padding:20px 30px;opacity:0;transform:translateX(-30px);}
.tag-dot{width:16px;height:16px;border-radius:50%;background:#00D4AA;}
.tag-t{font-family:'Space Grotesk';font-weight:600;font-size:40px;letter-spacing:.06em;color:#FFFFFF;text-transform:uppercase;}""",
    "body": r"""<div class="tag-chip" id="tagChip"><div class="tag-dot"></div><div class="tag-t">__TAG_TEXT__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.1)/0.6));var c=document.getElementById('tagChip');c.style.opacity=e;c.style.transform='translateX('+(-30*(1-e))+'px)';""",
}
