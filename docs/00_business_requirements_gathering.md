# 00 — Business Requirements Gathering Plan

**Project:** Astrea Manufacturing — Manufacturing & Production Management ERP
**ERP Platform:** Odoo 19
**Document Type:** Business Analysis / Requirements Elicitation Plan
**Version:** 1.0
**Status:** Draft — Portfolio Case Study
**Prepared By:** Business Analyst / ERP Consultant

---

# 1. Document Purpose

This document defines the approach, methodology, stakeholders, activities, and deliverables required to gather and validate business requirements for the Astrea Manufacturing ERP implementation project.

The purpose of the requirements gathering process is to understand the company's existing manufacturing operations, identify operational challenges, define business needs, and establish the requirements that will guide the ERP implementation.

This document serves as the foundation for the Business Requirements Document (BRD).

## 1.1 Project Background

Astrea Manufacturing is a hypothetical industrial manufacturing company specializing in industrial water pumps and electric motors.

The company currently manages several operational activities, including:

- Product and component management.
- Procurement and supplier management.
- Inventory management.
- Manufacturing planning.
- Work order execution.
- Quality inspection.
- Maintenance management.
- Manufacturing cost monitoring.
- Production performance reporting.

The company intends to implement Odoo 19 to integrate these processes into a centralized ERP system.

## 1.2 Business Analysis Objectives

The requirements gathering process aims to:

1. Understand the existing business processes.
2. Identify operational inefficiencies and business challenges.
3. Identify stakeholders and their responsibilities.
4. Understand business rules and operational constraints.
5. Identify functional and non-functional requirements.
6. Define the expected future business processes.
7. Identify gaps between existing processes and the proposed ERP solution.
8. Establish measurable acceptance criteria.
9. Obtain stakeholder validation and approval.

---

# 2. Requirements Gathering Scope

## 2.1 In-Scope Business Areas

| Business Area          | Requirements Gathering Scope                      |
| ---------------------- | ------------------------------------------------- |
| Product Management     | Product master data and product categorization    |
| Bill of Materials      | Product structure and component requirements      |
| Procurement            | Purchasing and supplier management                |
| Inventory              | Stock movement, replenishment, and traceability   |
| Manufacturing Planning | Production planning and manufacturing orders      |
| Work Orders            | Production operations and work center management  |
| Quality Management     | Incoming, in-process, and final inspection        |
| Maintenance            | Equipment maintenance and preventive maintenance  |
| Manufacturing Costing  | Material, labor, and overhead cost                |
| Reporting              | Manufacturing and operational performance reports |

## 2.2 Out-of-Scope Areas

The initial implementation excludes:

- Advanced product lifecycle management.
- Advanced demand forecasting.
- Multi-company manufacturing operations.
- Complex subcontracting.
- Advanced warehouse automation.
- Machine-to-machine IoT integration.
- Custom production scheduling optimization.

These capabilities may be considered in future implementation phases.

---

# 3. Stakeholder Identification

Stakeholder identification determines who participates in requirements gathering and who has authority to validate or approve business requirements.

## 3.1 Stakeholder Register

| Stakeholder           | Department         | Role in Project       | Responsibility                                              |
| --------------------- | ------------------ | --------------------- | ----------------------------------------------------------- |
| Project Sponsor       | Management         | Executive Sponsor     | Defines strategic objectives and approves project direction |
| Project Manager       | Project Management | Project Lead          | Coordinates project activities and stakeholder engagement   |
| Business Analyst      | Business Analysis  | Requirements Lead     | Conducts elicitation, analysis, and documentation           |
| Production Manager    | Production         | Process Owner         | Defines manufacturing processes and production requirements |
| Production Supervisor | Production         | Subject Matter Expert | Explains daily production activities                        |
| Warehouse Manager     | Inventory          | Process Owner         | Defines inventory management requirements                   |
| Warehouse Staff       | Inventory          | End User              | Explains stock handling and warehouse activities            |
| Procurement Manager   | Procurement        | Process Owner         | Defines procurement requirements                            |
| Procurement Staff     | Procurement        | End User              | Explains purchasing activities                              |
| Quality Manager       | Quality            | Process Owner         | Defines inspection and quality requirements                 |
| Maintenance Manager   | Maintenance        | Process Owner         | Defines equipment maintenance requirements                  |
| Finance Manager       | Finance            | Process Owner         | Defines costing and financial requirements                  |
| IT Administrator      | IT                 | Technical Stakeholder | Defines infrastructure, security, and technical constraints |

## 3.2 Stakeholder Priority

Stakeholders will be categorized based on their influence and involvement.

| Stakeholder         | Influence   | Involvement Priority |
| ------------------- | ----------- | -------------------- |
| Project Sponsor     | High        | High                 |
| Project Manager     | High        | High                 |
| Production Manager  | High        | High                 |
| Warehouse Manager   | High        | High                 |
| Procurement Manager | High        | High                 |
| Finance Manager     | High        | High                 |
| Quality Manager     | Medium–High | High                 |
| Maintenance Manager | Medium–High | High                 |
| End Users           | Medium      | High                 |
| IT Administrator    | High        | High                 |

---

# 4. Requirements Elicitation Methodology

A combination of elicitation techniques will be used to obtain comprehensive business requirements.

## 4.1 Stakeholder Interviews

**Purpose:** Understand stakeholder responsibilities, operational problems, business expectations, and system requirements.

Interview participants:

- Production Manager.
- Warehouse Manager.
- Procurement Manager.
- Quality Manager.
- Finance Manager.
- Maintenance Manager.

Interview format:

- Semi-structured interviews.
- Approximately 45–60 minutes per stakeholder.
- Individual interviews for process owners.
- Follow-up sessions for unresolved requirements.

Expected outputs:

- Interview notes.
- Business pain points.
- Business rules.
- Functional requirements.
- Open questions.

## 4.2 Business Process Workshops

**Purpose:** Understand cross-department workflows and identify dependencies between business processes.

Workshop participants:

- Project Manager.
- Business Analyst.
- Production.
- Warehouse.
- Procurement.
- Quality.
- Finance.

Expected outputs:

- AS-IS process flow.
- TO-BE process flow.
- Process improvement opportunities.
- Cross-functional dependencies.
- Agreed business requirements.

## 4.3 Document Analysis

Existing business documents will be reviewed to understand current operational procedures.

Examples:

| Document                      | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| Product Catalog               | Understand product definitions             |
| Bill of Materials Spreadsheet | Understand product component structures    |
| Inventory Report              | Understand stock balances                  |
| Purchase Order                | Understand procurement activities          |
| Manufacturing Order           | Understand production execution            |
| Work Order Sheet              | Understand manufacturing operations        |
| Quality Inspection Form       | Understand quality control                 |
| Maintenance Log               | Understand equipment maintenance           |
| Costing Spreadsheet           | Understand manufacturing cost calculations |

Expected outputs:

- Existing data definitions.
- Process documentation.
- Data quality issues.
- Business constraints.
- Missing information.

## 4.4 Observation

Where possible, business processes will be observed directly.

Examples:

- Receiving purchased components.
- Storing components in the warehouse.
- Issuing materials to production.
- Executing manufacturing operations.
- Performing quality inspections.
- Recording finished goods.
- Handling rejected products.

Expected outputs:

- Actual process observations.
- Process deviations.
- Manual workarounds.
- Operational bottlenecks.

## 4.5 Requirements Review Sessions

Collected requirements will be presented to stakeholders for review.

The objective is to verify that:

- Requirements accurately reflect business needs.
- Requirements are understandable.
- Requirements are not contradictory.
- Requirements are feasible.
- Requirements have clear acceptance criteria.
- Stakeholders agree with the documented requirements.

---

# 5. Interview Plan and Questionnaires

The following questions serve as the baseline interview guide.

## 5.1 Production Department

**Objective:** Understand manufacturing planning and production execution.

Questions:

1. How is production currently planned?
2. What information is required before creating a production order?
3. How are manufacturing priorities determined?
4. How are components allocated to production?
5. How are work orders assigned to operators?
6. How are work centers managed?
7. How is production progress monitored?
8. How are production delays recorded?
9. How are scrap and production losses recorded?
10. How is finished product completion validated?

Expected outputs:

- Production planning requirements.
- Manufacturing order requirements.
- Work order requirements.
- Work center requirements.
- Production reporting requirements.

## 5.2 Warehouse Department

**Objective:** Understand inventory operations and material traceability.

Questions:

1. How are incoming materials received?
2. How are materials stored?
3. How is stock availability monitored?
4. How are components issued to production?
5. How are finished goods received?
6. How are inventory adjustments performed?
7. Is lot or serial tracking required?
8. How are damaged or rejected materials handled?
9. How are stock replenishment decisions made?
10. How is inventory accuracy measured?

Expected outputs:

- Inventory management requirements.
- Warehouse operation requirements.
- Material traceability requirements.
- Replenishment requirements.

## 5.3 Procurement Department

**Objective:** Understand purchasing and supplier management.

Questions:

1. How are purchase requests initiated?
2. Who approves purchase requests?
3. How are suppliers selected?
4. How are purchase prices determined?
5. How are supplier lead times managed?
6. How are delayed deliveries handled?
7. How are incoming components validated?
8. How are supplier quality issues recorded?
9. How are purchase orders monitored?
10. How are supplier performance metrics measured?

Expected outputs:

- Procurement requirements.
- Supplier management requirements.
- Purchase approval requirements.
- Supplier performance requirements.

## 5.4 Quality Department

**Objective:** Understand quality inspection and non-conformance management.

Questions:

1. What inspection activities are performed?
2. Are incoming components inspected?
3. Are in-process inspections required?
4. What final inspections are performed?
5. What inspection criteria are used?
6. How are failed inspections handled?
7. How are non-conformities documented?
8. How are defective components managed?
9. Is lot traceability required?
10. How is quality performance measured?

Expected outputs:

- Quality inspection requirements.
- Quality control points.
- Non-conformance requirements.
- Quality reporting requirements.

## 5.5 Maintenance Department

**Objective:** Understand equipment and work center maintenance.

Questions:

1. What production equipment is maintained?
2. How are maintenance requests submitted?
3. Is preventive maintenance scheduled?
4. How are equipment breakdowns recorded?
5. How are maintenance activities prioritized?
6. How are spare parts managed?
7. How are maintenance costs recorded?
8. How is equipment availability monitored?
9. Who approves maintenance activities?
10. How is maintenance performance measured?

Expected outputs:

- Maintenance request requirements.
- Preventive maintenance requirements.
- Equipment management requirements.
- Maintenance reporting requirements.

## 5.6 Finance Department

**Objective:** Understand manufacturing costing and financial controls.

Questions:

1. How are component costs determined?
2. How are labor costs calculated?
3. How are machine operating costs calculated?
4. How is manufacturing overhead allocated?
5. How is finished product cost calculated?
6. How are inventory valuation methods determined?
7. How are manufacturing variances monitored?
8. How are cost changes approved?
9. How are inventory valuation adjustments handled?
10. What financial reports are required?

Expected outputs:

- Manufacturing costing requirements.
- Inventory valuation requirements.
- Cost approval rules.
- Financial reporting requirements.

---

# 6. Business Process Discovery

The requirements gathering process will document existing business processes before defining the proposed ERP workflows.

## 6.1 AS-IS Process Discovery

The following processes must be investigated:

| Process ID | Business Process                 | Main Participants               |
| ---------- | -------------------------------- | ------------------------------- |
| PROC-001   | Product Master Data Management   | Engineering                     |
| PROC-002   | Procurement Process              | Procurement                     |
| PROC-003   | Incoming Material Receipt        | Warehouse, Procurement, Quality |
| PROC-004   | Inventory Management             | Warehouse                       |
| PROC-005   | Manufacturing Planning           | Production                      |
| PROC-006   | Material Reservation and Issuing | Warehouse, Production           |
| PROC-007   | Manufacturing Execution          | Production                      |
| PROC-008   | Quality Inspection               | Quality                         |
| PROC-009   | Finished Goods Receipt           | Production, Warehouse           |
| PROC-010   | Manufacturing Cost Calculation   | Finance                         |

For each process, document:

- Triggering event.
- Process owner.
- Participants.
- Required inputs.
- Process activities.
- Business rules.
- Decision points.
- Outputs.
- Exceptions.
- Existing systems or spreadsheets.
- Operational problems.

## 6.2 TO-BE Process Design

After the AS-IS analysis, define the proposed business processes using Odoo 19.

The TO-BE design must specify:

- Target business workflow.
- Responsible user roles.
- Odoo application or module.
- Required master data.
- Required approvals.
- Business validations.
- Expected outputs.
- Exception handling.

---

# 7. Requirements Classification and Prioritization

All collected requirements must be categorized and prioritized.

## 7.1 Requirement Categories

| Category                   | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| Functional Requirement     | A capability the system must provide                        |
| Non-Functional Requirement | A quality, performance, security, or operational constraint |
| Business Rule              | A policy or condition governing business operations         |
| Data Requirement           | A requirement concerning master data or transactional data  |
| Reporting Requirement      | A requirement concerning reports and analytics              |
| Integration Requirement    | A requirement concerning interaction with external systems  |
| Technical Requirement      | A technical constraint or implementation requirement        |

## 7.2 MoSCoW Prioritization

The MoSCoW method will be used to prioritize requirements.

| Priority    | Definition                                 |
| ----------- | ------------------------------------------ |
| Must Have   | Essential for the initial implementation   |
| Should Have | Important but not critical for go-live     |
| Could Have  | Desirable if resources permit              |
| Won't Have  | Explicitly excluded from the current scope |

Each requirement should have:

- Unique requirement ID.
- Requirement description.
- Business justification.
- Stakeholder or source.
- Priority.
- Acceptance criteria.
- Related business process.
- Validation status.

---

# 8. Requirements Documentation and Traceability

Requirements will be maintained in the Business Requirements Document and linked to downstream implementation artifacts.

## 8.1 Requirements Traceability

The following traceability structure will be used:

| Requirement ID | Business Process       | Business Requirement                                      | Functional Specification | Test Case |
| -------------- | ---------------------- | --------------------------------------------------------- | ------------------------ | --------- |
| FR-001         | Product Management     | Product master data must be centrally managed             | FS-001                   | TC-001    |
| FR-010         | BoM Management         | Manufactured products must have approved BoMs             | FS-010                   | TC-010    |
| FR-020         | Manufacturing Planning | Users must create manufacturing orders                    | FS-020                   | TC-020    |
| FR-030         | Work Order Management  | Manufacturing operations must be assigned to work centers | FS-030                   | TC-030    |
| FR-040         | Inventory              | Materials must be reserved and issued to production       | FS-040                   | TC-040    |
| FR-050         | Quality                | Finished products must undergo final inspection           | FS-050                   | TC-050    |

The identifiers above are illustrative. Final traceability must use the approved requirement IDs in `01_business_requirements.md`.

## 8.2 Requirements Change Management

Any requirement change after approval must include:

1. Change request ID.
2. Description of the requested change.
3. Business justification.
4. Impact assessment.
5. Cost and schedule implications.
6. Approval decision.
7. Updated documentation.
8. Updated test cases, where applicable.

---

# 9. Requirements Gathering Workshop Plan

The following workshop schedule is proposed for the portfolio case study.

| Session | Topic                                      | Participants                | Duration | Deliverable                            |
| ------- | ------------------------------------------ | --------------------------- | -------- | -------------------------------------- |
| WS-001  | Project Initiation and Business Objectives | Sponsor, PM, BA             | 60 min   | Project objectives                     |
| WS-002  | Product and BoM Management                 | Engineering, Production     | 90 min   | Product and BoM requirements           |
| WS-003  | Procurement and Inventory                  | Procurement, Warehouse      | 90 min   | Procurement and inventory requirements |
| WS-004  | Manufacturing Planning and Execution       | Production, Warehouse       | 120 min  | Manufacturing requirements             |
| WS-005  | Quality and Maintenance                    | Quality, Maintenance        | 90 min   | Quality and maintenance requirements   |
| WS-006  | Costing and Financial Controls             | Finance, Production         | 90 min   | Costing requirements                   |
| WS-007  | Requirements Validation                    | All Process Owners          | 120 min  | Validated requirements                 |
| WS-008  | BRD Review and Sign-Off                    | Sponsor, PM, Process Owners | 60 min   | Approved BRD                           |

**Note:** The schedule is a proposed workshop plan, not evidence that actual stakeholder workshops have already taken place.

---

# 10. Requirements Gathering Deliverables

The following artifacts will be produced during the business analysis phase.

| Deliverable                       | File Name                               | Description                                                       |
| --------------------------------- | --------------------------------------- | ----------------------------------------------------------------- |
| Requirements Gathering Plan       | `00_business_requirements_gathering.md` | Elicitation methodology and stakeholder engagement                |
| Business Requirements Document    | `01_business_requirements.md`           | Business objectives, requirements, rules, and acceptance criteria |
| Master Data and BoM Specification | `02_master_data_and_bom.md`             | Product, component, BoM, routing, and costing definitions         |
| Business Process Flow             | `03_business_process_flow.md`           | AS-IS and TO-BE process workflows                                 |
| Functional Specification          | `04_functional_specification.md`        | Detailed system behavior and functional design                    |
| Technical Architecture            | `05_technical_architecture.md`          | Technical implementation design                                   |
| Test Strategy and Test Cases      | `06_test_strategy_and_test_cases.md`    | Test approach and validation scenarios                            |

The final file numbering should be reconciled with the actual project repository before implementation.

---

# 11. Requirements Validation and Approval

Requirements must be validated before they are treated as an approved baseline.

## 11.1 Validation Criteria

A requirement is considered valid when:

- It addresses a documented business need.
- It has a clear and unambiguous description.
- It has a defined business owner.
- It is feasible within the project scope.
- It does not conflict with another approved requirement.
- It has measurable acceptance criteria.
- Its priority is agreed upon.
- It has been reviewed by the appropriate stakeholder.

## 11.2 Approval Matrix

| Deliverable                    | Reviewer                | Approver                  |
| ------------------------------ | ----------------------- | ------------------------- |
| Business Requirements Document | Process Owners          | Project Sponsor           |
| Product and BoM Specification  | Production, Procurement | Engineering Manager       |
| Inventory Requirements         | Production, Procurement | Warehouse Manager         |
| Manufacturing Requirements     | Engineering, Warehouse  | Production Manager        |
| Costing Requirements           | Production, Procurement | Finance Manager           |
| Functional Specification       | Process Owners, IT      | Project Manager / Sponsor |

## 11.3 Sign-Off Record

| Approval Role       | Name            | Approval Date | Status  |
| ------------------- | --------------- | ------------- | ------- |
| Project Sponsor     | To Be Confirmed | Pending       | Pending |
| Project Manager     | To Be Confirmed | Pending       | Pending |
| Production Manager  | To Be Confirmed | Pending       | Pending |
| Warehouse Manager   | To Be Confirmed | Pending       | Pending |
| Procurement Manager | To Be Confirmed | Pending       | Pending |
| Finance Manager     | To Be Confirmed | Pending       | Pending |

For this portfolio project, approval records must be presented as simulated or pending unless genuine stakeholder approval has been obtained.

---

# 12. Assumptions, Constraints, and Open Questions

## 12.1 Assumptions

- Astrea Manufacturing is a hypothetical manufacturing company.
- The project uses Odoo 19.
- The initial implementation focuses on one manufacturing facility.
- WP100 and EM200 are the initial manufactured products.
- EM200 is a manufactured subassembly used in WP100.
- The initial production routing uses four work centers.
- Component specifications and costs are illustrative.
- The initial implementation uses a Linux-based environment without Docker.

## 12.2 Constraints

- Implementation scope is limited to the initial manufacturing workflow.
- Product specifications are not based on validated engineering drawings.
- Cost assumptions are not based on actual supplier quotations.
- Operational capacity assumptions require validation.
- Advanced manufacturing capabilities are excluded from the initial scope.

## 12.3 Open Questions

The following questions must be resolved before a real implementation:

| ID     | Question                                                       | Responsible Stakeholder | Status |
| ------ | -------------------------------------------------------------- | ----------------------- | ------ |
| OQ-001 | What are the approved engineering specifications for WP100?    | Engineering             | Open   |
| OQ-002 | What are the approved engineering specifications for EM200?    | Engineering             | Open   |
| OQ-003 | What are the actual supplier lead times?                       | Procurement             | Open   |
| OQ-004 | What are the actual component costs?                           | Procurement / Finance   | Open   |
| OQ-005 | What is the approved manufacturing overhead allocation method? | Finance                 | Open   |
| OQ-006 | What are the actual work center capacities?                    | Production              | Open   |
| OQ-007 | What are the standard operation times?                         | Production              | Open   |
| OQ-008 | What are the quality inspection criteria?                      | Quality                 | Open   |
| OQ-009 | What are the required lot and serial tracking policies?        | Quality / Inventory     | Open   |
| OQ-010 | What are the inventory valuation requirements?                 | Finance                 | Open   |

---

# 13. Definition of Done

The business requirements gathering phase is considered complete when:

- Stakeholders have been identified.
- Business processes have been documented.
- Existing operational challenges have been analyzed.
- Requirements have been collected and classified.
- Requirements have been prioritized.
- Business rules have been documented.
- Requirements have measurable acceptance criteria.
- Open questions have been assigned to responsible stakeholders.
- Requirements have been reviewed and validated.
- The BRD has been approved or formally marked as a portfolio simulation baseline.
- Requirements traceability has been established.

---

# 14. Final Statement

Business requirements gathering is the foundation of a successful ERP implementation.

The objective is not simply to collect a list of requested features, but to understand the business processes, identify underlying problems, establish operational rules, and define measurable outcomes.

For Astrea Manufacturing, the requirements gathering process will establish the business foundation for the Odoo 19 Manufacturing ERP implementation.

All requirements, process assumptions, and cost estimates must be validated before they are treated as actual production policies.

**Document Status:** Draft — Portfolio Case Study
**Next Deliverable:** Business Requirements Document (`01_business_requirements.md`)
