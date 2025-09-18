import React from 'react'

function PsqlDbTable() {
  return (
    <div>
      <div id='psql-db-table' className="for-space"></div>
      <h1>DATABASE </h1>  
      <h4>CREATE DATABASE database_name;</h4>
      <h5>읽기 전용으로 만들기: DB 삭제, 테이블 변경등 안됨</h5>
      <pre>ALTER DATABASE db_name READ ONLY = 1;<br/>
      ALTER DATABASE db_name READ ONLY = 0; // read only 제거</pre>
      <h4>import file</h4>
      <pre>-- 따움표 없음<br/>
  source /path/to/file.sql; <br/>
  USE DATABASES db_name; OR \u db_name</pre>

      <h5>DROP DATABASE database_name;</h5>
      <h5>BACKUP DATABASE database_name TO DISK ='filepath';</h5>
      <h5>RESTORE DATABASE database_name FROM DISK ='filepath';</h5>
      <h5>BACKUP DATABASE databasename TO DISK = 'filepath' WITH DIFFERENTIAL;</h5>

{/* ==================== table 관련 ===========================*/}
      <h1>TABLE 생성,삭제 등</h1>
      <h4>CREATE TABLE table_name(column1 datatype, column2 datatype,...)</h4>
      <pre>create table customer (<br/>
  customerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,<br/>
  name VARCHAR(100) NOT NULL,<br/>
  address VARCHAR(150),<br/>
  country VARCHAR(50) NOT NULL,<br/>
  PostalCode VARCHAR(150) NOT NULL,<br/>
  birthday DATE DEFAULT (CURRENT_DATE)<br/>
);<br/>
insert into customer (name, email, address, country, city, PostalCode) <br/>
values ('Shara Bohman', null, 'PO DRAWER 789', 'Honduras', 'Santa Lucía', null); </pre>

      <h4>import json: mysqlsh mode에서</h4>
      <pre>{`-- type을 json으로 지정하고,
-- 테이블을 생성한 후에 json 파일을 import
  \\sql
  CREATE TABLE car_json (
    id SERIAL NOT NULL PRIMARY KEY, car_info JSON NOT NULL);
  \\js
   -- 경로는 본인에 맞게 수정 '/로 해야함'
  util.importJson('C:/Users/slow3/Downloads/car.json',
    { schema: 'mydb', table:'car_json', tableColumn: 'car_info' } );
  json data format은 [] 없고, 끝에 ","도 없어야함
    {"id":1,"make":"Honda","model":"CR-Z","model_year":2011}
    {"id":2,"make":"Lincoln","model":"Town Car","model_year":1988}
    {"id":3,"make":"Scion","model":"iQ","model_year":2012}
    ...
  \sql select * from car_json\G    -- 여기서 ";" 없어야 함
  select * from car_json\G;    -- 여기서는 ";" 있어야 함`}</pre>

      <h3>CREATE TABLE : 다른 테이블을 이용해서 생성</h3>
      <pre>CREATE TABLE new_table_name AS<br/>
  SELECT column1, column2,...<br/>
  FROM existing_table_name<br/>
  WHERE ....; </pre>
        
    <pre>CREATE TABLE TestTable AS<br/>
  SELECT customername, contactname FROM customers; </pre>
      <h3>import json file : mysqlsh --js mode에서 실행</h3>
      <h3>DROP TABLE table_name;</h3>
      <h3>TRUNCATE TABLE table_name;</h3>
      <h4>데이터만 지우고 테이블을 그대로 둠</h4>

      <h3>RENAME TABLE</h3>
    <pre>ALTER TABLE old_table_name RENAME TO new_table_name;<br/>
  ALTER TABLE Customers RENAME TO Customers_NEW;</pre>

      <h2>ALTER TABLE</h2>
      <h3>ADD COLUMN</h3>
      <pre>ALTER TABLE table_name ADD column_name datatype;<br/>
    ALTER TABLE Customers ADD Email varchar(255);</pre>

      <h3>DROP COLUMN</h3>
      <pre>ALTER TABLE table_name DROP COLUMN column_name; <br/>
    ALTER TABLE Customers DROP COLUMN Email;</pre>

      <h3>RENAME COLUMN</h3>
      <pre>ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;<br/>
  ALTER TABLE Customers RENAME COLUMN Email TO EmailAddress;</pre>

      <h3>MODIFY COLUMN</h3>
      <pre>ALTER TABLE table_name MODIFY COLUMN column_name datatype;<br/>
    ALTER TABLE Customers MODIFY COLUMN Email varchar(100);<br/>
    ALTER TABLE Customers ALTER COLUMN Email varchar(100);</pre>

      <h3>COLUMN 위치변경</h3>
      <pre>-- email 위치를 last_name 뒤로 이동<br/>
  ALTER TABLE table_name MODIFY email AFTER last_name;<br/>
  ALTER TABLE table_name MODIFY email FIRST;</pre>
    </div>
  )
}

export default PsqlDbTable
