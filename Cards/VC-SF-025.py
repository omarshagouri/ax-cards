CARD = {
    "id": "VC-SF-025",
    "slots": ["USABLE_PCT", "TOP_BUFFER", "BOTTOM_BUFFER", "CAPTION"],
    "default_duration": 4.5,
    "css": r""".hb-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.hb-cap{font-family:'Space Grotesk';font-weight:700;font-size:54px;color:#FFFFFF;text-align:center;margin-bottom:50px;opacity:0;transform:translateY(24px);}
.hb-batt{position:relative;width:260px;height:600px;border:6px solid #8CA0B8;border-radius:26px;overflow:hidden;display:flex;flex-direction:column;}
.hb-seg{width:100%;height:0;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-weight:700;font-size:38px;color:#0A1628;overflow:hidden;}
.hb-top{background:rgba(255,122,60,.85);} .hb-use{background:#00D4AA;color:#0A1628;} .hb-bot{background:rgba(255,122,60,.85);}
.hb-legend{margin-top:40px;font-family:Inter;font-weight:500;font-size:34px;color:#8CA0B8;text-align:center;opacity:0;}""",
    "body": r"""<div class="hb-wrap"><div class="hb-cap" id="hbCap">__CAPTION__</div>
<div class="hb-batt"><div class="hb-seg hb-top" id="hbTop">buffer</div><div class="hb-seg hb-use" id="hbUse">__USABLE_PCT__ usable</div><div class="hb-seg hb-bot" id="hbBot">buffer</div></div>
<div class="hb-legend" id="hbLeg">Teal is what you use. Orange is the hidden reserve.</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('hbCap',0.1,0.85,24);
var top=parseFloat(('__TOP_BUFFER__'.match(/[\d.]+/)||[8])[0]);var bot=parseFloat(('__BOTTOM_BUFFER__'.match(/[\d.]+/)||[4])[0]);var use=parseFloat(('__USABLE_PCT__'.match(/[\d.]+/)||[88])[0]);
var e1=easeOutCubic(clamp((t-0.7)/0.5));document.getElementById('hbTop').style.height=(e1*top)+'%';
var e2=easeOutCubic(clamp((t-1.1)/0.8));document.getElementById('hbUse').style.height=(e2*use)+'%';
var e3=easeOutCubic(clamp((t-1.7)/0.5));document.getElementById('hbBot').style.height=(e3*bot)+'%';
document.getElementById('hbLeg').style.opacity=easeOutCubic(clamp((t-2.0)/0.6));""",
}
