CARD = {
    "id": "VC-SF-010",
    "slots": ["COL1_TITLE", "COL1_POINT", "COL2_TITLE", "COL2_POINT", "COL3_TITLE", "COL3_POINT"],
    "default_duration": 4.5,
    "css": r""".col-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;justify-content:center;align-items:center;gap:40px;}
.col{width:270px;min-height:360px;background:rgba(10,22,40,.55);border:1px solid rgba(0,212,170,.35);border-radius:20px;padding:36px 26px;opacity:0;transform:translateY(40px);}
.col-t{font-family:'Space Grotesk';font-weight:700;font-size:40px;color:#00D4AA;line-height:1.1;}
.col-bar{width:52px;height:4px;background:#00D4AA;border-radius:2px;margin:20px 0 24px;}
.col-p{font-family:Inter;font-weight:400;font-size:38px;line-height:1.32;color:#FFFFFF;}""",
    "body": r"""<div class="col-wrap">
<div class="col" id="c1"><div class="col-t">__COL1_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL1_POINT__</div></div>
<div class="col" id="c2"><div class="col-t">__COL2_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL2_POINT__</div></div>
<div class="col" id="c3"><div class="col-t">__COL3_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL3_POINT__</div></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
['c1','c2','c3'].forEach(function(id){var el=document.getElementById(id);if(el&&el.textContent.indexOf('__')>-1){el.style.display='none';}});
show('c1',0.15,0.9,40);show('c2',0.6,1.35,40);show('c3',1.05,1.8,40);""",
}
