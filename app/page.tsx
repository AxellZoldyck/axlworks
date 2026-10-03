"use client";
import {useEffect,useRef,useState} from "react";

const projects=[
 {index:"01",name:"Rentalin",type:"SAAS / SYSTEM",text:"Billing, device control, and business operations for PS rental owners.",href:"https://rentalin.online"},
 {index:"02",name:"XL SATU",type:"WEB / COMMERCE",text:"A conversion-focused digital storefront for home internet sales.",href:"https://xlsatungebut.com"},
 {index:"03",name:"Kejar Target",type:"SAAS / GAMIFICATION",text:"Sales tracking, performance visibility, and team gamification.",href:"https://kejartarget.online"}
];

function MotionFrame(){return <div className="motion-frame"><div className="frame-depth"/><div className="frame-grid"/><div className="frame-orbit orbit-one"/><div className="frame-orbit orbit-two"/><div className="frame-orbit orbit-three"/><div className="frame-core"><span/><span/><span/></div><div className="frame-line line-a"/><div className="frame-line line-b"/><div className="frame-line line-c"/><div className="frame-label label-a">AXL / 026</div><div className="frame-label label-b">DIGITAL SYSTEMS</div></div>}

function Preview({href,name}:{href:string,name:string}){return <div className="live-preview"><div className="browser-bar"><i/><i/><i/><span>{name.toLowerCase().replace(/ /g,"-")}.online</span></div><iframe src={href} title={name+" live website preview"} loading="lazy"/></div>}

function Scene({kind,active,children}:{kind:string,active:boolean,children:React.ReactNode}){return <article className={"scene scene-"+kind+(active?" scene-active":"")} aria-hidden={!active}>{children}</article>}

export default function Home(){
 const stage=useRef<HTMLDivElement>(null); const [active,setActive]=useState(0); const [mouse,setMouse]=useState({x:0,y:0});
 useEffect(()=>{
  let raf=0;
  const update=()=>{
   if(!stage.current)return;
   const r=stage.current.getBoundingClientRect(), total=Math.max(1,r.height-innerHeight), p=Math.min(1,Math.max(0,-r.top/total)), scenes=stage.current.querySelectorAll<HTMLElement>(".scene"), n=scenes.length-1;
   const virtual=p*n;
   scenes.forEach((el,i)=>{
    const d=virtual-i, ad=Math.abs(d);
    const z=Math.min(1,ad);
    const x=d*105, y=d*13;
    el.style.setProperty("--x",x+"%");
    el.style.setProperty("--y",y+"%");
    el.style.setProperty("--scale",String(1-z*.72));
    el.style.setProperty("--rotate",String(d*3.5));
    el.style.setProperty("--opacity",String(Math.max(0,1-z*.7)));
    el.style.setProperty("--blur",Math.min(12,z*10)+"px");
    el.style.setProperty("--depth",String(-ad*500)+"px");
   });
   setActive(Math.min(n,Math.round(virtual))); raf=0;
  };
  const onScroll=()=>{if(!raf)raf=requestAnimationFrame(update)};
  const onMouse=(e:MouseEvent)=>setMouse({x:(e.clientX/innerWidth-.5)*2,y:(e.clientY/innerHeight-.5)*2});
  addEventListener("scroll",onScroll,{passive:true});addEventListener("resize",onScroll);addEventListener("mousemove",onMouse);
  update(); return()=>{removeEventListener("scroll",onScroll);removeEventListener("resize",onScroll);removeEventListener("mousemove",onMouse);cancelAnimationFrame(raf)};
 },[]);
 const scenes=[
  <Scene key="hero" kind="hero" active={active===0}><div className="scene-noise"/><div className="scene-copy"><p className="eyebrow"><b/> DIGITAL SYSTEMS / 2026</p><h1>BUILDING<br/><em>DIGITAL</em><br/>SYSTEMS.</h1><p>A small software lab exploring products, interfaces, and the space between engineering and visual design.</p><a className="button button-dark" href="#work">Enter the work ↘</a></div><div className="scene-art" style={{transform:`translate3d(${mouse.x*-14}px,${mouse.y*-10}px,0)`}}><MotionFrame/></div><div className="scene-meta">01 / INTRO</div></Scene>,
  <Scene key="manifesto" kind="manifesto" active={active===1}><span className="scene-number">02</span><div><p className="eyebrow">A DIFFERENT KIND OF PORTFOLIO</p><h2>One space.<br/><em>Many systems.</em></h2><p>Scroll is not navigation here. It is the camera.</p></div><div className="crosshair">+</div></Scene>,
  <Scene key="work" kind="work" active={active===2}><div className="scene-head"><p className="eyebrow">03 / SELECTED WORK</p><h2>Built, shipped,<br/><em>used.</em></h2></div><div className="work-mini-grid">{projects.map(p=><div className="mini-project" key={p.name}><Preview href={p.href} name={p.name}/><div><span>{p.index} / {p.type}</span><h3>{p.name}</h3></div></div>)}</div></Scene>,
  <Scene key="statement" kind="statement" active={active===3}><p className="eyebrow">04 / PRINCIPLE</p><div className="giant">MAKE<br/><i>IT</i><br/>MOVE.</div><div className="orbit-text">INTERACTION • MOTION • SYSTEMS • DETAIL •</div></Scene>,
  <Scene key="process" kind="process" active={active===4}><div><p className="eyebrow">05 / PROCESS</p><h2>Idea → interface<br/>→ <em>real product.</em></h2></div><div className="process-list"><div><b>01</b><strong>FRAME</strong><span>Find the problem.</span></div><div><b>02</b><strong>SHAPE</strong><span>Design the interaction.</span></div><div><b>03</b><strong>SHIP</strong><span>Build what gets used.</span></div></div></Scene>,
  <Scene key="lab" kind="lab" active={active===5}><div className="lab-disc"><div/><div/><div/><b>LAB</b></div><div><p className="eyebrow">06 / THE LAB</p><h2>Experiments<br/>become <em>software.</em></h2><p>Interfaces, motion studies, tools, concepts and systems in progress.</p></div></Scene>,
  <Scene key="contact" kind="contact" active={active===6}><p className="eyebrow">07 / CONTACT</p><h2>Have something<br/><em>worth building?</em></h2><a href="mailto:hello@axlworks.co">hello@axlworks.co ↗</a><span className="contact-mark">AXLWORKS</span></Scene>
 ];
 return <main>
  <nav className="nav"><a className="brand" href="#top">AXL<span>WORKS</span></a><div className="nav-links"><a href="#work">Work</a><a href="#lab">Lab</a><a href="#contact">Contact</a></div><a className="nav-status" href="https://github.com/AxellZoldyck/axlworks" target="_blank" rel="noreferrer"><i/> GitHub</a></nav>
  <div id="top" ref={stage} className="camera-stage"><div className="camera"><div className="camera-frame">{scenes}</div><div className="camera-ui"><span>SCENE {String(active+1).padStart(2,"0")} / 07</span><span>SCROLL TO ZOOM</span></div></div></div>
  <div id="work" className="anchor"/><div id="lab" className="anchor"/><div id="contact" className="anchor"/>
  <footer><div>AXLWORKS</div><div>DIGITAL SYSTEMS / 2026</div><div>© 2026</div></footer>
 </main>
}