CARD = {
    "id": "VC-SF-013",
    "slots": ["VALUE", "METRIC_LABEL", "SOURCE"],
    "default_duration": 4.0,
    "css": r""".g-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.g-ring{position:relative;width:520px;height:520px;}
.g-val{position:absolute;left:0;top:0;width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-weight:700;font-size:150px;color:#FFFFFF;opacity:0;}
.g-lab{margin-top:36px;font-family:'Space Grotesk';font-weight:600;font-size:40px;color:#8CA0B8;opacity:0;transform:translateY(24px);}
.src{position:absolute;left:96px;bottom:320px;display:flex;align-items:center;gap:20px;opacity:0;}
.src-bar{width:10px;height:44px;background:#00D4AA;border-radius:3px;}
.src-txt{font-family:Inter;font-weight:600;font-size:30px;color:#FFFFFF;}""",
    "body": r"""<div class="g-wrap"><div class="g-ring"><canvas id="gCanvas" width="520" height="520"></canvas><div class="g-val" id="gVal">__VALUE__</div></div>
<div class="g-lab" id="gLab">__METRIC_LABEL__</div>
<div class="src" id="gSrc"><div class="src-bar"></div><div class="src-txt">SOURCE: __SOURCE__</div></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var cv=document.getElementById('gCanvas');var ctx=cv.getContext('2d');var cx=260,cy=260,r=210;
var full=parseFloat(('__VALUE__'.match(/[\d.]+/)||[0])[0]);
var e=easeOutCubic(clamp((t-0.15)/1.1));var frac=(full/100)*e;
ctx.clearRect(0,0,520,520);ctx.lineWidth=34;ctx.lineCap='round';
ctx.strokeStyle='rgba(140,160,184,0.20)';ctx.beginPath();ctx.arc(cx,cy,r,0,Math.PI*2);ctx.stroke();
ctx.strokeStyle='#00D4AA';ctx.beginPath();ctx.arc(cx,cy,r,-Math.PI/2,-Math.PI/2+frac*Math.PI*2);ctx.stroke();
var gv=document.getElementById('gVal');gv.style.opacity=easeOutCubic(clamp((t-0.5)/0.6));
if(!gv.dataset.full){gv.dataset.full=gv.textContent;}
var num=(full*e);var suf=gv.dataset.full.replace(/[\d.\s]/g,'');gv.textContent=(Math.round(num))+suf;
show('gLab',1.1,1.7,24);
var s=document.getElementById('gSrc');if(s){var ok=s.textContent.indexOf('__')<0 && s.textContent.replace('SOURCE:','').trim().length>0;s.style.opacity=ok?easeOutCubic(clamp((t-1.5)/0.6)):0;}""",
}
