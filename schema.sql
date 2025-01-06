/*

    Esse seria um schema inicial para rodar essa aplicação. Nele temos as informações
    necessárias para operar a aplicação controlando os estados e as ações do agente.

*/

CREATE TABLE conversation (
    id SERIAL PRIMARY KEY,
    sender VARCHAR(5) NOT NULL,        -- agent | user
    message TEXT NOT NULL,
    phone_number VARCHAR(20),
    name VARCHAR(100),
    current_state VARCHAR(100),
    lookahead_state VARCHAR(100),

    -- a partir daqui, campos opcionais
    memory_recover JSON,
    memory_saving JSON,
    follow_up_task VARCHAR(255),
    next_follow_up_message TEXT,
    document_needed BOOLEAN DEFAULT FALSE,
    document_needed_name VARCHAR(255),
    likely_predictor_variable VARCHAR(255),
    likely_outcome_variable VARCHAR(255),
    api_call_required BOOLEAN DEFAULT FALSE,
    human_routing_needed BOOLEAN DEFAULT FALSE,
    outlier_to_observe BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
