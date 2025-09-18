import React from 'react'

function PsqlInstallation() {
  return (
    <div>
      <div id='psql-CRUD' className="for-space"></div>
      <h1>PostgreSQL Basic</h1>
      <h3>CREATE USER</h3>
      <pre>CREATE USER user_name WITH PASSWORD 'password' CREATEROLE CREATEDB;</pre>
      <h3>원격 접속; -d database name</h3>
      <pre># psql -U mydbuser -h 127.0.0.1 -d postgres</pre>
      <h3>CREATE DATABASE</h3>
      <pre>=# CREATE DATABASE database_name;</pre>
      <h4>DROP TATABSE</h4>
      <pre>=# DROP DATABASE database_name;</pre>
      <h4>db connect</h4>
      <pre>=# \c database_name</pre>
      <h3>CREATE TABLE</h3>
      <p>SERIAL : auto increment, BIGSERIAL</p>
      <pre>=# CREATE TABLE person (<br/>
          id SERIAL PRIMARY KEY NOT NULL,<br/>
          name VARCHAR(100) NOT NULL,<br/>
          age INT NOT NULL,<br/>
          address VARCHAR(255) NOT NULL,<br/>
          created_at TIMESTAMP );</pre>
      <h4>DROM TABLE</h4>
      <pre>=# DROP TABLE person;</pre>

      <h3>INSERT</h3>
      <pre>=# INSERT INTO person (name, age, address, created_at)<br/>
          VALUES ('John Doe', 30, '123 Main St', NOW()),<br/>
          ('John Doe', 30, '123 Main St', '2019-02-22');</pre>
      <h4>Import data from file : https://www.mockaroo.com/</h4>
      <pre>=# \copy person FROM '/path/to/file.csv' DELIMITER ',' CSV HEADER;<br/>
    =# \i '/path/to/file.sql';</pre>

    {/* <!-- ######### UPDATE table_name SET ########--> */}
      <h3>UPDATE</h3>
        <pre>UPDATE table_name<br/>
          SET column1 = value1, column2 = value2, ...<br/>
          WHERE condition;</pre>
        <pre>UPDATE customer<br/>
          SET name = '김관용', country = '한국', address = '대전시 서구'<br/>
          WHERE id = 2;</pre>
      {/* <!-- ############## DELETE FROM ################--> */}
      <h3>DELETE</h3>
        <pre>DELETE FROM table_name WHERE condition;</pre>
        <pre>DELETE FROM customer<br/>
        WHERE email LIKE 'malebrooke6@%';<br/>
      DELETE FROM car<br/>
        WHERE price = null;</pre>
      {/* <!-- ######### on delete: foreign key가 있을 때 ############-->   */}
      <h4>ON DELETE SET NULL ; FOREIGN KEY가 지워지면 이를 참조하는 테이블의 값을 NULL로 함</h4>
      <pre>alter table employees drop constraint FK_Office_id;<br/>
      ALTER TABLE employees ADD FOREIGN(office_id) <br/>
      -- 부모 테이블에서 삭제시 자식 테이블의 값을 NULL로 함<br/>
        REFERENCES offices(office_id) ON DELETE SET NULL; <br/>
      -- OR<br/>
      ALTER TABLE table_name<br/>
        ADD CONSTRAINT constraint_name -- 제약조건 이름(같은 이름)<br/>
        FOREIGN KEY (column_name)<br/>
        REFERENCES parent_table (parent_column)<br/>
        ON DELETE CASCADE; -- 부모 테이블에서 삭제시 자식 테이블도 삭제<br/>
        -- 부모 테이블에서 삭제시 자식 테이블의 값을 NULL로 함<br/>
      --OR,  ON DELETE NULL; 
      </pre>
      <pre>ALTER TABLE employees <br/>
        ADD CONSTRAINT fk_employees_office_id <br/>
        FOREIGN KEY(office_id) REFERENCES offices(office_id) ON DELETE CASCADE;</pre>
      <h4>ON DELETE SET CASCADE ; FOREIGN KEY가 지워지면 이를 참조하는 테이블의 ROW를 지움</h4>
      {/* <!-- ######### TABLE 구조는 남기고 데이터만 지움 ###########-->   */}
      <h3>TRUNCATE</h3>  
        <pre>TRUNCATE TABLE table_name;</pre>
        <pre>TRUNCATE TABLE customer;</pre>
      {/* <!-- ########### 테이블 삭제 drop ###############--> */}
      <h3>delete table</h3>
        <pre>DROP TABLE table_name;</pre>
      {/* <!-- ########## COLUNM 위치이동 #################--> */}
      <h3>column 위치 이동</h3>
        <pre>ALTER TABLE t_name MODIFY COLUMN age INT AFTER last_name;</pre>
      {/* <!-- ############## VIEW ###################--> */}
      <h1>VIEW</h1>
      <h3>기존 테이블을 바탕으로 새로운 가상의 테이블을 생성(자동업데이트)</h3>
        <pre>CREATE VIEW view_name AS<br/>
      SELECT column1, column2, ...<br/>
      FROM table_name<br/>
      WHERE condition;</pre>
      <pre>CREATE VIES em_office AS <br/>
        SELECT first_name, offices.address FROM employees <br/>
        LEFT JOIN offices ON employees.office_id = offices.office_id;<br/>
      SELECT * FROM em_office;</pre>
      <pre>-- 다룰 때는 일반 테이블 다루듯이 하면됨<br/>
      SELECT * FROM view_name;<br/>
      DROP VIEW view_name;<br/>
      ALTER VIEW view_name AS SELECT ...; -- 기존 뷰를 변경<br/>
      CREATE OR REPLACE VIEW view_name AS SELECT ...; -- 기존 뷰를 변경</pre>
    </div>
  )
}

export default PsqlInstallation
