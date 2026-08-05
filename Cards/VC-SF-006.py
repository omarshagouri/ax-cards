CARD = {
    "id": "VC-SF-006",
    "slots": ["TERM", "DEFINITION"],
    "default_duration": 4.0,
    "css": r""".def-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.def-term{font-family:'Space Grotesk';font-weight:700;font-size:104px;color:#00D4AA;opacity:0;transform:translateY(30px);}
.def-eq{width:120px;height:4px;background:#8CA0B8;opacity:0;margin:36px 0;transform:scaleX(0);transform-origin:center;}
.def-body{font-family:'Space Grotesk';font-weight:600;font-size:62px;line-height:1.2;color:#FFFFFF;opacity:0;transform:translateY(30px);}""",
    "body": r"""<div class="def-wrap"><div class="def-term" id="defTerm">__TERM__</div><div class="def-eq" id="defEq"></div><div class="def-body" id="defBody">__DEFINITION__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('defTerm',0.10,0.85,30);
var e=easeOutCubic(clamp((t-0.6)/0.5));var eq=document.getElementById('defEq');eq.style.opacity=e;eq.style.transform='scaleX('+e+')';
show('defBody',0.95,1.7,30);""",
}
