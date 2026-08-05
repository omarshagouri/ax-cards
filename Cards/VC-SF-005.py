CARD = {
    "id": "VC-SF-005",
    "slots": ["BEAT_LINE"],
    "default_duration": 3.5,
    "css": r""".beat-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.beat-line{font-family:'Space Grotesk';font-weight:700;font-size:80px;line-height:1.14;color:#FFFFFF;opacity:0;transform:translateY(38px);}
.beat-rule{width:200px;height:4px;background:#00D4AA;border-radius:2px;margin-top:40px;transform:scaleX(0);transform-origin:center;}""",
    "body": r"""<div class="beat-wrap"><div class="beat-line" id="beatLine">__BEAT_LINE__</div><div class="beat-rule" id="beatRule"></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('beatLine',0.10,0.95,38);grow('beatRule',0.75,1.45);""",
}
