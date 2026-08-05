CARD = {
    "id": "VC-SF-019",
    "slots": ["QUOTE_TEXT", "SOURCE_NAME"],
    "default_duration": 4.5,
    "css": r""".q-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.q-mark{font-family:'Space Grotesk';font-weight:700;font-size:200px;line-height:0.6;color:#00D4AA;height:120px;opacity:0;transform:translateY(20px);}
.q-text{font-family:'Space Grotesk';font-weight:600;font-size:64px;line-height:1.24;color:#FFFFFF;opacity:0;transform:translateY(30px);}
.q-src{display:flex;align-items:center;gap:20px;margin-top:44px;opacity:0;transform:translateY(20px);}
.q-bar{width:52px;height:4px;background:#00D4AA;border-radius:2px;}
.q-name{font-family:Inter;font-weight:600;font-size:38px;color:#8CA0B8;letter-spacing:.02em;}""",
    "body": r"""<div class="q-wrap"><div class="q-mark" id="qMark">&#8220;</div><div class="q-text" id="qText">__QUOTE_TEXT__</div>
<div class="q-src" id="qSrc"><div class="q-bar"></div><div class="q-name">__SOURCE_NAME__</div></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('qMark',0.1,0.7,20);show('qText',0.55,1.4,30);show('qSrc',1.35,2.0,20);""",
}
