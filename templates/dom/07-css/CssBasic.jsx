import './../cssRoot.css'

function CssBasic() {
  return (
    <>
    <div  id='css-basic' className="for-space"></div>
      <h1>CSS Basic</h1>
      <h2>* and body</h2>
      <h4>브라우져에서 기본적으로 margin, padding을 적용해서 이를 무시할려면 *에 margin, padding을 0으로 적용해야함</h4>
      <h4>그리고 box-sizing: border-box로 해야함</h4>
      <p>*는 모든 box에 적용되는 규칙을 적용</p>
      <pre>{`* { padding:0; margin:0; box-sizing: border-box; }`}</pre>
      <h2>inheritance</h2>
      <h4>font, padding, margin 관련된 사항은 상속 받으며, border는 상속되지 않음</h4>
      <h4>width, height는 parent에서 정한 것에 대한 비율로 지정됨</h4>
      <h5>rem은 root em으로 html, body에 대한 비율</h5>
      <h5>em은 자신이 속한 element 내의 font size에 대한 비율로 정해짐(1em은 font size 임)</h5>
      <h2>CSS에서 + 기호</h2>
      <h4>인접 형제 선택자(Adjacent Sibling Selector)를 의미<br/>
        이는 특정 요소 바로 뒤에 위치한 형제 요소를 선택하는 선택자입니다. 예를 들어, p + span은 {`<p>`} 요소 바로 뒤에 오는 {`<span>`} 요소를 선택</h4>

      <h2>Animation</h2>  
    <pre>{`.nav__home-animate {
/* 
animation-name: homenav;
animation-duration: 3s;
animation-timing-function: ease;
animation-delay: 0.5s;
animation-iteration-count: infinite; // 2
animation-direction: normal;
animation-fill-mode: forwards;
*/
animation: 3s ease 0.5s infinite normal forwards homenav;
}
@keyframes homenav {
0%, 100% {
  color: black;
}
50% {
  color: blueviolet;
}
}`}</pre>

    </>
  )
}

export default CssBasic
