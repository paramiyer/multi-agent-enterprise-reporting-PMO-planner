# Complex PMO Visualization with Multi-Agent AI Planning

This Jupyter Notebook demonstrates a multi-agent AI-based orchestration system to generate enterprise-level KPI dashboard delivery scenarios.

## Project Overview
The notebook uses a structured prompt-based multi-agent setup to estimate and plan:
- KPI definition and stakeholder analysis
- UX design planning
- Dashboard development
- Data engineering and ETL design
- QA and UAT effort estimation
- Final deployment and user training
- Consolidation of all efforts into 4 delivery scenarios (A, B, C1, C2)

## Features
- Uses openAI agents defined using `crewai` to simulate tech leads from each function
- Each agent outputs scoped estimates and timelines
- A `resource_estimator_agent` aggregates the results and creates optimized delivery scenarios
- External validation checks ensure cost/duration sanity

## 🔧 Configuration Guide: How to Customize This Notebook

You can adapt this multi-agent project planner for other enterprise reporting initiatives by modifying the following components:

### 1. `agents.yaml`
- **Purpose**: Defines each agent’s role, goal, and backstory (e.g., UX Designer, QA Lead, Data Engineer).
- **What to Change**:  
  Update `role`, `goal`, and `backstory` to match your specific team setup or delivery expectations.
- **Where to Find in Notebook**:  
  Look for the cell where the variable `agents_file` is loaded or referenced.

---

### 2. `tasks.yaml`
- **Purpose**: Describes the specific task each agent should perform or estimate (e.g., design dashboards, run QA).
- **What to Change**:  
  Modify the `description` and `expected_output` fields per role or delivery workflow.
- **Where to Find in Notebook**:  
  Look for the variable `tasks_file` or function calls involving task parsing.

---

### 3. Project Requirements
- **Purpose**: Sets the business context for the planning activity (e.g., number of dashboards, complexity, cost structure).
- **What to Change**:  
  - Number of dashboards  
  - Complexity tiers (low, medium, high)  
  - Cost structure (weekly FTE rates per role)  
  - Phase constraints and stakeholder checkpoints
- **Where to Find in Notebook**:  
  Typically defined in a variable like `context_dict` or `project_requirements` near the start of the notebook.

---

### 4. 📊 Final Results
- **Location in Notebook**:  
  Scroll down to the section titled `## Generate and Visualize All Scenarios`.
- **What You’ll See**:
  - Project duration (per scenario)
  - FTEs by role
  - Cost estimations
  - Milestone plans and stakeholder checkpoints
  - Gantt charts as Markdown tables
  - GPT-based critique and validation output (with score and insights)

Use this notebook to simulate project planning with AI, validate results, and iterate delivery plans—before any high-cost execution begins!

## Running the Notebook
This notebook assumes access to OpenAI's GPT models and a prompt-based planning structure. Ensure the following:
- API access with relevant cost structures configured
- YAML task and agent specifications for grounding
- All domain agent prompts and validation logic set up in the notebook

## Output Examples
- Scenario tables with cost and timelines
- Gantt charts in Markdown
- Function-level validation scores and critique summaries

## Future Improvements
- Integrate historical cost benchmarking
- Add domain-specific dataset for better estimates
- Convert into a Streamlit Copilot or Copilot Plugin

## Author
- Param Iyer
- Inspired by: deeplearning.ai’s Copilot project

## License
MIT License (or your preferred license)
