CARD = {
    "id": "VC-SF-007",
    "slots": ["WARNING_LINE", "DETAIL"],
    "default_duration": 4.0,
    "css": r""".warn-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.warn-tri{width:0;height:0;border-left:58px solid transparent;border-right:58px solid transparent;border-bottom:100px solid #FF7A3C;opacity:0;transform:translateY(24px);position:relative;}
.warn-tri::after{content:'!';position:absolute;left:-11px;top:34px;font-family:'Space Grotesk';font-weight:700;font-size:56px;color:#0A1628;}
.warn-pill{margin-top:34px;border:2px solid #FF7A3C;border-radius:12px;padding:12px 28px;font-family:'Space Grotesk';font-weight:600;font-size:30px;letter-spacing:.14em;color:#FF7A3C;opacity:0;transform:translateY(22px);}
.warn-line{margin-top:40px;font-family:'Space Grotesk';font-weight:700;font-size:74px;line-height:1.14;color:#FFFFFF;opacity:0;transform:translateY(34px);}
.warn-detail{margin-top:26px;font-family:Inter;font-weight:400;font-size:40px;line-height:1.3;color:#8CA0B8;opacity:0;transform:translateY(26px);}""",
    "body": r"""<div class="warn-wrap"><div class="warn-tri" id="wTri"></div><div class="warn-pill" id="wPill">WARNING</div><div class="warn-line" id="wLine">__WARNING_LINE__</div><div class="warn-detail" id="wDetail">__DETAIL__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('wTri',0.05,0.7,24);show('wPill',0.5,1.1,22);show('wLine',0.95,1.75,34);show('wDetail',1.5,2.2,26);
// subtle breathing pulse on the triangle during hold (keeps the screen alive)
if(t>2.2){var p=0.5+0.5*Math.sin((t-2.2)*3.2);document.getElementById('wTri').style.opacity=(0.8+0.2*p);}""",
}
