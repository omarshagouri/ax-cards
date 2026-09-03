# VC-SF-025  |  caption-safe-zone pass 2026-08-18
CARD = {
    "id": "VC-SF-025",
    "slots": ["USABLE_PCT", "TOP_BUFFER", "BOTTOM_BUFFER", "CAPTION"],
    "default_duration": 4.5,
    "css": r'''.hb-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.hb-cap{font-family:'Space Grotesk';font-weight:700;font-size:54px;color:#FFFFFF;text-align:center;margin-bottom:50px;opacity:0;transform:translateY(24px);}
.hb-batt{position:relative;width:260px;height:600px;border:6px solid #8CA0B8;border-radius:26px;overflow:hidden;display:flex;flex-direction:column;}
.hb-seg{width:100%;height:0;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-weight:700;font-size:38px;color:#0A1628;overflow:hidden;}
.hb-top{background:rgba(255,122,60,.85);} .hb-use{background:#00D4AA;color:#0A1628;} .hb-bot{background:rgba(255,122,60,.85);}
.hb-legend{margin-top:40px;font-family:Inter;font-weight:500;font-size:34px;color:#8CA0B8;text-align:center;opacity:0;}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.hb-wrap{top:192px !important;height:988px !important;}

/* ax caption-safe v3: center ~y920, clamp bottom<=1340 (repo band bottom=1540) */
#axsafe{position:absolute;left:0;top:0;width:1080px;height:1920px;transform:translateY(230px);}
''',
    "body": r'''<div id="axsafe"><div class="hb-wrap"><div class="hb-cap" id="hbCap">__CAPTION__</div>
<div class="hb-batt"><div class="hb-seg hb-top" id="hbTop">buffer</div><div class="hb-seg hb-use" id="hbUse">__USABLE_PCT__ usable</div><div class="hb-seg hb-bot" id="hbBot">buffer</div></div>
<div class="hb-legend" id="hbLeg">Teal is what you use. Orange is the hidden reserve.</div></div></div>''',
    "seek": r'''
if(!window.__fit){window.__fit=function(sel,maxW,maxH,line,center){
var els=document.querySelectorAll(sel);var ready=(!document.fonts)||document.fonts.status==='loaded';
for(var i=0;i<els.length;i++){var el=els[i];
if(el.dataset.fitok==='1'){el.style.fontSize=el.dataset.fitpx+'px';continue;}
if(!el.dataset.fbase){el.dataset.fbase=(parseFloat(getComputedStyle(el).fontSize)||40);}
if(maxW){el.style.maxWidth=maxW+'px';if(center){el.style.marginLeft='auto';el.style.marginRight='auto';}}
el.style.whiteSpace=line?'nowrap':'normal';if(!line){el.style.overflowWrap='break-word';el.style.wordBreak='break-word';}
var size=parseFloat(el.dataset.fbase);el.style.fontSize=size+'px';var g=0;
while(size>16&&g<240&&(el.scrollWidth>el.clientWidth+0.5||(maxH&&el.scrollHeight>maxH+0.5))){size-=2;el.style.fontSize=size+'px';g++;}
if(ready){el.dataset.fitpx=size;el.dataset.fitok='1';}}
};}

__fit(".hb-cap",900,180,0,1);__fit(".hb-use",0,0,1,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('hbCap',0.1,0.85,24);
var top=parseFloat(('__TOP_BUFFER__'.match(/[\d.]+/)||[8])[0]);var bot=parseFloat(('__BOTTOM_BUFFER__'.match(/[\d.]+/)||[4])[0]);var use=parseFloat(('__USABLE_PCT__'.match(/[\d.]+/)||[88])[0]);
var e1=easeOutCubic(clamp((t-0.7)/0.5));document.getElementById('hbTop').style.height=(e1*top)+'%';
var e2=easeOutCubic(clamp((t-1.1)/0.8));document.getElementById('hbUse').style.height=(e2*use)+'%';
var e3=easeOutCubic(clamp((t-1.7)/0.5));document.getElementById('hbBot').style.height=(e3*bot)+'%';
document.getElementById('hbLeg').style.opacity=easeOutCubic(clamp((t-2.0)/0.6));''',
}
