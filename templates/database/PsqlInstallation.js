import React from 'react'

function PsqlInstallation() {
  return (
    <div>
      <div id='psql-installation' className="for-space"></div>
      <h1>Install PostgreSQL</h1>
      <h3>download and install </h3>
      <pre>{`RHEL 8 INSTALL
  # yum module install postgresql:16/server
  # postgresql-setup --initdb
    * Initializing database in '/var/lib/pgsql/data'
    * Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log
  # systemctl start postgresql.service
  # systemctl enable postgresql.service
  postgres=# CREATE USER mydbuser WITH PASSWORD 'mypasswd' CREATEROLE CREATEDB;`}    </pre>
      <h3>PostgreSQL 데이터베이스 초기화, 생성 및 연결</h3>
      <h5>이 예제에서는 PostgreSQL 데이터베이스를 초기화하고, 일상적인 데이터베이스 관리 권한이 있는 데이터베이스 사용자를 생성하고, 
        관리 권한이 있는 데이터베이스 사용자를 통해 모든 시스템 계정에서 액세스할 수 있는 데이터베이스를 생성하는 방법을 보여줍니다.</h5>
      <h4>PosgreSQL 서버를 설치합니다.</h4> 
      <pre># yum module install postgresql:13/server</pre>
      <h4>  데이터베이스 클러스터를 초기화합니다.</h4>
      <pre> # postgresql-setup --initdb<br/>
          * Initializing database in '/var/lib/pgsql/data'<br/>
          * Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log  </pre>
      <h4>암호 해시 알고리즘을 scram-sha-256 으로 설정합니다.</h4>
      <pre>/var/lib/pgsql/data/postgresql.conf 파일에서 다음 행을 변경합니다.<br/>
        #password_encryption = md5              # md5 or scram-sha-256<br/>
        다음으로 변경합니다.<br/>
        password_encryption = scram-sha-256<br/>
        /var/lib/pgsql/data/pg_hba.conf 파일에서 IPv4 로컬 연결에 대해 다음 행을 변경합니다.<br/>
        host    all             all             127.0.0.1/32            ident<br/>
        다음으로 변경합니다.<br/>
        host    all             all             127.0.0.1/32            scram-sha-256 </pre>
      <h4>postgresql 서비스를 시작합니다.</h4>
      <pre> # systemctl start postgresql.service</pre>
      <h4>  postgres 라는 시스템 사용자로 로그인합니다.</h4>
      <pre> # su - postgres<br/>
        PostgreSQL 대화형 터미널을 시작합니다.<br/>
          $ psql<br/>
          psql (13.7)<br/>
          Type "help" for help.<br/>
          postgres=#<br/>
      선택 사항: 현재 데이터베이스 연결에 대한 정보를 얻습니다.<br/>
      postgres=# \conninfo </pre>
      <h4>mydbuser 라는 사용자를 만들고, mydbuser 의 암호를 설정한 다음 
      mydbuser 에게 CREATEROLE 및 CREATEDB 권한을 할당합니다.</h4>
      <pre>postgres=# CREATE USER mydbuser WITH PASSWORD 'mypasswd' CREATEROLE CREATEDB;<br/>
        CREATE ROLE<br/>
        이제 mydbuser 사용자가 일상적인 데이터베이스 관리 작업을 수행할 수 있습니다:<br/>
         데이터베이스를 생성하고 사용자 인덱스를 관리합니다.<br/>
        \q meta 명령을 사용하여 대화형 터미널에서 로그아웃합니다.<br/>
          postgres=# \q<br/>
        postgres 사용자 세션에서 로그아웃합니다.<br/>
          $ logout<br/>   </pre>
      <h4>PostgreSQL 터미널에 mydbuser 로 로그인하고 호스트 이름을 지정하고 
        초기화 중에 생성된 기본 postgres 데이터베이스에 연결합니다.</h4>
      <pre>{`# psql -U mydbuser -h 127.0.0.1 -d postgres -p 5432
  cmd => psql -U postgres -d mydb -h localhost -p 5432
  Password for user mydbuser:
  Type the password.
    psql (13.7)
    Type "help" for help.
  postgres=>`}  </pre>
    <h4>mydatabase 데이터베이스를 생성합니다.</h4>
    <pre>{`postgres=> CREATE DATABASE mydatabase;
  CREATE DATABASE
  postgres=>

세션에서 로그아웃합니다.
  postgres=# \q`} </pre> 
    <h4>mydatabase에 mydbuser 로 연결합니다.</h4>
    <pre>{`# psql -U mydbuser -h 127.0.0.1 -d mydatabase
  Password for user mydbuser:
  psql (13.7)
  Type "help" for help.
  mydatabase=>

선택 사항: 현재 데이터베이스 연결에 대한 정보를 얻습니다.

mydatabase=> \conninfo
You are connected to database "mydatabase" as user`}</pre>
    <h3>basic command</h3>
    <pre> # check version<br/>
      psql --version<br/>        
      # connect to database<br/>
      psql -h localhost -U postgres<br/>        
      # create database<br/>
      CREATE DATABASE db_name;<br/>        
      # create user<br/>
      CREATE USER user_name WITH PASSWORD 'password';<br/>        
      # grant all privileges on database to user<br/>
      GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;<br/>        
      # list all databases<br/>
      \l<br/>
      # list all tables in current database<br/>
      \dt<br/>        
      # list all columns in a table<br/>
      \d table_name<br/>
      # windows에서 psql 접속시<br/>
      SQL shell(psql) 실행      </pre>
    <h3>rhel8에 설치하고 원격접근하기</h3>
  <p>RHEL(Red Hat Enterprise Linux)에서 PostgreSQL에 원격 접속하려면, 
    서버 측 설정과 클라이언트 측 설정이 필요합니다. <br/>
  서버 측에서는 postgresql.conf 파일에서 listen_addresses 설정이 *로 되어 있는지 확인하고, 
  pg_hba.conf 파일에서 클라이언트 접속을 허용하도록 설정해야 합니다. 
  클라이언트 측에서는 psql 또는 pgAdmin과 같은 클라이언트 도구를 사용하여 서버에 접속해야 합니다. <br/>
  서버 측 설정: /var/lib/pgsql/data</p>
    <h5>1. postgresql.conf 수정:</h5>
    <p> listen_addresses 설정을 * 로 변경하여 모든 IP 주소에서 접속을 허용합니다.<br/>
  예시: listen_addresses = '*' </p>
    <h5>2. pg_hba.conf 수정:</h5>
    <p>클라이언트의 IP 주소, 네트워크 또는 사용자별로 접속을 허용하도록 설정합니다.<br/>
    예시: host all all 192.168.1.0/24 trust (192.168.1.0/24 네트워크의 모든 사용자를 인증 없이 허용)</p>
    <h5>3. PostgreSQL 서비스 재시작:</h5>
    <p>sudo systemctl restart postgresql 명령어를 사용하여 변경 사항을 적용합니다. <br/>
클라이언트 측 설정:</p>
    <h5>1. psql 명령어 사용:</h5>
    <p>psql -h {`<서버 IP 주소> -p <포트 번호> -U <사용자 이름> -d <데이터베이스 이름>`} 명령어를 사용하여 접속합니다.<br/>
    예시: psql -h 192.168.1.10 -p 5432 -U postgres -d mydatabase</p>
    <h5>2. pgAdmin 사용:</h5>
    <p>pgAdmin에서 서버 연결 설정을 추가하고, 위에서 설정한 정보들을 입력하여 접속합니다. <br/>
    주의 사항:<br/>
    pg_hba.conf 파일에서 인증 설정을 신중하게 설정해야 합니다. <br/>
    필요에 따라 비밀번호 인증을 사용하거나 특정 IP 주소만 허용하도록 설정하는 것이 좋습니다. <br/>
방화벽 설정도 확인하여 PostgreSQL 포트(기본값 5432)가 열려있는지 확인해야 합니다.</p>

    <div id='psql-data-type' className="for-space"></div>
    <h1>psql data type</h1>
    <table style={{borderCollapse:'collapse'}}>
      <tr>
        <td>Name</td> <td>Aliases</td> <td>Description</td>
      </tr>
      <tr>
        <td>bigint</td> <td>int8</td> <td>signed eight-byte integer</td>
      </tr>
      <tr>
        <td>bigserial</td> <td>serial8</td> <td>autoincrementing eight-byte integer</td>
      </tr>
      <tr>
        <td>bit [ (n ) ]</td> <td></td>  <td>fixed-length bit string</td>
      </tr>
      <tr>
        <td>bit varying [ (n) ]</td> <td>varbit [ (n) ]</td>
        <td>variable-length bit string</td>
      </tr>
      <tr>
        <td>boolean</td>  <td>bool</td>  <td>logical Boolean (true/false)</td>
      </tr>
      <tr>
        <td>box</td>  <td></td>  <td>rectangular box on a plane</td>
      </tr>
      <tr>
        <td>bytea</td>  <td></td>  <td>binary data (byte array)</td>
      </tr>
      <tr>
        <td>character [ (n) ]</td> <td>char [ (n) ]</td> <td>fixed-length character string</td>
      </tr>
      <tr>
        <td>character varying [ (n) ]</td> <td>varchar [ (n ) ]</td> 
        <td>variable-length character string</td>
      </tr>
      <tr>
        <td>cidr</td> <td></td> <td>IPv4 or IPv6 network address</td>
      </tr>
      <tr>
        <td>circle</td> <td></td> <td>circle on a plane</td>
      </tr>
      <tr>
        <td>date</td> <td></td> <td>calendar date (year, month, day)</td>
      </tr>
      <tr>
        <td>double precision</td> <td>float8</td>
        <td>double precision floating-point number (8 bytes)</td>
      </tr>
      <tr>
        <td>inet</td> <td></td> <td>IPv4 or IPv6 host address</td>
      </tr>
      <tr>
        <td>integer</td> <td>int class="font013574">, int4</td>
        <td>signed four-byte integer</td>
      </tr>
      <tr>
        <td>interval [ fields ] [ (p ) ]</td> <td></td> <td>time span</td>
      </tr>
      <tr>
        <td>json</td> <td></td> <td>textual JSON data</td>
      </tr>
      <tr>
        <td>jsonb</td> <td></td> <td>binary JSON data, decomposed</td>
      </tr>
      <tr>
        <td>line</td> <td></td> <td>infinite line on a plane</td>
      </tr>
      <tr>
        <td>lseg</td> <td></td> <td>line segment on a plane</td>
      </tr>
      <tr>
        <td>macaddr</td> <td></td> <td>MAC (Media Access Control) address</td>
      </tr>
      <tr>
        <td>macaddr8</td> <td></td>
        <td>MAC (Media Access Control) address (EUI-64 format)</td>
      </tr>
      <tr>
        <td>money</td> <td></td> <td>currency amount</td>
      </tr>
      <tr>
        <td>numeric [ (p, s) ]</td> <td>decimal [ (p , s ) ]</td>
        <td>exact numeric of selectable precision</td>
      </tr>
      <tr>
        <td>path</td> <td></td> <td>geometric path on a plane</td>
      </tr>
      <tr>
        <td>pg_lsn</td> <td></td> <td>PostgreSQL Log Sequence Number</td>
      </tr>
      <tr>
        <td>pg_snapshot</td> <td></td>
        <td>user-level transaction ID snapshot</td>
      </tr>
      <tr>
        <td>point</td> <td></td>
        <td>geometric point on a plane</td>
      </tr>
      <tr>
        <td>polygon</td> <td></td>
        <td>closed geometric path on a plane</td>
      </tr>
      <tr>
        <td>real</td> <td>float4</td>
        <td>single precision floating-point number (4 bytes)</td>
      </tr>
      <tr>
        <td>smallint</td> <td>int2</td>
        <td>signed two-byte integer</td>
      </tr>
      <tr>
        <td>smallserial</td> <td>serial2</td>
        <td>autoincrementing two-byte integer</td>
      </tr>
      <tr>
        <td>serial</td> <td>serial4</td>
        <td>autoincrementing four-byte integer</td>
      </tr>
      <tr>
        <td>text</td> <td></td>
        <td>variable-length character string</td>
      </tr>
      <tr>
        <td>time [ (p ) ] [ without time zone ]</td> <td></td>
        <td>time of day (no time zone)</td>
      </tr>
      <tr>
        <td>time [ (p ) ] with time zone</td> <td>timetz</td>
        <td>time of day, including time zone</td>
      </tr>
      <tr>
        <td>timestamp [ (p ) ] [ without time zone ]</td> <td></td>
        <td>date and time (no time zone)</td>
      </tr>
      <tr>
        <td>timestamp [ (p ) ] with time zone</td> <td>timestamptz</td>
        <td>date and time, including time zone</td>
      </tr>
      <tr>
        <td>tsquery</td> <td></td> <td>text search query</td>
      </tr>
      <tr>
        <td>tsvector</td> <td></td> <td>text search document</td>
      </tr>
      <tr>
        <td>txid_snapshot</td> <td></td>
        <td>user-level transaction ID snapshot (deprecated; see pg_snapshot)</td>
      </tr>
      <tr>
        <td>uuid</td> <td></td> <td>universally unique identifier</td>
      </tr>
      <tr>
        <td>xml</td> <td></td> <td>XML data</td>
      </tr>
    </table>
    </div>
  )
}

export default PsqlInstallation
