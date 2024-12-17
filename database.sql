
CREATE TABLE IF NOT EXISTS assistants (
    name TEXT PRIMARY KEY,
    instructions TEXT,
    functions TEXT,
    code TEXT
);
