function CssAlignElements() {
  return (
    <>
      <div className="for-space" id='css-align-elements'></div>

      <h1>Flow</h1>

      <h2>Position</h2>
      <h3>relative(기본), absolute, sticky, fixed</h3>
      <p>absolute는 상위 element 중 relative 기준으로 위치를 정의함</p>
      <pre>position: absolute; top:0; left:2rem;</pre>
      <p>sticky는 window 기준 스크롤 시에 위치를 갖음</p>
      <pre>position: sticky; top:0</pre>
      <p>fixed는 window 기준 절대값을 가짐. 스크롤 시에도 위치가 고정됨</p>
      <pre>position:fixed; top:0;</pre>

      <h2>flex 속성</h2>
      <h3>display: flex; flex-direction: [row, column, row-reverse, column-reverse]</h3>
      <p>flex-wrap: nowrap/wrap/wrap-reverse;</p>
      <p>flex-flow: flex-direction과 flex-warp을 한번에 적용</p>
      <pre>flex-flow: row wrap;</pre>
      <h3>정렬하기</h3>
      <p>justify-content: flex-start/flex-end/center/space-between/space-around/space-evenly</p>
      <p>align-items: stretch/flex-start/flex-end/center/baseline;</p>
      <h3>flex-grow, flex-shrink는 item에 적용</h3>
      
      <h2>Grid</h2>
      <pre>{`display: grid; 
      grid-template-columns: 1fr 2fr 3fr; // column 기준으로 배열, 넘어가면 순서대로 적용됨
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: 2fr 1fr;      `}</pre>
      <div className="wrapper">
        <div className="one grid_item">One</div>
        <div className="two grid_item">Two</div>
        <div className="three grid_item">Three</div>
        <div className="four grid_item">Four</div>
        <div className="five grid_item">Five</div>
        <div className="six grid_item">Six</div>
      </div>
      <pre>{`.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  grid-auto-rows: minmax(50px, auto);
}
.one {  grid-column: 1 / 3;  grid-row: 1; }
.two {  grid-column: 2 / 4;  grid-row: 1 / 3; }
.three {  grid-column: 1;  grid-row: 2 / 5; }
.four {  grid-column: 3;  grid-row: 3; }
.five {  grid-column: 2;  grid-row: 4; }
.six {  grid-column: 3;  grid-row: 4; `}</pre>
      <h4>grid로 가운데 정렬하기</h4>
      <p>이 속성은 align-items: center; (수직 중앙 정렬)와 justify-items: center; (수평 중앙 정렬)를 동시에 설정하는 단축 속성</p>
      <pre>{`.items__length {
  display: grid;
  place-items: center;
}`}</pre>
    </>
  )
}

export default CssAlignElements
