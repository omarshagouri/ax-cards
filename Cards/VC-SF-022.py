CARD = {
    "id": "VC-SF-022",
    "slots": ["CTA_LINE"],
    "default_duration": 4.0,
    "css": r""".o-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.o-mark{font-family:'Space Grotesk';font-weight:700;font-size:130px;color:#FFFFFF;opacity:0;transform:translateY(30px);}
.o-mark .x{color:#00D4AA;text-shadow:0 0 30px rgba(0,212,170,.7);}
.o-tag{font-family:'Space Grotesk';font-weight:600;font-size:34px;letter-spacing:.22em;text-transform:uppercase;color:#00D4AA;margin-top:26px;opacity:0;transform:translateY(22px);}
.o-cta{font-family:Inter;font-weight:600;font-size:44px;color:#FFFFFF;margin-top:70px;opacity:0;transform:translateY(24px);}""",
    "body": r"""<div class="o-wrap"><div class="o-mark" id="oMark">AmpCore<span class="x">X</span></div><div class="o-tag" id="oTag">Battery intelligence for the electric age</div><div class="o-cta" id="oCta">__CTA_LINE__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('oMark',0.1,0.9,30);show('oTag',0.7,1.5,22);show('oCta',1.4,2.1,24);""",
}
