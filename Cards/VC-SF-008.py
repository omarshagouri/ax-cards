CARD = {
    "id": "VC-SF-008",
    "slots": ["CORRECT_LABEL", "CORRECT_ITEM", "WRONG_LABEL", "WRONG_ITEM"],
    "default_duration": 4.0,
    "css": r""".elim-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.elim-row{display:flex;width:888px;justify-content:space-between;position:relative;}
.elim-div{position:absolute;left:50%;top:6px;width:2px;height:280px;background:rgba(140,160,184,.35);transform:translateX(-1px) scaleY(0);transform-origin:top;}
.elim-col{width:400px;text-align:center;}
.elim-head{font-family:'Space Grotesk';font-weight:700;font-size:44px;letter-spacing:.04em;opacity:0;transform:translateY(24px);}
.elim-item{margin-top:34px;font-family:'Space Grotesk';font-weight:700;font-size:64px;line-height:1.12;color:#FFFFFF;opacity:0;transform:translateY(30px);}
.elim-ok{color:#00D4AA;} .elim-no{color:#FF7A3C;}
.elim-rule{width:260px;height:4px;background:#00D4AA;border-radius:2px;margin-top:56px;transform:scaleX(0);transform-origin:center;}""",
    "body": r"""<div class="elim-wrap"><div class="elim-row"><div class="elim-div" id="eDiv"></div>
<div class="elim-col"><div class="elim-head elim-ok" id="eH1">__CORRECT_LABEL__ &#10003;</div><div class="elim-item" id="eI1">__CORRECT_ITEM__</div></div>
<div class="elim-col"><div class="elim-head elim-no" id="eH2">__WRONG_LABEL__ &#10007;</div><div class="elim-item" id="eI2">__WRONG_ITEM__</div></div></div>
<div class="elim-rule" id="eRule"></div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var d=easeOutCubic(clamp((t-0.1)/0.5));document.getElementById('eDiv').style.transform='translateX(-1px) scaleY('+d+')';
show('eH1',0.35,0.95,24);show('eI1',0.7,1.35,30);show('eH2',0.95,1.55,24);show('eI2',1.3,1.95,30);grow('eRule',1.9,2.6);""",
}
