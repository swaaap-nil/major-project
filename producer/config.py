# DB_CONFIG = { "dbname":"postgres",
#             # "user":"postgres",
#             # "password":"postgres1",
#             # "host":"skill-db.ckcpmbhhbpgq.ap-south-1.rds.amazonaws.com",
#             "user":"root",
#             "password":"password@root",
#             "host":"localhost",
#             "port":5432,
#             "connect_timeout":30
#             }

# NEO4J_CONFIG = {
#     "uri": "neo4j://localhost:7687",
#     "user": "neo4j",
#     "password": "testpassword"
# }

import os
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "password@root"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "connect_timeout": int(os.getenv("DB_CONNECT_TIMEOUT", 30))
}

NEO4J_CONFIG = {
    "uri": os.getenv("NEO4J_URI", "neo4j://localhost:7687"),
    "user": os.getenv("NEO4J_USER", "neo4j"),
    "password": os.getenv("NEO4J_PASSWORD", "testpassword")
}

RABBIT_MQ_CONFIG = {
    "user": os.getenv("RABBIT_USER", "user@notification"),
    "password": os.getenv("RABBIT_PASSWORD", "password@notification"),
}
