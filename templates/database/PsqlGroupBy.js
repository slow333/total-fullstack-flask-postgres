import React from 'react'

function PsqlGroupBy() {
return (
<div>
  <div id='psql-group-by' className="for-space"></div>
  <h1>GROUP BY AND HAVING</h1>
  <h4>group by는 aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) 과 합께 사용</h4>
  <pre>SELECT column_name(s) FROM table_name<br/>
    WHERE condition<br/>
    GROUP BY column_name(s) ORDER BY column_name(s); </pre>
    
  <h3>GROUP BY</h3>
  <pre>SELECT COUNT(id), country FROM customer<br/>
    GROUP BY country ORDER BY COUNT(id) DESC;</pre>
  <pre>SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders <br/>
    FROM Orders<br/>
    LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID<br/>
    GROUP BY ShipperName;</pre>
  <pre>-- 출고된 연도 별로 가격의 합<br/>
    -- COUNT, MAX, MIN, AVG 등도 사용 가능<br/>
  SELECT SUM(price), model_year FROM car GROUP BY model_year; <br/>
  SELECT SUM(price), customer_id FROM car GROUP BY customer_id; </pre>  

  <h3>HAVING</h3>
  <h4>group by 하면 where을 사용할 수 없어 HAVING 을 사용.</h4>
  <pre>SELECT column_name(s) FROM table_name<br/>
    WHERE condition<br/>
    GROUP BY column_name(s)<br/>
    HAVING condition ORDER BY column_name(s);</pre>
  <pre>SELECT COUNT(id), Country FROM Customer<br/>
    GROUP BY Country<br/>
    HAVING COUNT(id) &gt; 15;</pre>
  <pre>SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders<br/>
  FROM (Orders INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)<br/>
  GROUP BY LastName<br/>
  HAVING COUNT(Orders.OrderID) &gt; 10;</pre>
  <pre>SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders<br/>
  FROM Orders<br/>
  INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID<br/>
  WHERE LastName = 'Davolio' OR LastName = 'Fuller'<br/>
  GROUP BY LastName<br/>
  HAVING COUNT(Orders.OrderID) &gt; 25;</pre>
  <pre>SELECT COUNT(*) , model FROM car<br/>
    GROUP BY model <br/>
    HAVING COUNT(*) {`>`} 1 <br/>
    ORDER BY COUNT(*) DESC;</pre>

    {/* <!-- ############## distinct #########################--> */}
  <h3>SELECT DISTINCT; 중복제거</h3>
    <pre>SELECT DISTINCT column1, column2 FROM table_name;<br/>
  SELECT Count(DISTINCT column1) FROM table_name;</pre>
  <pre>SELECT country, COUNT(DISTINCT city) FROM customers<br/>
    GROUP BY country; -- 중복되지 않는 CITY의 개수를 샘</pre>

  <h3>중복된 모델을 가진 자동차를 삭제</h3>
  <pre>DELETE c1<br/>
    FROM car c1<br/>
    JOIN car c2<br/>
    ON c1.model = c2.model<br/>
    WHERE c1.id &lt; c2.id;<br/>
    -- OR, WHERE c1.id &lt; (c2.id + 3); -- 3개만 남기기 </pre>
  <pre>-- 중복 제거 make, model, model_year 조합<br/>
  DELETE FROM car <br/>
  WHERE id NOT IN (SELECT MIN(id) FROM car GROUP BY make, model, model_year);</pre>

  <h3>ROLLUP : GROUP BY 이후에 다시 전체 내용을 더하는 방식 </h3>
  <pre>SELECT make, SUM(price) AS total_price FROM car  <br/>
  GROUP BY make WITH ROLLUP;<br/>
  SELECT make, COUNT(id) AS total_price FROM car  <br/>
  GROUP BY make WITH ROLLUP;  </pre>
</div>
)
}

export default PsqlGroupBy
