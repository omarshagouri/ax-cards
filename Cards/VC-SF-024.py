# VC-SF-024  |  fix draw-on: dash length in screen px (was user units -> dashes) 2026-09-07
CARD = {
    "id": "VC-SF-024",
    "slots": ["TITLE", "PATH", "X_LABEL", "Y_LABEL", "ANNOTATION"],
    "default_duration": 4.5,
    "css": r'''.cl-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.cl-title{font-family:'Space Grotesk';font-weight:700;font-size:56px;color:#00D4AA;text-align:center;margin-bottom:44px;opacity:0;transform:translateY(24px);}
.cl-plot{position:relative;width:820px;height:460px;margin:0 auto;}
.cl-yl{position:absolute;left:-86px;top:50%;transform:translateY(-50%) rotate(-90deg);font-family:'Space Grotesk';font-weight:600;font-size:32px;color:#00D4AA;}
.cl-xl{position:absolute;bottom:-68px;left:50%;transform:translateX(-50%);font-family:'Space Grotesk';font-weight:600;font-size:32px;color:#00D4AA;}
.cl-anno{font-family:Inter;font-weight:500;font-size:38px;color:#FFFFFF;text-align:center;margin-top:80px;opacity:0;transform:translateY(22px);}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.cl-wrap{top:192px !important;height:988px !important;}

/* ax caption-safe v3: center ~y920, clamp bottom<=1340 (repo band bottom=1540) */
#axsafe{position:absolute;left:0;top:0;width:1080px;height:1920px;transform:translateY(230px);}
''',
    "body": r'''<div id="axsafe"><div class="cl-wrap"><div class="cl-title" id="clTitle">__TITLE__</div>
<div class="cl-plot"><svg width="820" height="460" style="overflow:visible">
<!-- Axes are drawn slightly longer than the plotting area to perfectly frame the data -->
<line x1="10" y1="450" x2="820" y2="450" stroke="rgba(140,160,184,.6)" stroke-width="2.5" stroke-linecap="round"/>
<line x1="10" y1="0" x2="10" y2="450" stroke="rgba(140,160,184,.6)" stroke-width="2.5" stroke-linecap="round"/>
<polyline id="clPath" points="__PATH__" fill="none" stroke="#00D4AA" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
</svg><div class="cl-yl">__Y_LABEL__</div><div class="cl-xl">__X_LABEL__</div></div>
<div class="cl-anno" id="clAnno">__ANNOTATION__</div></div></div>''',
    "seek": r'''
var x=(typeof x!=='undefined'&&x>0)?x:4;
var HOLD=1,ENTER=0.5;
function S(i,N){return N<2?0.12*x:0.12*x+(i/(N-1))*((x-HOLD-ENTER)-0.12*x);}
function E(i,N){return N<2?Math.min(x-HOLD,0.12*x+0.6):S(i,N)+ENTER;}
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

__fit(".cl-title",888,140,0,1);__fit(".cl-anno",888,180,0,1);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
show('clTitle',S(0,3),E(0,3),24);

var p=document.getElementById('clPath');
if(p){
  if(!p.dataset.mapped){
    var pts=(p.getAttribute('points')||'').trim().split(/\s+/).map(function(s){
      var xy=s.split(',');return [parseFloat(xy[0]),parseFloat(xy[1])];
    }).filter(function(a){return !isNaN(a[0])&&!isNaN(a[1]);});
    
    // Calculate mapping: scale 0-100 to an 800x440 zone to leave a 10px safe margin for rounded caps
    var sx=800/100, sy=440/100, len=0;
    var nPts=[];
    var px=0, py=0;
    for(var qi=0; qi<pts.length; qi++){
      var nx = 10 + pts[qi][0] * sx;
      var ny = 10 + (440 - pts[qi][1] * sy); // Safely invert the Y-axis mapping in JS
      nPts.push(nx + ',' + ny);
      if(qi > 0){
        var dx = nx - px, dy = ny - py;
        len += Math.sqrt(dx*dx + dy*dy);
      }
      px = nx; py = ny;
    }
    
    // Inject the physical screen-pixel points back into the SVG before animating
    p.setAttribute('points', nPts.join(' '));
    p.dataset.len = len || 800;
    p.dataset.mapped = '1';
  }
  
  var L=parseFloat(p.dataset.len);
  p.style.strokeDasharray = L;
  var e=easeOutCubic(clamp((t-S(1,3))/(E(1,3)-S(1,3))));
  p.style.strokeDashoffset = L * (1 - e);
}

show('clAnno',S(2,3),E(2,3),22);
'''
}
