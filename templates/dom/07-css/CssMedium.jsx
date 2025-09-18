import React from 'react'
import './../cssRoot.css';

function CssMedium() {
  return (
    <>
      <div id='css-medium'className="for-space"></div>
      <h1>CSS Medium</h1>
      <h2>list style</h2>
      <p>list-style-type: none;를 적용하면 list의 기본 bullet이 사라짐, padding:0 해야 들어감</p>
      <p>list-style-type: square, circle, lower-alpha, lower-roman, ...</p>
      <p>list-style: [-type] [-image] [-position]</p>
      <p>순서는 type은 fault back이고 position은 inside, outside가 있음</p>
      <pre>list-style-image: url(이미지경로)</pre>

      <h2>pseudo class</h2>
      <p>pseudo class는 특정 상태에 있는 element를 선택할 때 사용</p>
      <p>예를 들어, a:hover는 마우스가 링크 위에 있을 때 적용됨</p>
      <pre>{`a:hover { color: red; }`}</pre>
      <p>다른 예로, :first-child, :last-child, :nth-child( 2 | even | odd ) 등이 있습니다.</p>
      <pre>{`p:first-child { color: blue; }`}</pre>
      <p>::marker 해서 지정하면 리스트 아이템의 마커 스타일을 변경할 수 있습니다.</p>
      <pre>{`li::marker {
  color: green; 
  font-weight: bold;
  content: "•"; /* 여기에 머리글을 지정하는 뭐든지 넣을 수 있음 */
}`}</pre>
      <pre>{`p::before {  content: "Before: ";  // 요소의 내용 앞에 추가할 콘텐츠 }`}</pre>

      <h2>float</h2>
      <p>이미지나 컨테이너의 위치를 flow의 중간에 삽입하는 기능</p>
      <pre>{`img {
  float: left; // right
  margin: 0 15px 15px 0; // 마진을 여기서 정의해야함
}`}</pre>
      <h3>clear</h3>
      <p>float property 제거</p>
      <pre>{`div { clear: both; }`}</pre>
      <h3>float</h3>
      <h4>자신이 포함된 container의 높이를 넘어섰을 때 이를 보정하기 위해서</h4>
      <p>상위 컴포넌트에 display: flow-root;를 적용하면 float를 사용한 자식 컴포넌트의 높이를 보정할 수 있습니다.</p>
      <p>또는 clearfix를 적용할 수도 있습니다.</p>
      <pre>{`.clearfix::after {   
  content: "";
  display: table;
  clear: both;
}`}</pre>
    <h2>column</h2>
      <p>column-count, conlumn-width, column-rule(right border), column-gap의 속성을 갖음</p>
      <h4>chrome에서는 -webkit-perspective:1; 를 해주어야함</h4>
      <h4>break-inside: avoid; 해주면 해당 box가 분리되서 표시되는 것을 막을 수 있음</h4>
      <p>이게 없으면 중간에 컬럼이 조정되면서 내용이 잘려서 넘어감</p>
      <p>column-span:all; 하면 중간에 끈고 들어가서 표시함</p>
      <p>다시한번 우선순위는 점수 계산 잘해서 적용해야함, nowrap 적용시 적용한 곳 앞에 공백이 있어야함</p>
      <div className="columns"> <h4 style={{background:"gray", textAlign:"center"}}>적용 예시</h4>
        <p style={{borderBottom: '2px solid #333'}}>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, illum.</p>
        <p style={{borderBottom: '2px solid #333'}}>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, illum.</p>
        <h2>break-inside column</h2>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, illum.</p>
        <p>html 특수문자: unicode.table-com에 많이 있음</p>
        <div className="quote">&#8220;column-span:all;&#8221; 
          <span className='nowrap'>&#8212;.span.nowrap</span></div>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, illum.</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt, illum.</p>
      </div>
    </>
  )
}

export default CssMedium
