"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[5794],{75794:(t,e,a)=>{a.r(e);a.d(e,{diagram:()=>R});var n=a(91760);var i=a(34596);var s=a(96001);var r=a(30573);var d=a(23787);var o=a(27484);var c=a.n(o);var g=a(17967);var l=a(27856);var p=a.n(l);const h={};const f=(t,e)=>{h[t]=e};const x=t=>h[t];const u=()=>Object.keys(h);const y=()=>u().length;const w={get:x,set:f,keys:u,size:y};const b=t=>t.append("circle").attr("class","start-state").attr("r",(0,d.c)().state.sizeUnit).attr("cx",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit).attr("cy",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit);const B=t=>t.append("line").style("stroke","grey").style("stroke-dasharray","3").attr("x1",(0,d.c)().state.textHeight).attr("class","divider").attr("x2",(0,d.c)().state.textHeight*2).attr("y1",0).attr("y2",0);const m=(t,e)=>{const a=t.append("text").attr("x",2*(0,d.c)().state.padding).attr("y",(0,d.c)().state.textHeight+2*(0,d.c)().state.padding).attr("font-size",(0,d.c)().state.fontSize).attr("class","state-title").text(e.id);const n=a.node().getBBox();t.insert("rect",":first-child").attr("x",(0,d.c)().state.padding).attr("y",(0,d.c)().state.padding).attr("width",n.width+2*(0,d.c)().state.padding).attr("height",n.height+2*(0,d.c)().state.padding).attr("rx",(0,d.c)().state.radius);return a};const k=(t,e)=>{const a=function(t,e,a){const n=t.append("tspan").attr("x",2*(0,d.c)().state.padding).text(e);if(!a){n.attr("dy",(0,d.c)().state.textHeight)}};const n=t.append("text").attr("x",2*(0,d.c)().state.padding).attr("y",(0,d.c)().state.textHeight+1.3*(0,d.c)().state.padding).attr("font-size",(0,d.c)().state.fontSize).attr("class","state-title").text(e.descriptions[0]);const i=n.node().getBBox();const s=i.height;const r=t.append("text").attr("x",(0,d.c)().state.padding).attr("y",s+(0,d.c)().state.padding*.4+(0,d.c)().state.dividerMargin+(0,d.c)().state.textHeight).attr("class","state-description");let o=true;let c=true;e.descriptions.forEach((function(t){if(!o){a(r,t,c);c=false}o=false}));const g=t.append("line").attr("x1",(0,d.c)().state.padding).attr("y1",(0,d.c)().state.padding+s+(0,d.c)().state.dividerMargin/2).attr("y2",(0,d.c)().state.padding+s+(0,d.c)().state.dividerMargin/2).attr("class","descr-divider");const l=r.node().getBBox();const p=Math.max(l.width,i.width);g.attr("x2",p+3*(0,d.c)().state.padding);t.insert("rect",":first-child").attr("x",(0,d.c)().state.padding).attr("y",(0,d.c)().state.padding).attr("width",p+2*(0,d.c)().state.padding).attr("height",l.height+s+2*(0,d.c)().state.padding).attr("rx",(0,d.c)().state.radius);return t};const v=(t,e,a)=>{const n=(0,d.c)().state.padding;const i=2*(0,d.c)().state.padding;const s=t.node().getBBox();const r=s.width;const o=s.x;const c=t.append("text").attr("x",0).attr("y",(0,d.c)().state.titleShift).attr("font-size",(0,d.c)().state.fontSize).attr("class","state-title").text(e.id);const g=c.node().getBBox();const l=g.width+i;let p=Math.max(l,r);if(p===r){p=p+i}let h;const f=t.node().getBBox();if(e.doc);h=o-n;if(l>r){h=(r-p)/2+n}if(Math.abs(o-f.x)<n&&l>r){h=o-(l-r)/2}const x=1-(0,d.c)().state.textHeight;t.insert("rect",":first-child").attr("x",h).attr("y",x).attr("class",a?"alt-composit":"composit").attr("width",p).attr("height",f.height+(0,d.c)().state.textHeight+(0,d.c)().state.titleShift+1).attr("rx","0");c.attr("x",h+n);if(l<=r){c.attr("x",o+(p-i)/2-l/2+n)}t.insert("rect",":first-child").attr("x",h).attr("y",(0,d.c)().state.titleShift-(0,d.c)().state.textHeight-(0,d.c)().state.padding).attr("width",p).attr("height",(0,d.c)().state.textHeight*3).attr("rx",(0,d.c)().state.radius);t.insert("rect",":first-child").attr("x",h).attr("y",(0,d.c)().state.titleShift-(0,d.c)().state.textHeight-(0,d.c)().state.padding).attr("width",p).attr("height",f.height+3+2*(0,d.c)().state.textHeight).attr("rx",(0,d.c)().state.radius);return t};const N=t=>{t.append("circle").attr("class","end-state-outer").attr("r",(0,d.c)().state.sizeUnit+(0,d.c)().state.miniPadding).attr("cx",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit+(0,d.c)().state.miniPadding).attr("cy",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit+(0,d.c)().state.miniPadding);return t.append("circle").attr("class","end-state-inner").attr("r",(0,d.c)().state.sizeUnit).attr("cx",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit+2).attr("cy",(0,d.c)().state.padding+(0,d.c)().state.sizeUnit+2)};const E=(t,e)=>{let a=(0,d.c)().state.forkWidth;let n=(0,d.c)().state.forkHeight;if(e.parentId){let t=a;a=n;n=t}return t.append("rect").style("stroke","black").style("fill","black").attr("width",a).attr("height",n).attr("x",(0,d.c)().state.padding).attr("y",(0,d.c)().state.padding)};const M=(t,e,a,n)=>{let i=0;const s=n.append("text");s.style("text-anchor","start");s.attr("class","noteText");let r=t.replace(/\r\n/g,"<br/>");r=r.replace(/\n/g,"<br/>");const o=r.split(d.e.lineBreakRegex);let c=1.25*(0,d.c)().state.noteMargin;for(const g of o){const t=g.trim();if(t.length>0){const n=s.append("tspan");n.text(t);if(c===0){const t=n.node().getBBox();c+=t.height}i+=c;n.attr("x",e+(0,d.c)().state.noteMargin);n.attr("y",a+i+1.25*(0,d.c)().state.noteMargin)}}return{textWidth:s.node().getBBox().width,textHeight:i}};const S=(t,e)=>{e.attr("class","state-note");const a=e.append("rect").attr("x",0).attr("y",(0,d.c)().state.padding);const n=e.append("g");const{textWidth:i,textHeight:s}=M(t,0,0,n);a.attr("height",s+2*(0,d.c)().state.noteMargin);a.attr("width",i+(0,d.c)().state.noteMargin*2);return a};const z=function(t,e){const a=e.id;const n={id:a,label:e.id,width:0,height:0};const i=t.append("g").attr("id",a).attr("class","stateGroup");if(e.type==="start"){b(i)}if(e.type==="end"){N(i)}if(e.type==="fork"||e.type==="join"){E(i,e)}if(e.type==="note"){S(e.note.text,i)}if(e.type==="divider"){B(i)}if(e.type==="default"&&e.descriptions.length===0){m(i,e)}if(e.type==="default"&&e.descriptions.length>0){k(i,e)}const s=i.node().getBBox();n.width=s.width+2*(0,d.c)().state.padding;n.height=s.height+2*(0,d.c)().state.padding;w.set(a,n);return n};let H=0;const T=function(t,e,a){const s=function(t){switch(t){case n.d.relationType.AGGREGATION:return"aggregation";case n.d.relationType.EXTENSION:return"extension";case n.d.relationType.COMPOSITION:return"composition";case n.d.relationType.DEPENDENCY:return"dependency"}};e.points=e.points.filter((t=>!Number.isNaN(t.y)));const r=e.points;const o=(0,i.jvg)().x((function(t){return t.x})).y((function(t){return t.y})).curve(i.$0Z);const c=t.append("path").attr("d",o(r)).attr("id","edge"+H).attr("class","transition");let g="";if((0,d.c)().state.arrowMarkerAbsolute){g=window.location.protocol+"//"+window.location.host+window.location.pathname+window.location.search;g=g.replace(/\(/g,"\\(");g=g.replace(/\)/g,"\\)")}c.attr("marker-end","url("+g+"#"+s(n.d.relationType.DEPENDENCY)+"End)");if(a.title!==void 0){const n=t.append("g").attr("class","stateLabel");const{x:i,y:s}=d.u.calcLabelPosition(e.points);const r=d.e.getRows(a.title);let o=0;const c=[];let g=0;let l=0;for(let t=0;t<=r.length;t++){const e=n.append("text").attr("text-anchor","middle").text(r[t]).attr("x",i).attr("y",s+o);const a=e.node().getBBox();g=Math.max(g,a.width);l=Math.min(l,a.x);d.l.info(a.x,i,s+o);if(o===0){const t=e.node().getBBox();o=t.height;d.l.info("Title height",o,s)}c.push(e)}let p=o*r.length;if(r.length>1){const t=(r.length-1)*o*.5;c.forEach(((e,a)=>e.attr("y",s+a*o-t)));p=o*r.length}const h=n.node().getBBox();n.insert("rect",":first-child").attr("class","box").attr("x",i-g/2-(0,d.c)().state.padding/2).attr("y",s-p/2-(0,d.c)().state.padding/2-3.5).attr("width",g+(0,d.c)().state.padding).attr("height",p+(0,d.c)().state.padding);d.l.info(h)}H++};let G;const L={};const O=function(){};const A=function(t){t.append("defs").append("marker").attr("id","dependencyEnd").attr("refX",19).attr("refY",7).attr("markerWidth",20).attr("markerHeight",28).attr("orient","auto").append("path").attr("d","M 19,7 L9,13 L14,7 L9,1 Z")};const D=function(t,e,a,n){G=(0,d.c)().state;const s=(0,d.c)().securityLevel;let r;if(s==="sandbox"){r=(0,i.Ys)("#i"+e)}const o=s==="sandbox"?(0,i.Ys)(r.nodes()[0].contentDocument.body):(0,i.Ys)("body");const c=s==="sandbox"?r.nodes()[0].contentDocument:document;d.l.debug("Rendering diagram "+t);const g=o.select(`[id='${e}']`);A(g);const l=n.db.getRootDoc();U(l,g,void 0,false,o,c,n);const p=G.padding;const h=g.node().getBBox();const f=h.width+p*2;const x=h.height+p*2;const u=f*1.75;(0,d.i)(g,x,u,G.useMaxWidth);g.attr("viewBox",`${h.x-G.padding}  ${h.y-G.padding} `+f+" "+x)};const P=t=>t?t.length*G.fontSizeFactor:1;const U=(t,e,a,n,i,o,c)=>{const g=new r.k({compound:true,multigraph:true});let l;let p=true;for(l=0;l<t.length;l++){if(t[l].stmt==="relation"){p=false;break}}if(a){g.setGraph({rankdir:"LR",multigraph:true,compound:true,ranker:"tight-tree",ranksep:p?1:G.edgeLengthFactor,nodeSep:p?1:50,isMultiGraph:true})}else{g.setGraph({rankdir:"TB",multigraph:true,compound:true,ranksep:p?1:G.edgeLengthFactor,nodeSep:p?1:50,ranker:"tight-tree",isMultiGraph:true})}g.setDefaultEdgeLabel((function(){return{}}));c.db.extract(t);const h=c.db.getStates();const f=c.db.getRelations();const x=Object.keys(h);for(const s of x){const t=h[s];if(a){t.parentId=a}let r;if(t.doc){let a=e.append("g").attr("id",t.id).attr("class","stateGroup");r=U(t.doc,a,t.id,!n,i,o,c);{a=v(a,t,n);let e=a.node().getBBox();r.width=e.width;r.height=e.height+G.padding/2;L[t.id]={y:G.compositTitleSize}}}else{r=z(e,t)}if(t.note){const a={descriptions:[],id:t.id+"-note",note:t.note,type:"note"};const n=z(e,a);if(t.note.position==="left of"){g.setNode(r.id+"-note",n);g.setNode(r.id,r)}else{g.setNode(r.id,r);g.setNode(r.id+"-note",n)}g.setParent(r.id,r.id+"-group");g.setParent(r.id+"-note",r.id+"-group")}else{g.setNode(r.id,r)}}d.l.debug("Count=",g.nodeCount(),g);let u=0;f.forEach((function(t){u++;d.l.debug("Setting edge",t);g.setEdge(t.id1,t.id2,{relation:t,width:P(t.title),height:G.labelHeight*d.e.getRows(t.title).length,labelpos:"c"},"id"+u)}));(0,s.bK)(g);d.l.debug("Graph after layout",g.nodes());const y=e.node();g.nodes().forEach((function(t){if(t!==void 0&&g.node(t)!==void 0){d.l.warn("Node "+t+": "+JSON.stringify(g.node(t)));i.select("#"+y.id+" #"+t).attr("transform","translate("+(g.node(t).x-g.node(t).width/2)+","+(g.node(t).y+(L[t]?L[t].y:0)-g.node(t).height/2)+" )");i.select("#"+y.id+" #"+t).attr("data-x-shift",g.node(t).x-g.node(t).width/2);const e=o.querySelectorAll("#"+y.id+" #"+t+" .divider");e.forEach((t=>{const e=t.parentElement;let a=0;let n=0;if(e){if(e.parentElement){a=e.parentElement.getBBox().width}n=parseInt(e.getAttribute("data-x-shift"),10);if(Number.isNaN(n)){n=0}}t.setAttribute("x1",0-n+8);t.setAttribute("x2",a-n-8)}))}else{d.l.debug("No Node "+t+": "+JSON.stringify(g.node(t)))}}));let w=y.getBBox();g.edges().forEach((function(t){if(t!==void 0&&g.edge(t)!==void 0){d.l.debug("Edge "+t.v+" -> "+t.w+": "+JSON.stringify(g.edge(t)));T(e,g.edge(t),g.edge(t).relation)}}));w=y.getBBox();const b={id:a?a:"root",label:a?a:"root",width:0,height:0};b.width=w.width+2*G.padding;b.height=w.height+2*G.padding;d.l.debug("Doc rendered",b,g);return b};const C={setConf:O,draw:D};const R={parser:n.p,db:n.d,renderer:C,styles:n.s,init:t=>{if(!t.state){t.state={}}t.state.arrowMarkerAbsolute=t.arrowMarkerAbsolute;n.d.clear()}}}}]);