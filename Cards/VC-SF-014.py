CARD = {
    "id": "VC-SF-014",
    "slots": ["TEMP", "CAPTION", "SOURCE"],
    "default_duration": 4.0,
    "css": r""".th-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.th-cap{font-family:'Space Grotesk';font-weight:700;font-size:56px;color:#FFFFFF;margin-bottom:56px;text-align:center;opacity:0;transform:translateY(26px);}
.th-row{display:flex;align-items:flex-end;gap:44px;}
.th-tube{position:relative;width:78px;height:520px;background:rgba(140,160,184,.16);border-radius:40px;overflow:hidden;}
.th-merc{position:absolute;left:0;bottom:0;width:100%;height:0;background:linear-gradient(180deg,#FF7A3C,#00D4AA);}
.th-val{font-family:'Space Grotesk';font-weight:700;font-size:110px;color:#FFFFFF;opacity:0;transform:translateY(28px);}""",
    "body": r"""<div class="th-wrap"><div class="th-cap" id="thCap">__CAPTION__</div>
<div class="th-row"><div class="th-tube"><div class="th-merc" id="thMerc"></div></div><div class="th-val" id="thVal">__TEMP__</div></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('thCap',0.1,0.85,26);
var e=easeOutCubic(clamp((t-0.7)/1.0));document.getElementById('thMerc').style.height=(e*100)+'%';
show('thVal',1.3,2.0,28);""",
}
