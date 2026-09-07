CARD = {
    "id": "VC-SF-027",
    "slots": [],
    "default_duration": 2.5,
    "css": r""".sting-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;align-items:center;justify-content:center;}
.sting-x{font-family:'Space Grotesk';font-weight:700;font-size:420px;color:#00D4AA;opacity:0;transform:scale(0.6);text-shadow:0 0 60px rgba(0,212,170,.0);}""",
    "body": r"""<div class="sting-wrap"><div class="sting-x" id="stingX">X</div></div>""",
    "seek": r"""
var x=(typeof x!=='undefined'&&x>0)?x:4;function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.12*x)/(0.23*x)));var xel=document.getElementById('stingX');
xel.style.opacity=Math.min(1,e*1.2);xel.style.transform='scale('+(0.6+0.4*e)+')';
var glow=40+80*Math.sin(clamp((t-0.12*x)/(0.5*x))*Math.PI);xel.style.textShadow='0 0 '+glow+'px rgba(0,212,170,'+(0.4+0.4*e)+')';
if(t>0.7*x){var f=clamp((t-0.7*x)/(0.27*x));xel.style.opacity=(1-f);}""",
}
