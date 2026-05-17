from langgraph.graph import StateGraph, START, END

from agent.state import MaintenanceState
from agent.nodes import *
from agent.tools import *

workflow = StateGraph(MaintenanceState)

#Add named nodes of the graph and what function is executed at the node
workflow.add_node(
    "fetch_history",
    fetch_history_node
)

workflow.add_node(
    "fetch_explanations",
    fetch_explanation_node
)

workflow.add_node(
    "generate_diagnostic_summary",
    generate_diagnostic_summary_node
)

workflow.add_node(
    "generate_llm_report",
    generate_llm_report_node
)

#Add edges connecting the nodes
workflow.add_edge(
    START,
    "fetch_history"
)

workflow.add_edge(
    "fetch_history",
    "fetch_explanations"
)

workflow.add_edge(
    "fetch_explanations",
    "generate_diagnostic_summary"
)

workflow.add_edge(
    "generate_diagnostic_summary",
    "generate_llm_report"
)

workflow.add_edge(
    "generate_llm_report",
    END
)


#Compile the graph
app = workflow.compile()

#Generate initial state
test_df = get_payload()
engine_id = int(test_df.iloc[0]['engine_id'])
drop_columns = ['engine_id', 'cycle', 'RUL', 'failure_risk']
x_test = test_df.drop(columns=drop_columns)
sample_features = x_test.iloc[0].to_dict()

init_state = {
    "engine_id": engine_id,
    "prediction_payload":{
        "engine_id":engine_id,
        "features":sample_features
    }
}

#Execute graph
result = app.invoke(init_state)

#Print results
print(result["maintenance_report"])