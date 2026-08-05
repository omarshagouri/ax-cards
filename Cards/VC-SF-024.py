CARD = {
    "id": "VC-SF-024",
    "slots": ["TITLE", "PATH", "X_LABEL", "Y_LABEL", "ANNOTATION"],
    "default_duration": 4.5,
    "css": r""".cl-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.cl-title{font-family:'Space Grotesk';font-weight:700;font-size:56px;color:#00D4AA;text-align:center;margin-bottom:44px;opacity:0;transform:translateY(24px);}
.cl-plot{position:relative;width:820px;height:460px;margin:0 auto;}
.cl-yl{position:absolute;left:-70px;top:50%;transform:translateY(-50%) rotate(-90deg);font-family:'Space Grotesk';font-weight:600;font-size:32px;color:#00D4AA;}
.cl-xl{position:absolute;bottom:-58px;left:50%;transform:translateX(-50%);font-family:'Space Grotesk';font-weight:600;font-size:32px;color:#00D4AA;}
.cl-anno{font-family:Inter;font-weight:500;font-size:38px;color:#FFFFFF;text-align:center;margin-top:80px;opacity:0;transform:translateY(22px);}""",
    "body": r"""<div class="cl-wrap"><div class="cl-title" id="clTitle">__TITLE__</div>
<div class="cl-plot"><svg width="820" height="460" viewBox="0 0 100 100" preserveAspectRatio="none" style="overflow:visible">
<line x1="0" y1="100" x2="100" y2="100" stroke="rgba(140,160,184,.4)" stroke-width="0.6"/>
<line x1="0" y1="0" x2="0" y2="100" stroke="rgba(140,160,184,.4)" stroke-width="0.6"/>
<polyline id="clPath" points="__PATH__" fill="none" stroke="#00D4AA" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
</svg><div class="cl-yl">__Y_LABEL__</div><div class="cl-xl">__X_LABEL__</div></div>
<div class="cl-anno" id="clAnno">__ANNOTATION__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('clTitle',0.1,0.8,24);
var p=document.getElementById('clPath');if(p){var len=p.getTotalLength?p.getTotalLength():500;p.style.strokeDasharray=len;var e=easeOutCubic(clamp((t-0.6)/1.5));p.style.strokeDashoffset=len*(1-e);}
show('clAnno',1.9,2.6,22);""",
}
