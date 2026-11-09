# Stakeholder Interview Questions & Elicitation Guide

**Project:** Astra Manufacturing — Manufacturing & Production Management ERP  
**ERP Platform:** Odoo 19  
**Document Type:** Stakeholder Interview Guide  
**Version:** 1.0  
**Status:** Draft — Portfolio Case Study  
**Prepared By:** Business Analyst / ERP Consultant

---

# 1. Document Purpose

This document provides a structured interview guide for gathering business requirements from stakeholders involved in Astra Manufacturing's ERP implementation project.

The objective is to understand existing business processes, operational challenges, business rules, data requirements, system expectations, and improvement opportunities.

The collected information will be used as input for:

- Business Requirements Document (BRD).
- AS-IS and TO-BE business process documentation.
- Master data and BoM specification.
- Functional specification.
- Requirements traceability matrix.
- ERP configuration and implementation.
- User acceptance testing (UAT).

**Important:** Astra Manufacturing is a hypothetical portfolio case study. Interview responses, findings, and stakeholder approvals must be marked as simulated unless actual interviews have been conducted.

---

# 2. Interview Guidelines

## 2.1 Interview Objectives

Each interview should establish:

1. The stakeholder's responsibilities.
2. The existing business process.
3. The systems and tools currently used.
4. Operational problems and bottlenecks.
5. Business rules and approval requirements.
6. Data requirements.
7. Reporting requirements.
8. Expected improvements from ERP implementation.
9. Functional and non-functional requirements.
10. Potential risks and implementation constraints.

## 2.2 Interview Format

| Attribute | Description |
|---|---|
| Interview Type | Semi-structured interview |
| Duration | 45–60 minutes |
| Interviewer | Business Analyst / ERP Consultant |
| Interviewee | Department Manager / Supervisor / End User |
| Method | Face-to-face or online meeting |
| Documentation | Interview notes and requirement log |
| Follow-up | Additional clarification sessions when required |

## 2.3 Interview Techniques

Use the following techniques during interviews:

**Open-ended questions**

Encourage stakeholders to explain their actual working processes.

Example:

"Can you explain how your department currently handles production planning?"

**Probing questions**

Explore specific details when an answer is too general.

Example:

"You mentioned that production planning is performed manually. What information do you use to determine the production quantity?"

**Scenario-based questions**

Ask stakeholders to explain how they handle specific operational situations.

Example:

"What happens when a manufacturing order cannot proceed because one component is unavailable?"

**Validation questions**

Confirm that the information collected accurately represents the business process.

Example:

"Based on your explanation, the warehouse reserves components before production starts. Is this the correct sequence?"

---

# 3. Stakeholder Interview Schedule

| Interview ID | Department | Interviewee | Duration | Priority |
|---|---|---|---|---|
| INT-001 | Management | Project Sponsor | 45 min | High |
| INT-002 | Production | Production Manager | 60 min | High |
| INT-003 | Production | Production Supervisor | 60 min | High |
| INT-004 | Engineering | Engineering Manager | 60 min | High |
| INT-005 | Inventory | Warehouse Manager | 60 min | High |
| INT-006 | Inventory | Warehouse Staff | 45 min | High |
| INT-007 | Procurement | Procurement Manager | 60 min | High |
| INT-008 | Procurement | Procurement Staff | 45 min | Medium |
| INT-009 | Quality | Quality Manager | 60 min | High |
| INT-010 | Maintenance | Maintenance Manager | 60 min | Medium |
| INT-011 | Finance | Finance Manager | 60 min | High |
| INT-012 | IT | IT Administrator | 45 min | Medium |

The interview sequence should be adjusted based on stakeholder availability and business dependencies.

---

# 4. Project Sponsor Interview

**Interview ID:** INT-001  
**Department:** Management  
**Role:** Project Sponsor  
**Duration:** 45 minutes

## 4.1 Interview Objectives

Understand the company's strategic objectives, business priorities, expected ERP outcomes, project constraints, and success criteria.

## 4.2 Business Strategy and Objectives

| ID | Interview Question | Information to Capture |
|---|---|---|
| SP-001 | What are the company's primary business objectives for the next 1–3 years? | Strategic business goals |
| SP-002 | What are the biggest operational challenges currently affecting the business? | Business pain points |
| SP-003 | Why is the company considering an ERP implementation? | Business justification |
| SP-004 | Which business processes need the most improvement? | Improvement priorities |
| SP-005 | What business outcomes are expected from implementing Odoo? | Expected business value |

## 4.3 Project Expectations

| ID | Interview Question | Information to Capture |
|---|---|---|
| SP-006 | What are the most important outcomes expected from this project? | Project objectives |
| SP-007 | Which departments should be included in the initial implementation? | Project scope |
| SP-008 | What is the expected implementation timeline? | Project schedule |
| SP-009 | Are there budget or resource constraints? | Project constraints |
| SP-010 | What are the biggest risks associated with this implementation? | Project risks |

## 4.4 Success Criteria

| ID | Interview Question | Information to Capture |
|---|---|---|
| SP-011 | How will management measure ERP implementation success? | Success metrics |
| SP-012 | Which KPIs should management monitor? | KPI requirements |
| SP-013 | What level of inventory accuracy is expected? | Inventory KPI target |
| SP-014 | What production performance indicators are important? | Manufacturing KPI |
| SP-015 | What reporting capabilities are required by management? | Management reporting |

## 4.5 Expected Outputs

- Business objectives.
- Project scope.
- Strategic priorities.
- Project constraints.
- Success criteria.
- Management reporting requirements.

---

# 5. Production Manager Interview

**Interview ID:** INT-002  
**Department:** Production  
**Role:** Production Manager  
**Duration:** 60 minutes

## 5.1 Interview Objectives

Understand production planning, manufacturing execution, work center utilization, production performance, and operational controls.

## 5.2 Production Planning

| ID | Interview Question | Information to Capture |
|---|---|---|
| PRD-001 | How is production currently planned? | Production planning process |
| PRD-002 | What information is required before creating a production plan? | Planning inputs |
| PRD-003 | How are production quantities determined? | Production quantity rules |
| PRD-004 | Is production based on sales orders, forecasts, or minimum stock levels? | MTS / MTO strategy |
| PRD-005 | How frequently are production plans reviewed? | Planning frequency |
| PRD-006 | How are urgent production orders prioritized? | Priority rules |
| PRD-007 | How are production schedules communicated to operators? | Scheduling process |

## 5.3 Manufacturing Orders

| ID | Interview Question | Information to Capture |
|---|---|---|
| PRD-008 | Who is authorized to create manufacturing orders? | Authorization rules |
| PRD-009 | What information must be available before an order is confirmed? | MO prerequisites |
| PRD-010 | How are components allocated to manufacturing orders? | Material allocation |
| PRD-011 | How are partially completed manufacturing orders handled? | Partial production process |
| PRD-012 | How are production quantities adjusted? | Quantity adjustment rules |
| PRD-013 | How are cancelled manufacturing orders handled? | Cancellation process |

## 5.4 Work Orders and Work Centers

| ID | Interview Question | Information to Capture |
|---|---|---|
| PRD-014 | What work centers are currently available? | Work center inventory |
| PRD-015 | What operations are performed at each work center? | Operation definitions |
| PRD-016 | How are operations assigned to work centers? | Routing rules |
| PRD-017 | What is the standard processing time for each operation? | Standard operation duration |
| PRD-018 | What is the production capacity of each work center? | Work center capacity |
| PRD-019 | How are machine breakdowns handled during production? | Exception handling |
| PRD-020 | Can operations be transferred to alternative work centers? | Alternative work center rules |

## 5.5 Production Monitoring

| ID | Interview Question | Information to Capture |
|---|---|---|
| PRD-021 | How is production progress monitored? | Production monitoring |
| PRD-022 | How are actual production times recorded? | Actual operation time |
| PRD-023 | How are production delays recorded? | Delay tracking |
| PRD-024 | How are defective products and scrap quantities recorded? | Scrap management |
| PRD-025 | How is production efficiency measured? | Production KPIs |
| PRD-026 | What production reports are required? | Reporting requirements |

## 5.6 Expected Outputs

- Manufacturing planning requirements.
- Manufacturing order rules.
- Work center definitions.
- Routing requirements.
- Production scheduling rules.
- Production monitoring requirements.
- Manufacturing KPIs.

---

# 6. Production Supervisor Interview

**Interview ID:** INT-003  
**Department:** Production  
**Role:** Production Supervisor  
**Duration:** 60 minutes

## 6.1 Interview Objectives

Understand actual shop-floor activities, operator workflows, material consumption, operation completion, and production exceptions.

## 6.2 Daily Production Activities

| ID | Interview Question | Information to Capture |
|---|---|---|
| SUP-001 | How do operators receive their daily production assignments? | Work assignment process |
| SUP-002 | How are work instructions communicated? | Work instruction method |
| SUP-003 | How do operators confirm that an operation has started? | Operation start process |
| SUP-004 | How do operators report completed operations? | Operation completion |
| SUP-005 | How are actual production quantities recorded? | Production quantity recording |

## 6.3 Production Issues

| ID | Interview Question | Information to Capture |
|---|---|---|
| SUP-006 | What are the most common reasons for production delays? | Delay causes |
| SUP-007 | How are missing components reported? | Material shortage process |
| SUP-008 | How are defective components handled during assembly? | Defect handling |
| SUP-009 | What happens when an operation must be repeated? | Rework process |
| SUP-010 | How are machine downtime and operator downtime recorded? | Downtime tracking |

## 6.4 Production Documentation

| ID | Interview Question | Information to Capture |
|---|---|---|
| SUP-011 | What forms or documents are used during production? | Production documents |
| SUP-012 | Are operators required to record material consumption manually? | Material consumption recording |
| SUP-013 | How are work order completion records maintained? | Production records |
| SUP-014 | How are production issues escalated? | Escalation procedure |
| SUP-015 | What information would make daily production activities easier? | User expectations |

## 6.5 Expected Outputs

- Shop-floor process requirements.
- Operator workflow.
- Production exception handling.
- Actual time recording requirements.
- Production documentation requirements.

---

# 7. Engineering Manager Interview

**Interview ID:** INT-004  
**Department:** Engineering  
**Role:** Engineering Manager  
**Duration:** 60 minutes

## 7.1 Interview Objectives

Understand product specifications, product structures, engineering master data, BoM governance, routing validation, and engineering change management.

## 7.2 Product Master Data

| ID | Interview Question | Information to Capture |
|---|---|---|
| ENG-001 | How are new products defined and approved? | Product creation process |
| ENG-002 | What information is required for each product? | Product master fields |
| ENG-003 | How are product codes assigned? | Naming convention |
| ENG-004 | How are product categories determined? | Product classification |
| ENG-005 | How are engineering specifications maintained? | Product documentation |

## 7.3 Bill of Materials

| ID | Interview Question | Information to Capture |
|---|---|---|
| ENG-006 | How is a Bill of Materials currently created? | BoM creation process |
| ENG-007 | Who is responsible for validating BoM quantities? | BoM ownership |
| ENG-008 | Are products manufactured using multi-level BoMs? | BoM hierarchy |
| ENG-009 | How are alternative components handled? | Component substitution |
| ENG-010 | How are material losses and production scrap reflected in the BoM? | Scrap assumptions |
| ENG-011 | How are BoM changes approved? | Engineering change control |
| ENG-012 | How are historical BoM revisions maintained? | Revision management |

## 7.4 Routing and Operations

| ID | Interview Question | Information to Capture |
|---|---|---|
| ENG-013 | How are manufacturing operations defined? | Operation definitions |
| ENG-014 | Who determines operation sequences? | Routing ownership |
| ENG-015 | How are standard operation durations determined? | Standard time |
| ENG-016 | What technical instructions are required for each operation? | Work instructions |
| ENG-017 | How are engineering changes communicated to Production? | Change communication |

## 7.5 Expected Outputs

- Product master requirements.
- Product coding standards.
- BoM structure.
- BoM revision policy.
- Component specifications.
- Routing requirements.
- Engineering change management rules.

---

# 8. Warehouse Manager Interview

**Interview ID:** INT-005  
**Department:** Inventory  
**Role:** Warehouse Manager  
**Duration:** 60 minutes

## 8.1 Interview Objectives

Understand inventory organization, receiving, storage, material reservation, stock movements, replenishment, and traceability.

## 8.2 Warehouse Structure

| ID | Interview Question | Information to Capture |
|---|---|---|
| WH-001 | How many warehouses are currently operated? | Warehouse structure |
| WH-002 | How are warehouse locations organized? | Location hierarchy |
| WH-003 | How are raw materials separated from finished products? | Storage strategy |
| WH-004 | Are separate locations used for rejected or quarantined materials? | Quality locations |
| WH-005 | How are stock transfers between locations handled? | Internal transfer process |

## 8.3 Incoming Inventory

| ID | Interview Question | Information to Capture |
|---|---|---|
| WH-006 | How are incoming materials received? | Receiving process |
| WH-007 | How are received quantities verified? | Quantity validation |
| WH-008 | How are supplier discrepancies handled? | Receiving exceptions |
| WH-009 | Is incoming quality inspection required before stock becomes available? | Quality integration |
| WH-010 | How are received products identified and labeled? | Product identification |

## 8.4 Material Issuing and Production

| ID | Interview Question | Information to Capture |
|---|---|---|
| WH-011 | How are components issued to production? | Material issuing |
| WH-012 | Are materials reserved before production begins? | Reservation policy |
| WH-013 | How are material shortages identified? | Shortage management |
| WH-014 | How are excess components returned from production? | Material return process |
| WH-015 | How are damaged materials handled? | Damaged stock process |

## 8.5 Inventory Control

| ID | Interview Question | Information to Capture |
|---|---|---|
| WH-016 | How frequently are stock counts performed? | Cycle counting |
| WH-017 | How are inventory adjustments approved? | Adjustment approval |
| WH-018 | Is lot or serial number tracking required? | Traceability requirements |
| WH-019 | How are obsolete materials identified? | Obsolete stock management |
| WH-020 | Which inventory KPIs are monitored? | Inventory performance |

## 8.6 Expected Outputs

- Warehouse structure.
- Inventory location requirements.
- Receiving and delivery processes.
- Material reservation rules.
- Inventory adjustment rules.
- Traceability requirements.
- Replenishment policies.

---

# 9. Warehouse Staff Interview

**Interview ID:** INT-006  
**Department:** Inventory  
**Role:** Warehouse Staff  
**Duration:** 45 minutes

## 9.1 Interview Objectives

Understand the actual warehouse execution workflow and identify manual activities, operational issues, and usability requirements.

## 9.2 Daily Warehouse Operations

| ID | Interview Question | Information to Capture |
|---|---|---|
| WST-001 | How do you identify products when receiving materials? | Product identification |
| WST-002 | How do you verify received quantities? | Receiving procedure |
| WST-003 | How do you determine where materials should be stored? | Putaway process |
| WST-004 | How do you identify available stock? | Stock visibility |
| WST-005 | How do you prepare materials for production? | Material picking |

## 9.3 Operational Challenges

| ID | Interview Question | Information to Capture |
|---|---|---|
| WST-006 | What are the most common inventory discrepancies? | Stock accuracy problems |
| WST-007 | What makes material picking difficult? | Picking bottlenecks |
| WST-008 | How do you handle unexpected material shortages? | Exception handling |
| WST-009 | How are inventory errors reported? | Error reporting |
| WST-010 | What information is difficult to access during daily work? | Information gaps |

## 9.4 Expected Outputs

- Warehouse user requirements.
- Picking and receiving workflow.
- Inventory usability requirements.
- Common operational exceptions.

---

# 10. Procurement Manager Interview

**Interview ID:** INT-007  
**Department:** Procurement  
**Role:** Procurement Manager  
**Duration:** 60 minutes

## 10.1 Interview Objectives

Understand procurement planning, supplier management, purchasing approval, supplier performance, and replenishment processes.

## 10.2 Procurement Planning

| ID | Interview Question | Information to Capture |
|---|---|---|
| PUR-001 | How are purchasing requirements identified? | Procurement triggers |
| PUR-002 | Are purchases based on minimum stock levels or production demand? | Replenishment strategy |
| PUR-003 | How are supplier lead times determined? | Supplier lead times |
| PUR-004 | How are purchase quantities determined? | Purchasing quantity rules |
| PUR-005 | How are urgent purchasing requirements handled? | Urgent purchasing process |

## 10.3 Supplier Management

| ID | Interview Question | Information to Capture |
|---|---|---|
| PUR-006 | How are suppliers selected and approved? | Supplier approval |
| PUR-007 | Are multiple suppliers maintained for one component? | Alternative suppliers |
| PUR-008 | How are supplier prices negotiated? | Pricing process |
| PUR-009 | How are supplier delivery performances evaluated? | Supplier KPIs |
| PUR-010 | How are supplier quality issues handled? | Supplier quality management |

## 10.4 Purchase Order Management

| ID | Interview Question | Information to Capture |
|---|---|---|
| PUR-011 | Who can create purchase orders? | Purchase authorization |
| PUR-012 | Who approves purchase orders? | Approval hierarchy |
| PUR-013 | Are purchase orders subject to spending limits? | Approval thresholds |
| PUR-014 | How are purchase order changes handled? | Purchase modification |
| PUR-015 | How are partial supplier deliveries handled? | Partial receipt process |
| PUR-016 | How are supplier invoices matched with purchase orders and receipts? | Three-way matching requirements |

## 10.5 Expected Outputs

- Procurement workflow.
- Supplier management requirements.
- Purchasing approval matrix.
- Replenishment rules.
- Supplier performance requirements.
- Purchase reporting requirements.

---

# 11. Procurement Staff Interview

**Interview ID:** INT-008  
**Department:** Procurement  
**Role:** Procurement Staff  
**Duration:** 45 minutes

## 11.1 Interview Objectives

Understand daily purchasing activities, supplier communication, purchase order processing, and procurement documentation.

## 11.2 Daily Purchasing Activities

| ID | Interview Question | Information to Capture |
|---|---|---|
| PST-001 | How do you receive purchasing requests? | Purchase request process |
| PST-002 | How do you select suppliers? | Supplier selection |
| PST-003 | How do you compare supplier quotations? | Price comparison |
| PST-004 | How do you create purchase orders? | PO creation |
| PST-005 | How do you monitor purchase order status? | PO tracking |

## 11.3 Supplier Communication

| ID | Interview Question | Information to Capture |
|---|---|---|
| PST-006 | How are supplier delivery dates confirmed? | Delivery confirmation |
| PST-007 | How are delivery delays communicated? | Delay communication |
| PST-008 | How are price changes documented? | Price change records |
| PST-009 | How are supplier disputes handled? | Dispute management |
| PST-010 | What purchasing documents are maintained? | Procurement documentation |

## 11.4 Expected Outputs

- Purchase order execution requirements.
- Supplier communication process.
- Purchasing documentation requirements.
- Procurement exception handling.

---

# 12. Quality Manager Interview

**Interview ID:** INT-009  
**Department:** Quality  
**Role:** Quality Manager  
**Duration:** 60 minutes

## 12.1 Interview Objectives

Understand incoming inspection, in-process inspection, final inspection, quality standards, non-conformance management, and product traceability.

## 12.2 Quality Inspection Process

| ID | Interview Question | Information to Capture |
|---|---|---|
| QA-001 | What quality inspections are currently performed? | Inspection types |
| QA-002 | Are incoming components inspected? | Incoming inspection |
| QA-003 | Which manufacturing operations require in-process inspection? | In-process inspection |
| QA-004 | What tests are required before finished products are released? | Final inspection |
| QA-005 | What are the inspection criteria for WP100? | Product quality standards |
| QA-006 | What are the inspection criteria for EM200? | Product quality standards |
| QA-007 | Who is authorized to approve inspection results? | Quality approval |

## 12.3 Non-Conformance Management

| ID | Interview Question | Information to Capture |
|---|---|---|
| QA-008 | How are failed inspections documented? | Non-conformance records |
| QA-009 | How are defective materials isolated? | Quarantine process |
| QA-010 | Can defective products be reworked? | Rework process |
| QA-011 | How are scrap decisions approved? | Scrap approval |
| QA-012 | How are supplier quality issues escalated? | Supplier quality escalation |

## 12.4 Traceability and Reporting

| ID | Interview Question | Information to Capture |
|---|---|---|
| QA-013 | Is lot or serial number traceability required? | Traceability policy |
| QA-014 | How are inspection results stored? | Quality records |
| QA-015 | How are recurring quality problems analyzed? | Root cause analysis |
| QA-016 | Which quality KPIs are monitored? | Quality performance |
| QA-017 | What quality reports are required? | Reporting requirements |

## 12.5 Expected Outputs

- Quality inspection requirements.
- Quality control points.
- Inspection criteria.
- Non-conformance workflow.
- Rework and scrap rules.
- Quality KPIs.

---

# 13. Maintenance Manager Interview

**Interview ID:** INT-010  
**Department:** Maintenance  
**Role:** Maintenance Manager  
**Duration:** 60 minutes

## 13.1 Interview Objectives

Understand equipment management, preventive maintenance, corrective maintenance, breakdown reporting, spare parts, and maintenance performance.

## 13.2 Equipment Management

| ID | Interview Question | Information to Capture |
|---|---|---|
| MNT-001 | What machines and equipment are used in production? | Equipment register |
| MNT-002 | How are equipment assets identified? | Asset identification |
| MNT-003 | What maintenance information is recorded for each machine? | Equipment master data |
| MNT-004 | How is equipment availability monitored? | Equipment availability |
| MNT-005 | Which work centers are most critical to production? | Critical equipment |

## 13.3 Maintenance Activities

| ID | Interview Question | Information to Capture |
|---|---|---|
| MNT-006 | How is preventive maintenance scheduled? | Preventive maintenance |
| MNT-007 | How are maintenance requests submitted? | Maintenance request |
| MNT-008 | How are breakdowns prioritized? | Maintenance priority |
| MNT-009 | How are maintenance activities recorded? | Maintenance history |
| MNT-010 | How are recurring equipment failures handled? | Failure management |

## 13.4 Spare Parts and Cost

| ID | Interview Question | Information to Capture |
|---|---|---|
| MNT-011 | How are spare parts managed? | Spare parts inventory |
| MNT-012 | How are maintenance material requirements identified? | Maintenance procurement |
| MNT-013 | How are maintenance costs calculated? | Maintenance cost |
| MNT-014 | How are external maintenance services managed? | Outsourced maintenance |
| MNT-015 | Which maintenance KPIs are monitored? | MTBF, MTTR, availability |

## 13.5 Expected Outputs

- Equipment master data requirements.
- Preventive maintenance requirements.
- Corrective maintenance workflow.
- Spare parts requirements.
- Maintenance performance metrics.

---

# 14. Finance Manager Interview

**Interview ID:** INT-011  
**Department:** Finance  
**Role:** Finance Manager  
**Duration:** 60 minutes

## 14.1 Interview Objectives

Understand product costing, inventory valuation, manufacturing overhead allocation, financial controls, and cost reporting.

## 14.2 Product Costing

| ID | Interview Question | Information to Capture |
|---|---|---|
| FIN-001 | How are raw material costs determined? | Material cost methodology |
| FIN-002 | How are purchased component costs maintained? | Component cost management |
| FIN-003 | How are direct labor costs calculated? | Labor cost methodology |
| FIN-004 | How are machine operating costs calculated? | Work center cost |
| FIN-005 | How is manufacturing overhead allocated? | Overhead allocation |
| FIN-006 | How is finished product cost calculated? | Product cost methodology |
| FIN-007 | How are subassembly costs incorporated into finished product costs? | Multi-level costing |

## 14.3 Inventory Valuation

| ID | Interview Question | Information to Capture |
|---|---|---|
| FIN-008 | Which inventory valuation method is currently used? | Standard Price, AVCO, FIFO |
| FIN-009 | Is inventory valuation automated or manually recorded? | Valuation process |
| FIN-010 | How are inventory adjustments approved? | Financial approval |
| FIN-011 | How are inventory valuation differences handled? | Valuation adjustments |
| FIN-012 | How are manufacturing variances monitored? | Cost variance |

## 14.4 Financial Controls and Reporting

| ID | Interview Question | Information to Capture |
|---|---|---|
| FIN-013 | Who can approve product cost changes? | Cost approval authority |
| FIN-014 | What accounting entries are expected during manufacturing? | Accounting requirements |
| FIN-015 | How are production costs reconciled with inventory valuation? | Cost reconciliation |
| FIN-016 | What financial reports are required? | Financial reporting |
| FIN-017 | How frequently are manufacturing costs reviewed? | Cost review frequency |

## 14.5 Expected Outputs

- Product costing methodology.
- Inventory valuation policy.
- Manufacturing overhead rules.
- Financial approval matrix.
- Manufacturing cost reporting requirements.

---

# 15. IT Administrator Interview

**Interview ID:** INT-012  
**Department:** IT  
**Role:** IT Administrator  
**Duration:** 45 minutes

## 15.1 Interview Objectives

Understand technical infrastructure, security, access management, backup, availability, integration, and system administration requirements.

## 15.2 Infrastructure

| ID | Interview Question | Information to Capture |
|---|---|---|
| IT-001 | Where will Odoo be hosted? | Hosting architecture |
| IT-002 | What operating system and infrastructure are available? | Infrastructure environment |
| IT-003 | What database technology is required? | Database requirements |
| IT-004 | How many concurrent users are expected? | User capacity |
| IT-005 | What are the expected system availability requirements? | Availability requirements |

## 15.3 Security and Access

| ID | Interview Question | Information to Capture |
|---|---|---|
| IT-006 | How are user accounts managed? | User provisioning |
| IT-007 | What authentication policies are required? | Authentication |
| IT-008 | How should access permissions be assigned? | Role-based access |
| IT-009 | Are audit logs required for sensitive operations? | Audit requirements |
| IT-010 | How are user access changes handled? | Access governance |

## 15.4 Backup and Integration

| ID | Interview Question | Information to Capture |
|---|---|---|
| IT-011 | How frequently should the database be backed up? | Backup frequency |
| IT-012 | What recovery time is acceptable? | RTO |
| IT-013 | What data loss window is acceptable? | RPO |
| IT-014 | Are integrations with external systems required? | Integration scope |
| IT-015 | How will system upgrades and maintenance be managed? | Maintenance strategy |

## 15.5 Expected Outputs

- Infrastructure requirements.
- Security requirements.
- User access management.
- Backup and recovery requirements.
- Integration requirements.
- System maintenance requirements.

---

# 16. Cross-Functional Scenario Questions

Department-specific interviews should be supplemented with cross-functional scenarios to discover process dependencies and conflicting expectations.

## 16.1 Material Shortage Scenario

**Scenario:** Production has a confirmed manufacturing order, but one required component is unavailable.

Questions:

1. How is the shortage identified?
2. Who is notified?
3. Who is responsible for replenishment?
4. Can production proceed with partial material availability?
5. Is an alternative component permitted?
6. Who approves component substitution?
7. How is the manufacturing schedule updated?

Participants:

- Production.
- Warehouse.
- Procurement.
- Engineering.

Expected findings:

- Material shortage workflow.
- Replenishment rules.
- Production rescheduling.
- Component substitution approval.

## 16.2 Failed Quality Inspection Scenario

**Scenario:** A finished WP100 fails the final quality inspection.

Questions:

1. Who records the inspection failure?
2. Where is the defective product stored?
3. Can the product be reworked?
4. Who approves rework?
5. How are additional materials and labor recorded?
6. When can the product be released?
7. How is the failure linked to its production lot?

Participants:

- Quality.
- Production.
- Warehouse.
- Finance.

Expected findings:

- Quality failure workflow.
- Quarantine process.
- Rework authorization.
- Scrap management.
- Traceability requirements.

## 16.3 Machine Breakdown Scenario

**Scenario:** The Assembly Work Center becomes unavailable during production.

Questions:

1. Who reports the breakdown?
2. How is production affected?
3. Is an alternative work center available?
4. Who approves reassignment?
5. How are downtime hours recorded?
6. How is the production schedule updated?
7. How are maintenance costs recorded?

Participants:

- Production.
- Maintenance.
- Project Management.

Expected findings:

- Breakdown management.
- Work center availability.
- Alternative routing.
- Downtime reporting.
- Maintenance integration.

## 16.4 Engineering Change Scenario

**Scenario:** Engineering changes the specification of a component used in the WP100 BoM.

Questions:

1. Who initiates the change?
2. Who reviews and approves the new specification?
3. How is the BoM updated?
4. What happens to existing stock?
5. What happens to ongoing manufacturing orders?
6. When does the new revision become effective?
7. How are historical production records preserved?

Participants:

- Engineering.
- Production.
- Procurement.
- Warehouse.
- Quality.

Expected findings:

- Engineering change management.
- BoM revision control.
- Effective-date policy.
- Inventory disposition.
- Production order impact assessment.

## 16.5 Manufacturing Cost Variance Scenario

**Scenario:** Actual manufacturing cost is higher than the expected standard cost.

Questions:

1. How is the variance identified?
2. Which cost elements are analyzed?
3. How are material price differences handled?
4. How are labor and machine variances measured?
5. Who investigates the variance?
6. Who approves cost adjustments?
7. How are corrective actions monitored?

Participants:

- Finance.
- Production.
- Procurement.
- Engineering.

Expected findings:

- Cost variance reporting.
- Cost analysis requirements.
- Approval rules.
- Corrective action workflow.

---

# 17. Requirement Discovery and Analysis Template

Every significant finding from an interview must be evaluated before it becomes an approved requirement.

Use the following structure.

| Attribute | Description |
|---|---|
| Finding ID | Unique identifier |
| Interview ID | Related interview |
| Stakeholder | Source of information |
| Business Process | Related business process |
| Current Situation | Existing process or problem |
| Business Problem | Identified issue |
| Business Impact | Effect on the business |
| Root Cause | Suspected or validated cause |
| Business Need | Required improvement |
| Proposed Requirement | Expected system capability |
| Priority | MoSCoW classification |
| Acceptance Criteria | Measurable expected outcome |
| Validation Status | Draft, Reviewed, Approved |

## 17.1 Example Requirement Discovery

**Interview ID:** INT-002

**Stakeholder:** Production Manager

**Question:** How are components allocated to manufacturing orders?

**Illustrative Interview Response:**

"Production currently checks component availability manually using an inventory spreadsheet. When components are unavailable, the production team contacts the warehouse to confirm stock status."

**Current Situation:**

Component availability is checked manually before production begins.

**Business Problem:**

Manual stock verification creates delays and increases the possibility of incorrect production planning.

**Business Impact:**

- Production delays.
- Increased manual communication.
- Inaccurate production planning.
- Reduced inventory visibility.

**Root Cause:**

Inventory and production planning information are not managed through an integrated workflow.

**Business Need:**

Production must be able to identify component availability before confirming production execution.

**Proposed Functional Requirement:**

`FR-040: The system must provide component availability visibility and support material reservation for manufacturing orders.`

**Priority:** Must Have

**Illustrative Acceptance Criteria:**

- Users can identify required components for a manufacturing order.
- The system displays relevant component availability.
- Material reservations are reflected in inventory availability.
- Insufficient component availability can be identified before production execution.

**Validation Status:** Simulated — Pending Stakeholder Validation

---

# 18. Interview Notes Template

Use this template for every stakeholder interview.

## Interview Information

| Attribute | Value |
|---|---|
| Interview ID | INT-XXX |
| Department | To Be Completed |
| Interviewee | To Be Completed |
| Position | To Be Completed |
| Interviewer | To Be Completed |
| Interview Date | YYYY-MM-DD |
| Start Time | HH:MM |
| End Time | HH:MM |
| Interview Method | Online / Face-to-face |
| Interview Status | Planned / Completed / Follow-up Required |

## Interview Summary

**1. Department Responsibilities**

To be completed after the interview.

**2. Existing Business Process**

To be completed after the interview.

**3. Existing Systems and Tools**

To be completed after the interview.

**4. Main Business Problems**

To be completed after the interview.

**5. Business Requirements Identified**

To be completed after the interview.

**6. Business Rules Identified**

To be completed after the interview.

**7. Reporting Requirements**

To be completed after the interview.

**8. Open Questions**

To be completed after the interview.

**9. Agreed Actions**

To be completed after the interview.

**10. Follow-up Required**

Yes / No

---

# 19. Interview Findings and Action Log

All findings and follow-up actions should be tracked centrally.

| Finding ID | Interview ID | Finding Description | Responsible | Priority | Status |
|---|---|---|---|---|---|
| FIND-001 | INT-002 | Production component availability must be visible before execution | Production / Warehouse | High | Open |
| FIND-002 | INT-004 | BoM changes require formal approval | Engineering | High | Open |
| FIND-003 | INT-005 | Inventory traceability policy needs confirmation | Warehouse / Quality | High | Open |
| FIND-004 | INT-007 | Supplier lead times must be maintained | Procurement | Medium | Open |
| FIND-005 | INT-009 | Final inspection criteria must be documented | Quality | High | Open |
| FIND-006 | INT-011 | Manufacturing overhead allocation requires confirmation | Finance | High | Open |

**Note:** These are illustrative findings for the portfolio simulation. They must not be presented as actual stakeholder interview results.

---

# 20. Interview Completion Checklist

## Before the Interview

- [ ] Identify the stakeholder.
- [ ] Understand the stakeholder's department.
- [ ] Review relevant business requirements.
- [ ] Prepare department-specific questions.
- [ ] Define the interview objectives.
- [ ] Schedule the interview.
- [ ] Prepare the interview notes template.

## During the Interview

- [ ] Explain the purpose of the interview.
- [ ] Understand the stakeholder's responsibilities.
- [ ] Document the current business process.
- [ ] Identify operational problems.
- [ ] Ask follow-up questions.
- [ ] Capture business rules.
- [ ] Identify reporting requirements.
- [ ] Record open questions.
- [ ] Confirm important findings with the stakeholder.

## After the Interview

- [ ] Consolidate interview notes.
- [ ] Identify business problems.
- [ ] Analyze root causes.
- [ ] Identify business needs.
- [ ] Draft functional requirements.
- [ ] Identify non-functional requirements.
- [ ] Record business rules.
- [ ] Assign requirement priorities.
- [ ] Update the requirements log.
- [ ] Schedule follow-up sessions if necessary.
- [ ] Validate the findings with the stakeholder.

---

# 21. Final Deliverables

The stakeholder interview process should produce the following artifacts:

| Deliverable | Description |
|---|---|
| Interview Schedule | Planned stakeholder interview sessions |
| Interview Notes | Documented interview discussions |
| Stakeholder Findings | Consolidated business observations |
| Business Pain Points | Identified operational problems |
| Business Rules | Policies and operational constraints |
| Functional Requirements | Required system capabilities |
| Non-Functional Requirements | Performance, security, and operational requirements |
| Open Questions | Unresolved business questions |
| Action Log | Follow-up actions and ownership |
| Requirements Log | Consolidated requirements with traceability |

---

# 22. Final Statement

Stakeholder interviews are a critical part of ERP business analysis.

The objective is not simply to ask stakeholders which features they want. The Business Analyst must understand the actual operational process, investigate underlying business problems, identify root causes, and translate validated business needs into clear and testable requirements.

For Astra Manufacturing, the interview findings will provide the foundation for defining the future manufacturing processes and configuring Odoo 19.

**Document Status:** Draft — Portfolio Case Study  
**Next Step:** Conduct or simulate structured stakeholder interviews, document findings, and validate the resulting requirements before updating the BRD.