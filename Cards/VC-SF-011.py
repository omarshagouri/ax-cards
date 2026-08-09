# VC-SF-011  |  auto-fit safe-zone patch applied 2026-08-09
# Text shrink-to-fit added at top of seek(); css/body unchanged.
CARD = {
    "id": "VC-SF-011",
    "slots": ["HEADER", "ITEM1", "ITEM2", "ITEM3", "ITEM4"],
    "default_duration": 5.0,
    "css": r'''.list-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.list-h{font-family:'Space Grotesk';font-weight:700;font-size:58px;color:#FFFFFF;margin-bottom:44px;opacity:0;transform:translateY(28px);}
.li{display:flex;align-items:center;gap:28px;margin-bottom:34px;opacity:0;transform:translateY(30px);}
.li-n{flex:0 0 auto;width:66px;height:66px;border-radius:16px;background:#00D4AA;color:#0A1628;font-family:'Space Grotesk';font-weight:700;font-size:38px;display:flex;align-items:center;justify-content:center;}
.li-t{font-family:Inter;font-weight:500;font-size:46px;color:#FFFFFF;line-height:1.2;}''',
    "body": r'''<div class="list-wrap"><div class="list-h" id="lH">__HEADER__</div>
<div class="li" id="li1"><div class="li-n">1</div><div class="li-t">__ITEM1__</div></div>
<div class="li" id="li2"><div class="li-n">2</div><div class="li-t">__ITEM2__</div></div>
<div class="li" id="li3"><div class="li-n">3</div><div class="li-t">__ITEM3__</div></div>
<div class="li" id="li4"><div class="li-n">4</div><div class="li-t">__ITEM4__</div></div></div>''',
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

__fit(".list-h",888,150,0,0);__fit(".li-t",740,140,0,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
['li1','li2','li3','li4'].forEach(function(id){var el=document.getElementById(id);if(el&&el.textContent.indexOf('__')>-1){el.style.display='none';}});
show('lH',0.1,0.8,28);show('li1',0.6,1.3,30);show('li2',1.0,1.7,30);show('li3',1.4,2.1,30);show('li4',1.8,2.5,30);''',
}
