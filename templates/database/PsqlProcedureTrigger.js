import React from 'react'

function PsqlProcedureTrigger() {
  return (
    <div>
      <div id='psql-procedure-trigger' className="for-space"></div>
      <h1>STORED PROCEDURE</h1>
      <h3>STORED PROCEDURE: 자주 쓰는 SQL을 함수로 저장</h3>
      <pre>
      DELIMITER $$ -- delimiter 를 $$ 임시로 변경 procedure에서 ;를 쓸 수 있도록 함<br/>
      CREATE PROCEDURE procedure_name ()<br/>
      BEGIN<br/>
          -- SQL statements<br/>
          SELECT * FROM table_name;<br/>
          -- Other SQL statements<br/>
      END $$<br/>
      DELIMITER ; -- 다시 delimiter를 ;로 변경<br/>
      -- 프로시저 호출<br/>
      CALL procedure_name('value1', @output);</pre>
      <pre>
      -- 프로시저에 OUT 파라미터가 있는 경우, @output 변수에 결과를 저장함<br/>
      DELIMITER $$<br/>
      CREATE PROCEDURE procedure_name (IN param1 datatype, OUT param2 datatype)<br/>
      BEGIN<br/>
        SELECT * FROM table_name WHERE column_name = param1;<br/>
        SET param2 = (SELECT COUNT(*) FROM table_name WHERE column_name = param1);<br/>
      END $$<br/>
      DELIMITER ;<br/>
      CALL procedure_name('value1', @output);<br/>
      -- --------------------------------------<br/>
      DELIMITER $$<br/>
      CREATE PROCEDURE find_customer (IN id INT)<br/>
      BEGIN<br/>
        SELECT * FROM customers WHERE customer_id = id;<br/>
      END $$<br/>
      DELIMITER ;<br/>
      CALL find_customer(1); -- 프로시저 호출<br/>
      -- --------------------------------------<br/>
      DELIMITER $$<br/>
      CREATE PROCEDURE find_customer_full_name (IN f_name VARCHAR(50), IN l_name VARCHAR(50))<br/>
      BEGIN<br/>
        SELECT * FROM customers where first_name = f_name AND last_name = l_name;<br/>
      END $$<br/>
      DELIMITER ;<br/>
      CALL find_customer_full_name("abc", "cde"); -- 프로시저 호출<br/>

      DROP PROCEDURE IF EXISTS procedure_name; -- 프로시저 삭제<br/>
      </pre>
      {/* <!--*********** TRIGGERS ******************--> */}
      <h1>TRIGGERS</h1>
      <h3>뭔가를 한 후에 수행할 주로 업데이트할 내용을 정의</h3>
      <pre>
      SHOW TRIGGERS; -- 트리거 목록 보기<br/>
      DROP TRIGGER IF EXISTS trigger_name; -- 트리거 삭제<br/>
      -- ########## 트리거 생성 #############<br/>
      CREATE TRIGGER trigger_name<br/>
      BEFORE|AFTER INSERT|UPDATE|DELETE ON table_name<br/>
      FOR EACH ROW<br/>
      BEGIN<br/>
        INSERT INTO log_table (action, action_time) VALUES ('insert', NOW());<br/>
      END;  </pre>
      <pre>--exercise<br/>
        ALTER TABLE employees<br/>
        ADD COLUMN salary DECIMAL(10, 2) NOT NULL DEFAULT 0.00<br/>
        AFTER hourly_pay;<br/>
        UPDATE employees<br/>
        SET salary = hourly_pay * 40 * 4; -- 월급으로 변환<br/>
        -- ########## 트리거 생성 hourly_pay가 변경되면 salary도 변경되도록 함<br/>
        CREATE TRIGGER before_hourly_pay_update<br/>
        BEFORE UPDATE ON employees<br/>
        FOR EACH ROW<br/>
          SET NEW.salary = NEW.hourly_pay * 40 * 4; -- 월급으로 변환<br/>
        -- ########## 트리거 생성 hourly_pay가 변경되면 salary도 변경되도록 함    <br/>
        CREATE TRIGGER before_hourly_pay_insert<br/>
        BEFORE INSERT ON employees<br/>
        FOR EACH ROW<br/>
          SET NEW.salary = NEW.hourly_pay * 40 * 4; -- 월급으로 변환<br/>

        insert into employees values(29, "신입","직원", "worker", 18, null, DATE(NOW()), 3);
      </pre>
      <h3>예제</h3>
      <pre>
      CREATE TABLE IF NOT EXISTS expenses (<br/>
        id INT AUTO_INCREMENT PRIMARY KEY,<br/>
        expense_name varchar(20),<br/>
        expense_total INT<br/>
      );<br/>
      UPDATE expenses <br/>
        SET expense_total = (SELECT SUM(salary) FROM employees) <br/>
        WHERE expense_name = "salaries";<br/>
      -- ########## 행이 추가허면 업데이트 하는 트리거<br/>
      CREATE TRIGGER after_salary_insert_expense_total<br/>
      AFTER INSERT ON employees<br/>
      FOR EACH ROW<br/>
        UPDATE expenses<br/> 
        SET expense_total = expense_total + NEW.salary <br/>
        WHERE expense_name = "salaries";<br/>

      -- ########## 행이 삭제하면 업데이트 하는 트리거 생성<br/>
      CREATE TRIGGER after_salary_delete_expense_total<br/>
      AFTER DELETE ON employees -- BEFORE로 하면 삭제된 행이 없어서 에러 발생<br/>
      FOR EACH ROW<br/>
        UPDATE expenses<br/> 
        SET expense_total = expense_total - OLD.salary -- OLD.salary는 삭제되는 행의 salary<br/>
        WHERE expense_name = "salaries";<br/>

      -- --------------------------------------<br/>
      -- update해서 값이 변경되었을 때  <br/>
      CREATE TRIGGER after_salary_update_expense_total<br/>
      AFTER UPDATE ON employees -- BEFORE로 하면 삭제된 행이 없어서 에러 발생<br/>
      FOR EACH ROW<br/>
        UPDATE expenses<br/> 
        SET expense_total = expense_total + (NEW.salary - OLD.salary) -- 새로운 값에서 이전 값을 뺌<br/>
        WHERE expense_name = "salaries"; </pre>
    </div>
  )
}

export default PsqlProcedureTrigger
