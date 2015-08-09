sudo -u postgres psql postgres
CREATE DATABASE ffxi_gamify;
CREATE USER ffxi_gamify WITH PASSWORD 'ffxi_gamify';
GRANT ALL PRIVILEGES ON DATABASE ffxi_gamify to ffxi_gamify;
\q
